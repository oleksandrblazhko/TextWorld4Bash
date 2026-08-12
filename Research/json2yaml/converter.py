import re

def clean_description_text(desc, door_states, container_states):
    """
    Evaluates conditional templates [if ...] in room/entity descriptions
    and removes conditional blocks to keep descriptions clean and formatted.
    """
    if not desc:
        return ""
    
    def replace_cond(match):
        cond = match.group(1).strip()
        content = match.group(2)
        
        parts = cond.split()
        if len(parts) >= 3 and parts[1] == 'is':
            entity_id = parts[0]
            state_val = parts[2]
            
            # Retrieve the entity status (default to 'closed' for doors/containers if not set)
            status = door_states.get(entity_id) or container_states.get(entity_id) or 'closed'
            
            if 'otherwise' in content or 'else if' in content:
                # Handle status conditions with alternatives
                if 'locked' in cond and status == 'locked':
                    return content.split('[')[0]
                elif 'open' in cond and status == 'open':
                    return content.split('[')[0]
                elif 'closed' in cond and status == 'closed':
                    return content.split('[')[0]
                elif 'else if' in content:
                    else_match = re.search(r'\[else if\s+' + re.escape(entity_id) + r'\s+is\s+([^\]]+)\]([^\[]+)', content)
                    if else_match:
                        else_state = else_match.group(1)
                        else_text = else_match.group(2)
                        if status == else_state:
                            return else_text
                
                if '[otherwise]' in content:
                    return content.split('[otherwise]')[1].split('[')[0]
                return ''
            else:
                # Simple if without otherwise (typically container/supporter content descriptors)
                if entity_id.startswith('d') or entity_id.startswith('c'):
                    if status == state_val:
                        return content
                return ''
        return ''
        
    cleaned = re.sub(r'\[if\s+([^\]]+)\](.*?)\[end if\]', replace_cond, desc, flags=re.DOTALL)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = re.sub(r'\n +', '\n', cleaned)
    cleaned = re.sub(r' +\n', '\n', cleaned)
    return cleaned.strip()

def map_action_template(action_name):
    # Mapping JSON action name to YAML action template id
    mapping = {
        'open/c': 'open_container',
        'close/c': 'close_container',
        'take/c': 'take_from_container',
        'insert': 'insert_into_container',
        'take/s': 'take_from_supporter',
        'put': 'put_on_supporter',
        'unlock/d': 'unlock_door',
        'lock/d': 'lock_door',
        'open/d': 'open_door',
        'close/d': 'close_door',
        'take': 'take',
        'drop': 'drop',
        'eat': 'eat',
    }
    if action_name in mapping:
        return mapping[action_name]
    if action_name.startswith('go/'):
        direction = action_name.split('/')[1]
        return f'go_{direction}'
    return action_name

def extract_action_arguments(action, template):
    args_dict = {}
    command_template = action.get('command_template', '') or ''
    placeholders = re.findall(r'\{([^}]+)\}', command_template)
    
    if template in ['open_container', 'close_container']:
        if placeholders:
            args_dict['container'] = placeholders[0]
    elif template in ['take_from_container', 'insert_into_container']:
        if len(placeholders) >= 2:
            args_dict['object'] = placeholders[0]
            args_dict['container'] = placeholders[1]
    elif template in ['take_from_supporter', 'put_on_supporter']:
        if len(placeholders) >= 2:
            args_dict['object'] = placeholders[0]
            args_dict['supporter'] = placeholders[1]
    elif template in ['unlock_door', 'lock_door']:
        if len(placeholders) >= 2:
            args_dict['door'] = placeholders[0]
            args_dict['key'] = placeholders[1]
    elif template in ['open_door', 'close_door']:
        if placeholders:
            args_dict['door'] = placeholders[0]
    elif template in ['take', 'drop']:
        if placeholders:
            args_dict['object'] = placeholders[0]
    elif template == 'eat':
        if placeholders:
            args_dict['food'] = placeholders[0]
    elif template.startswith('go_'):
        from_room = None
        for prec in action.get('preconditions', []):
            if prec.get('name') == 'at' and len(prec.get('arguments', [])) == 2:
                if prec['arguments'][0]['name'] == 'P':
                    from_room = prec['arguments'][1]['name']
                    break
        to_room = None
        for post in action.get('postconditions', []):
            if post.get('name') == 'at' and len(post.get('arguments', [])) == 2:
                if post['arguments'][0]['name'] == 'P':
                    to_room = post['arguments'][1]['name']
                    break
        args_dict['from'] = from_room
        args_dict['to'] = to_room
        
    return args_dict

def get_expected_effects(template, args_dict):
    if template == 'open_container':
        return [f"{args_dict.get('container')}.status = open"]
    elif template == 'close_container':
        return [f"{args_dict.get('container')}.status = closed"]
    elif template == 'take_from_container':
        return [f"{args_dict.get('object')}.location = inventory"]
    elif template == 'insert_into_container':
        return [f"{args_dict.get('object')}.location = {args_dict.get('container')}"]
    elif template == 'take_from_supporter':
        return [f"{args_dict.get('object')}.location = inventory"]
    elif template == 'put_on_supporter':
        return [f"{args_dict.get('object')}.location = {args_dict.get('supporter')}"]
    elif template == 'unlock_door':
        return [f"{args_dict.get('door')}.status = closed"]
    elif template == 'lock_door':
        return [f"{args_dict.get('door')}.status = locked"]
    elif template == 'open_door':
        return [f"{args_dict.get('door')}.status = open"]
    elif template == 'close_door':
        return [f"{args_dict.get('door')}.status = closed"]
    elif template == 'take':
        return [f"{args_dict.get('object')}.location = inventory"]
    elif template == 'drop':
        return [f"{args_dict.get('object')}.location = floor"]
    elif template == 'eat':
        return [f"{args_dict.get('food')}.status = eaten"]
    elif template.startswith('go_'):
        return [f"player.location = {args_dict.get('to')}"]
    return []

def convert_json_data_to_yaml_dict(json_data):
    """
    Parses the game JSON structure and constructs a dictionary conforming to the YAML schema.
    """
    # 1. Build lookup tables from entity infos
    entity_infos = {info[0]: info[1] for info in json_data.get('infos', [])}
    
    # 2. Process initial predicates from world state
    room_contents = {}
    container_contents = {}
    supporter_contents = {}
    door_states = {}
    container_states = {}
    edible_states = {}
    player_location = None
    player_inventory = []
    
    link_predicates = []
    direction_predicates = []
    free_predicates = []
    match_predicates = []
    
    # Parse predicates
    for pred in json_data.get('world', []):
        name = pred.get('name')
        args = pred.get('arguments', [])
        
        if name == 'at' and len(args) == 2:
            subj = args[0]['name']
            loc = args[1]['name']
            if subj == 'P':
                player_location = loc
            else:
                room_contents.setdefault(loc, []).append(subj)
                
        elif name == 'in' and len(args) == 2:
            obj = args[0]['name']
            container = args[1]['name']
            if container == 'I':
                player_inventory.append(obj)
            else:
                container_contents.setdefault(container, []).append(obj)
                
        elif name == 'on' and len(args) == 2:
            obj = args[0]['name']
            supporter = args[1]['name']
            supporter_contents.setdefault(supporter, []).append(obj)
            
        elif name in ['closed', 'open', 'locked'] and len(args) == 1:
            ent = args[0]['name']
            ent_type = entity_infos.get(ent, {}).get('type')
            if ent_type == 'd':
                door_states[ent] = name
            elif ent_type == 'c':
                container_states[ent] = name
                
        elif name == 'edible' and len(args) == 1:
            edible_states[args[0]['name']] = True
            
        elif name == 'link' and len(args) == 3:
            link_predicates.append(pred)
            
        elif name in ['north_of', 'south_of', 'east_of', 'west_of'] and len(args) == 2:
            direction_predicates.append(pred)
            
        elif name == 'free' and len(args) == 2:
            free_predicates.append(pred)
            
        elif name == 'match' and len(args) == 2:
            match_predicates.append(pred)

    # Resolve room directions
    # direction_map: (room1, room2) -> direction of room2 from room1
    direction_map = {}
    for pred in direction_predicates:
        r1 = pred['arguments'][0]['name']
        r2 = pred['arguments'][1]['name']
        d_name = pred['name']
        
        # E.g. north_of(r1, r2) means r1 is north of r2, so direction from r2 to r1 is north.
        if d_name == 'north_of':
            direction_map[(r2, r1)] = 'north'
            direction_map[(r1, r2)] = 'south'
        elif d_name == 'south_of':
            direction_map[(r2, r1)] = 'south'
            direction_map[(r1, r2)] = 'north'
        elif d_name == 'east_of':
            direction_map[(r2, r1)] = 'east'
            direction_map[(r1, r2)] = 'west'
        elif d_name == 'west_of':
            direction_map[(r2, r1)] = 'west'
            direction_map[(r1, r2)] = 'east'

    # Helper function to generate room exit and connection data
    # A link can exist via doors
    door_links = {}
    for link in link_predicates:
        r1 = link['arguments'][0]['name']
        door = link['arguments'][1]['name']
        r2 = link['arguments'][2]['name']
        door_links.setdefault(door, set()).add(r1)
        door_links.setdefault(door, set()).add(r2)

    # 3. METADATA
    metadata = {}
    json_meta = json_data.get('metadata', {})
    uuid = json_meta.get('uuid', '')
    
    metadata['id'] = uuid
    metadata['name'] = json_meta.get('desc', 'Simple game')
    metadata['game_type'] = "tw-simple"
    metadata['version'] = json_data.get('version', 1)
    
    # Seeds and config
    seeds = json_meta.get('seeds', {})
    metadata['generator'] = {
        'name': "TextWorld",
        'seeds': {
            'map': seeds.get('map'),
            'objects': seeds.get('objects'),
            'quest': seeds.get('quest'),
            'grammar': seeds.get('grammar')
        },
        'world_size': json_meta.get('world_size'),
        'quest_length': json_meta.get('quest_length')
    }
    
    # Configuration
    grammar_json = json_data.get('grammar', {})
    
    reward_type = "sparse"
    if 'rSparse' in uuid:
        reward_type = "sparse"
    elif 'rDense' in uuid:
        reward_type = "dense"
        
    goal_desc = "brief"
    if 'gBrief' in uuid:
        goal_desc = "brief"
    elif 'gDetailed' in uuid:
        goal_desc = "detailed"
        
    metadata['configuration'] = {
        'theme': grammar_json.get('theme', 'house'),
        'reward_type': reward_type,
        'goal_description': goal_desc,
        'grammar': {
            'include_adj': grammar_json.get('include_adj', False),
            'blend_descriptions': grammar_json.get('blend_descriptions', False),
            'ambiguous_instructions': grammar_json.get('ambiguous_instructions', False),
            'only_last_action': grammar_json.get('only_last_action', False),
            'blend_instructions': grammar_json.get('blend_instructions', False),
            'allowed_variables_numbering': grammar_json.get('allowed_variables_numbering', False),
            'unique_expansion': grammar_json.get('unique_expansion', False)
        }
    }

    # 4. OBJECTIVE
    objective_desc = json_data.get('objective', '')
    # Extract completion target (food item) and relation
    comp_cond = None
    target_food_name = "apple"  # default
    
    quests = json_data.get('quests', [])
    if quests and quests[0].get('win_events'):
        # Extract target state from last event trigger condition
        win_ev = quests[0]['win_events'][0]
        trigger_cond = win_ev.get('condition', {})
        preconds = trigger_cond.get('preconditions', [])
        
        for pre in preconds:
            if pre.get('name') in ['on', 'in'] and len(pre.get('arguments', [])) == 2:
                obj_id = pre['arguments'][0]['name']
                tgt_id = pre['arguments'][1]['name']
                obj_name = entity_infos.get(obj_id, {}).get('name')
                tgt_name = entity_infos.get(tgt_id, {}).get('name')
                
                target_food_name = obj_name or "apple"
                comp_cond = {
                    'object': obj_id,
                    'name': obj_name,
                    'relation': pre.get('name'),
                    'target': tgt_id,
                    'target_name': tgt_name
                }
                break

    objective = {
        'description': objective_desc,
        'reward': quests[0].get('reward', 1) if quests else 1,
        'completion': {
            'condition': comp_cond
        }
    }

    # 5. WORLD
    world = {}
    
    # Helper to construct entity dict
    def make_entity_dict(ent_id):
        info = entity_infos.get(ent_id, {})
        t_char = info.get('type')
        type_name = {
            'c': 'Container', 's': 'Supporter', 'd': 'Door',
            'f': 'Food', 'k': 'Key', 'o': 'Object'
        }.get(t_char, 'Object')
        
        ent = {
            'id': ent_id,
            'name': info.get('name'),
            'type': type_name
        }
        
        # Doors don't have description in the reference YAML
        if type_name != 'Door':
            desc_raw = info.get('desc', '')
            ent['description'] = clean_description_text(desc_raw, door_states, container_states)
            
        state = {}
        if type_name in ['Container', 'Door']:
            state['status'] = door_states.get(ent_id) or container_states.get(ent_id) or 'closed'
        if type_name == 'Food':
            state['edible'] = edible_states.get(ent_id, False)
        if type_name == 'Key':
            state['available'] = True
            
        if state:
            ent['state'] = state
            
        return ent

    # Player
    player_room_info = entity_infos.get(player_location, {})
    world['player'] = {
        'id': 'P',
        'name': 'player',
        'location': player_location,
        'location_name': player_room_info.get('name') if player_room_info else None,
        'inventory': [make_entity_dict(item) for item in player_inventory]
    }

    # Connections collection
    # Gather all connection pairs (A, B) where A < B
    connection_pairs = {} # (A, B) -> {'via': door_id, 'state': state_dict, 'direction': dir, 'rev_direction': rev_dir}
    
    # Add pairs from link (with doors)
    for link in link_predicates:
        r1 = link['arguments'][0]['name']
        door = link['arguments'][1]['name']
        r2 = link['arguments'][2]['name']
        
        from_r, to_r = (r1, r2) if r1 < r2 else (r2, r1)
        direction = direction_map.get((from_r, to_r))
        rev_direction = direction_map.get((to_r, from_r))
        
        door_status = door_states.get(door, 'closed')
        
        connection_pairs[(from_r, to_r)] = {
            'via': door,
            'state': {'status': door_status},
            'direction': direction,
            'reverse_direction': rev_direction
        }
        
    # Add pairs from free (without doors)
    for free in free_predicates:
        r1 = free['arguments'][0]['name']
        r2 = free['arguments'][1]['name']
        
        from_r, to_r = (r1, r2) if r1 < r2 else (r2, r1)
        if (from_r, to_r) not in connection_pairs:
            direction = direction_map.get((from_r, to_r))
            rev_direction = direction_map.get((to_r, from_r))
            
            connection_pairs[(from_r, to_r)] = {
                'via': None,
                'state': {'status': 'free'},
                'direction': direction,
                'reverse_direction': rev_direction
            }

    # Format connections list sorted by (from, to)
    connections_list = []
    sorted_pairs = sorted(connection_pairs.keys())
    for idx, (from_r, to_r) in enumerate(sorted_pairs):
        conn_info = connection_pairs[(from_r, to_r)]
        connections_list.append({
            'id': f"connection_{idx + 1}",
            'from': from_r,
            'to': to_r,
            'direction': conn_info['direction'],
            'reverse_direction': conn_info['reverse_direction'],
            'via': conn_info['via'],
            'state': conn_info['state']
        })

    # Location Exits Helper
    def get_room_exits(room_id):
        exits = []
        for (r1, r2), conn in connection_pairs.items():
            if room_id == r1:
                exits.append({
                    'direction': conn['direction'],
                    'to': r2,
                    'via': conn['via']
                })
            elif room_id == r2:
                exits.append({
                    'direction': conn['reverse_direction'],
                    'to': r1,
                    'via': conn['via']
                })
                
        # Sort exits by: has_door first, door_id, direction
        def exit_sort_key(ex):
            has_door = 0 if ex['via'] is not None else 1
            door_id = ex['via'] if ex['via'] is not None else ""
            direction = ex['direction']
            return (has_door, door_id, direction)
            
        return sorted(exits, key=exit_sort_key)

    # Locations
    locations_list = []
    room_ids = sorted([r_id for r_id, info in entity_infos.items() if info.get('type') == 'r'])
    
    for room_id in room_ids:
        room_info = entity_infos[room_id]
        
        # Room entities (excluding player P, keys matching nothing or stored elsewhere)
        ent_ids = room_contents.get(room_id, [])
        entities = []
        for ent_id in ent_ids:
            ent_dict = make_entity_dict(ent_id)
            
            # Sub-contents: contains
            if ent_dict['type'] == 'Container':
                sub_items = container_contents.get(ent_id, [])
                ent_dict['contains'] = [make_entity_dict(sub) for sub in sorted(sub_items)]
            # Sub-contents: supports
            elif ent_dict['type'] == 'Supporter':
                sub_items = supporter_contents.get(ent_id, [])
                ent_dict['supports'] = [make_entity_dict(sub) for sub in sorted(sub_items)]
                
            entities.append(ent_dict)
            
        # Add door entities that connect to this room
        room_doors = []
        for door_id, connected_rooms in door_links.items():
            if room_id in connected_rooms:
                room_doors.append(make_entity_dict(door_id))
                
        # Group room doors
        for d_dict in room_doors:
            # Add door connects field
            # find the other room
            door_id = d_dict['id']
            connected_rooms = list(door_links[door_id])
            if len(connected_rooms) == 2:
                other_room = connected_rooms[1] if connected_rooms[0] == room_id else connected_rooms[0]
                dir_to_other = direction_map.get((room_id, other_room))
                d_dict['connects'] = {
                    'to': other_room,
                    'direction': dir_to_other
                }
            entities.append(d_dict)

        # Sort entities by ID (or type then ID)
        # To match the bedroom exactly: c_0, c_1, s_0, d_0 (so room entities sorted by ID, then door entities sorted by ID)
        room_ents = sorted([e for e in entities if e['type'] != 'Door'], key=lambda x: x['id'])
        door_ents = sorted([e for e in entities if e['type'] == 'Door'], key=lambda x: x['id'])
        sorted_entities = room_ents + door_ents

        locations_list.append({
            'id': room_id,
            'name': room_info.get('name'),
            'type': 'Location',
            'room_type': room_info.get('room_type'),
            'description': clean_description_text(room_info.get('desc', '').split('\n\n')[0], door_states, container_states),
            'entities': sorted_entities,
            'exits': get_room_exits(room_id)
        })

    world['locations'] = locations_list
    world['connections'] = connections_list

    # Relations
    relations_list = []
    for match_pred in sorted(match_predicates, key=lambda x: x['arguments'][0]['name']):
        k_id = match_pred['arguments'][0]['name']
        t_id = match_pred['arguments'][1]['name']
        k_name = entity_infos.get(k_id, {}).get('name')
        t_name = entity_infos.get(t_id, {}).get('name')
        
        relations_list.append({
            'type': 'matches',
            'from': k_id,
            'to': t_id,
            'description': f"The {k_name} matches the {t_name}."
        })
    world['relations'] = relations_list
    
    # 6. ACTIONS
    # templates: placeholder to be replaced by formatted template block in post-processing
    actions = {
        'templates': [],
        'instances': [],
        'admissible': []
    }
    
    # Instances
    quest_actions = []
    if quests and quests[0].get('win_events'):
        quest_actions = quests[0]['win_events'][0].get('actions', [])
        quest_commands = quests[0].get('commands', [])
        
        for idx, act in enumerate(quest_actions):
            t_name = map_action_template(act['name'])
            cmd = quest_commands[idx] if idx < len(quest_commands) else ""
            args_dict = extract_action_arguments(act, t_name)
            
            actions['instances'].append({
                'id': f"a_{idx+1:03d}",
                'template': t_name,
                'command': cmd,
                'arguments': args_dict
            })

    # Admissible
    admissible_list = []
    # Always present
    admissible_list.append("look")
    admissible_list.append("inventory")
    
    # Open/close container actions
    open_close_actions = []
    take_from_actions = []
    examine_actions = []
    take_actions = []
    eat_actions = []
    go_actions = []
    
    # Exits from starting room
    start_exits = get_room_exits(player_location)
    for ex in start_exits:
        go_actions.append(f"go {ex['direction']}")
        
    # Entities in starting room
    start_ents = room_contents.get(player_location, [])
    for ent_id in start_ents:
        info = entity_infos.get(ent_id, {})
        name = info.get('name')
        t_char = info.get('type')
        
        if t_char == 'c':  # Container
            status = container_states.get(ent_id, 'closed')
            if status == 'closed':
                open_close_actions.append(f"open {name}")
            else:
                open_close_actions.append(f"close {name}")
                sub_items = container_contents.get(ent_id, [])
                for sub in sub_items:
                    sub_name = entity_infos.get(sub, {}).get('name')
                    take_from_actions.append(f"take {sub_name} from {name}")
            examine_actions.append(f"examine {name}")
            
        elif t_char == 's':  # Supporter
            sub_items = supporter_contents.get(ent_id, [])
            for sub in sub_items:
                sub_name = entity_infos.get(sub, {}).get('name')
                take_from_actions.append(f"take {sub_name} from {name}")
            examine_actions.append(f"examine {name}")
            
        elif t_char in ['o', 'f', 'k']:  # Portable item
            examine_actions.append(f"examine {name}")
            take_actions.append(f"take {name}")
            if t_char == 'f':
                eat_actions.append(f"eat {name}")

    # Combine in the specific order to match simple_game.yaml
    admissible_list.extend(sorted(open_close_actions))
    admissible_list.extend(sorted(take_from_actions))
    admissible_list.extend(sorted(examine_actions))
    admissible_list.extend(sorted(take_actions))
    admissible_list.extend(sorted(eat_actions))
    admissible_list.extend(sorted(go_actions))
    
    actions['admissible'] = admissible_list

    # 7. QUESTS
    quests_list = []
    if quests:
        q_json = quests[0]
        quest_dict = {
            'id': 'main_quest',
            'name': f"Prepare grilled {target_food_name}",
            'description': f"Prepare the grilled {target_food_name} required by the game objective.",
            'reward': q_json.get('reward', 1),
            'optional': q_json.get('optional', False),
            'repeatable': q_json.get('repeatable', False)
        }
        
        # Steps
        steps_list = []
        for idx, act in enumerate(quest_actions):
            t_name = map_action_template(act['name'])
            cmd = quest_commands[idx] if idx < len(quest_commands) else ""
            args_dict = extract_action_arguments(act, t_name)
            effects = get_expected_effects(t_name, args_dict)
            
            steps_list.append({
                'sequence': idx + 1,
                'action': t_name,
                'arguments': args_dict,
                'command': cmd,
                'expected_effects': effects
            })
            
        quest_dict['steps'] = steps_list
        
        # Completion
        comp_str = f"{target_food_name} is on stove"  # Simple mapping for goal text
        if comp_cond:
            comp_str = f"{comp_cond['name']} is {comp_cond['relation']} {comp_cond['target_name']}"
            
        quest_dict['completion'] = {
            'conditions': [comp_str]
        }
        
        # Fail conditions
        fail_conditions = []
        first_quest_fail_events = q_json.get('fail_events', [])
        for fail_event in first_quest_fail_events:
            condition_predicates = fail_event.get('condition', {}).get('preconditions', [])
            for pred in condition_predicates:
                if pred.get('name') == 'eaten' and len(pred.get('arguments', [])) == 1:
                    obj_id = pred['arguments'][0]['name']
                    obj_info = entity_infos.get(obj_id, {})
                    obj_name = obj_info.get('name', obj_id)
                    
                    fail_conditions.append({
                        'id': f"eat_{obj_name}",
                        'condition': {
                            'action': 'eat',
                            'object': obj_id
                        },
                        'effect': {
                            'result': 'failure'
                        }
                    })
        quest_dict['fail_conditions'] = fail_conditions
        quests_list.append(quest_dict)

    # 8. OBSERVATION
    observation_room_info = entity_infos.get(player_location, {})
    obs_text_raw = observation_room_info.get('desc', '')
    cleaned_obs_text = clean_description_text(obs_text_raw, door_states, container_states)
    
    # Visible entities: sorted starting room items + start door items
    vis_ents = []
    for ent_id in start_ents:
        vis_ents.append({
            'id': ent_id,
            'name': entity_infos.get(ent_id, {}).get('name')
        })
    # start door items
    for door_id, connected_rooms in door_links.items():
        if player_location in connected_rooms:
            vis_ents.append({
                'id': door_id,
                'name': entity_infos.get(door_id, {}).get('name')
            })
            
    # Sort room entities by ID, door entities by ID, then combine
    room_vis = sorted([e for e in vis_ents if not e['id'].startswith('d')], key=lambda x: x['id'])
    door_vis = sorted([e for e in vis_ents if e['id'].startswith('d')], key=lambda x: x['id'])
    sorted_vis_ents = room_vis + door_vis

    # Exits of player room
    obs_exits = []
    for ex in start_exits:
        exit_dict = {
            'direction': ex['direction'],
            'to': ex['to']
        }
        if ex['via']:
            exit_dict['via'] = ex['via']
            door_status = door_states.get(ex['via'], 'closed')
            exit_dict['state'] = {'status': door_status}
        obs_exits.append(exit_dict)

    observation = {
        'location': {
            'id': player_location,
            'name': player_room_info.get('name') if player_room_info else None
        },
        'text': cleaned_obs_text,
        'visible_entities': sorted_vis_ents,
        'exits': obs_exits,
        'last_action': {
            'command': None,
            'template': None
        },
        'last_feedback': None
    }

    # Final Output Dictionary
    output_dict = {
        'game': {
            'metadata': metadata,
            'objective': objective,
            'world': world,
            'actions': actions,
            'quests': quests_list,
            'observation': observation
        }
    }
    
    # Build a mapping of room id -> room name for formatting banners
    room_name_map = {r_id: entity_infos[r_id].get('name', 'ROOM') for r_id in room_ids}
    
    return output_dict, room_name_map
