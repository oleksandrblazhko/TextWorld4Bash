import yaml
import re

class FoldedString(str):
    pass

class QuotedString(str):
    pass

class CustomDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(CustomDumper, self).increase_indent(flow, False)

    def represent_mapping(self, tag, mapping, flow_style=None):
        value = []
        node = yaml.nodes.MappingNode(tag, value, flow_style=flow_style)
        if self.alias_key is not None:
            self.represented_objects[self.alias_key] = node
        best_style = True
        if hasattr(mapping, 'items'):
            mapping = list(mapping.items())
        for item_key, item_value in mapping:
            node_key = self.represent_data(item_key)
            node_value = self.represent_data(item_value)
            if not (isinstance(node_key, yaml.nodes.ScalarNode) and not node_key.style):
                best_style = False
            if not (isinstance(node_value, yaml.nodes.ScalarNode) and not node_value.style):
                best_style = False
            value.append((node_key, node_value))
        if flow_style is None:
            if self.default_flow_style is not None:
                node.flow_style = self.default_flow_style
            else:
                node.flow_style = best_style
        return node

def folded_string_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='>')

def quoted_string_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

# Add representers to CustomDumper
CustomDumper.add_representer(FoldedString, folded_string_representer)
CustomDumper.add_representer(QuotedString, quoted_string_representer)

def wrap_data_strings(data, parent_key=None):
    """
    Recursively wrap strings in QuotedString or FoldedString based on their type,
    length, and key context to ensure correct YAML styling (quoted vs folded block).
    """
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            new_dict[k] = wrap_data_strings(v, parent_key=k)
        return new_dict
    elif isinstance(data, list):
        return [wrap_data_strings(item, parent_key=parent_key) for item in data]
    elif isinstance(data, str):
        # We always want double quotes (no folding) for specific technical fields
        always_quoted_keys = {
            'id', 'to', 'from', 'via', 'direction', 'reverse_direction', 
            'action', 'template', 'relation', 'target', 'game_type'
        }
        if parent_key in always_quoted_keys:
            return QuotedString(data)
        
        # If it contains newline or is longer than 40 characters, represent as folded
        if '\n' in data or len(data) > 40:
            # Normalize newlines
            return FoldedString(data.strip())
        return QuotedString(data)
    else:
        return data

# Static template string matching simple_game.yaml exactly
STATIC_TEMPLATES_STR = """    templates:


      # --------------------------------------------------------
      # INFORMATION
      # --------------------------------------------------------

      - id: "look"

        name: "look"

        command: "look"

        targets: []

        preconditions: []

        effects: []


      - id: "inventory"

        name: "inventory"

        command: "inventory"

        targets: []

        preconditions: []

        effects: []


      # --------------------------------------------------------
      # MOVEMENT
      # --------------------------------------------------------

      - id: "go_north"

        name: "go north"

        command: "go north"

        targets: []

        preconditions:
          - "player_has_north_exit"
          - "destination_is_free"

        effects:
          - "player_location_changed"


      - id: "go_south"

        name: "go south"

        command: "go south"

        targets: []

        preconditions:
          - "player_has_south_exit"
          - "destination_is_free"

        effects:
          - "player_location_changed"


      - id: "go_east"

        name: "go east"

        command: "go east"

        targets: []

        preconditions:
          - "player_has_east_exit"
          - "destination_is_free"

        effects:
          - "player_location_changed"


      - id: "go_west"

        name: "go west"

        command: "go west"

        targets: []

        preconditions:
          - "player_has_west_exit"
          - "destination_is_free"

        effects:
          - "player_location_changed"


      # --------------------------------------------------------
      # OBJECT EXAMINATION
      # --------------------------------------------------------

      - id: "examine"

        name: "examine"

        command: "examine {object}"

        targets:
          object:
            type: "Thing"

        preconditions:
          - "object_accessible"

        effects: []


      # --------------------------------------------------------
      # CONTAINERS
      # --------------------------------------------------------

      - id: "open_container"

        name: "open"

        command: "open {container}"

        targets:
          container:
            type: "Container"

        preconditions:
          - "container_accessible"
          - "container_closed"

        effects:
          - "container_open"


      - id: "close_container"

        name: "close"

        command: "close {container}"

        targets:
          container:
            type: "Container"

        preconditions:
          - "container_accessible"
          - "container_open"

        effects:
          - "container_closed"


      - id: "take_from_container"

        name: "take from container"

        command: "take {object} from {container}"

        targets:
          object:
            type: "Thing"

          container:
            type: "Container"

        preconditions:
          - "container_accessible"
          - "container_open"
          - "object_in_container"

        effects:
          - "object_in_inventory"


      - id: "insert_into_container"

        name: "insert"

        command: "insert {object} into {container}"

        targets:
          object:
            type: "Thing"

          container:
            type: "Container"

        preconditions:
          - "object_in_inventory"
          - "container_accessible"
          - "container_open"

        effects:
          - "object_in_container"


      # --------------------------------------------------------
      # SUPPORTERS
      # --------------------------------------------------------

      - id: "take_from_supporter"

        name: "take from supporter"

        command: "take {object} from {supporter}"

        targets:
          object:
            type: "Thing"

          supporter:
            type: "Supporter"

        preconditions:
          - "supporter_accessible"
          - "object_on_supporter"

        effects:
          - "object_in_inventory"


      - id: "put_on_supporter"

        name: "put"

        command: "put {object} on {supporter}"

        targets:
          object:
            type: "Thing"

          supporter:
            type: "Supporter"

        preconditions:
          - "object_in_inventory"
          - "supporter_accessible"

        effects:
          - "object_on_supporter"


      # --------------------------------------------------------
      # DOORS AND LOCKS
      # --------------------------------------------------------

      - id: "unlock_door"

        name: "unlock"

        command: "unlock {door} with {key}"

        targets:
          door:
            type: "Door"

          key:
            type: "Key"

        preconditions:
          - "door_accessible"
          - "door_locked"
          - "key_in_inventory"
          - "key_matches_door"

        effects:
          - "door_closed"


      - id: "lock_door"

        name: "lock"

        command: "lock {door} with {key}"

        targets:
          door:
            type: "Door"

          key:
            type: "Key"

        preconditions:
          - "door_accessible"
          - "door_closed"
          - "key_in_inventory"
          - "key_matches_door"

        effects:
          - "door_locked"


      - id: "open_door"

        name: "open"

        command: "open {door}"

        targets:
          door:
            type: "Door"

        preconditions:
          - "door_accessible"
          - "door_closed"
          - "door_unlocked"

        effects:
          - "door_open"


      - id: "close_door"

        name: "close"

        command: "close {door}"

        targets:
          door:
            type: "Door"

        preconditions:
          - "door_accessible"
          - "door_open"

        effects:
          - "door_closed"


      # --------------------------------------------------------
      # GENERAL OBJECT ACTIONS
      # --------------------------------------------------------

      - id: "take"

        name: "take"

        command: "take {object}"

        targets:
          object:
            type: "Thing"

        preconditions:
          - "object_accessible"
          - "object_on_floor"

        effects:
          - "object_in_inventory"


      - id: "drop"

        name: "drop"

        command: "drop {object}"

        targets:
          object:
            type: "Thing"

        preconditions:
          - "object_in_inventory"

        effects:
          - "object_on_floor"


      - id: "eat"

        name: "eat"

        command: "eat {food}"

        targets:
          food:
            type: "Food"

        preconditions:
          - "food_accessible"
          - "food_edible"

        effects:
          - "food_eaten\""""

def post_process_yaml(yaml_str, room_name_map):
    """
    Format and clean up the generated YAML string, adding header comments,
    sub-headers, correct indentation, and extra spacing to match simple_game.yaml.
    """
    # 1. Add headers
    yaml_str = yaml_str.replace('  metadata:', '\\n  # ============================================================\\n  # 1. METADATA\\n  # ============================================================\\n\\n  metadata:')
    yaml_str = yaml_str.replace('  objective:', '\\n  # ============================================================\\n  # 2. OBJECTIVE\\n  # ============================================================\\n\\n  objective:')
    yaml_str = yaml_str.replace('  world:', '\\n  # ============================================================\\n  # 3. WORLD\\n  # ============================================================\\n\\n  world:')
    yaml_str = yaml_str.replace('    player:', '\\n    # ----------------------------------------------------------\\n    # 3.1 PLAYER\\n    # ----------------------------------------------------------\\n\\n    player:')
    yaml_str = yaml_str.replace('    locations:', '\\n    # ----------------------------------------------------------\\n    # 3.2 LOCATIONS\\n    # ----------------------------------------------------------\\n\\n    locations:')
    yaml_str = yaml_str.replace('    connections:', '\\n    # ----------------------------------------------------------\\n    # 3.3 CONNECTIONS\\n    # ----------------------------------------------------------\\n\\n    connections:')
    yaml_str = yaml_str.replace('    relations:', '\\n    # ----------------------------------------------------------\\n    # 3.4 SEMANTIC RELATIONS\\n    # ----------------------------------------------------------\\n\\n    relations:')
    yaml_str = yaml_str.replace('  actions:', '\\n  # ============================================================\\n  # 4. ACTIONS\\n  # ============================================================\\n\\n  actions:')
    yaml_str = yaml_str.replace('    instances:', '\\n    # ----------------------------------------------------------\\n    # 4.2 CONCRETE ACTION INSTANCES\\n    # ----------------------------------------------------------\\n\\n    instances:')
    yaml_str = yaml_str.replace('    admissible:', '\\n    # ----------------------------------------------------------\\n    # 4.3 ADMISSIBLE ACTIONS — INITIAL STATE\\n    # ----------------------------------------------------------\\n\\n    admissible:')
    yaml_str = yaml_str.replace('  quests:', '\\n  # ============================================================\\n  # 5. QUEST\\n  # ============================================================\\n\\n  quests:')
    yaml_str = yaml_str.replace('  observation:', '\\n  # ============================================================\\n  # 6. OBSERVATION\\n  # ============================================================\\n\\n  observation:')

    # Hack to un-escape replaced newlines if we used double slashes in string literal
    yaml_str = yaml_str.replace('\\n', '\n')

    # 2. Replace templates placeholder
    yaml_str = yaml_str.replace('    templates: []', STATIC_TEMPLATES_STR)

    # 3. Format room blocks under locations
    # Replace "- id: \"r_X\"" with a nice uppercase room name banner
    def replace_room_banner(match):
        room_id = match.group(1)
        if room_id not in room_name_map:
            return match.group(0)
        room_name = room_name_map[room_id].upper()
        banner = f"\\n\\n      # ========================================================\\n"
        banner += f"      # {room_id} — {room_name}\\n"
        banner += f"      # ========================================================\\n\\n"
        banner += f"      - id: \"{room_id}\""
        banner = banner.replace('\\n', '\n')
        return banner

    yaml_str = re.sub(r'(?m)^      - id: "([^"]+)"', replace_room_banner, yaml_str)

    # 4. Spacing adjustment: Replace folded chomp indicators ": >-" with ": >"
    yaml_str = yaml_str.replace(': >-\n', ': >\n')

    # 5. Add space between elements in list sequences for readability
    yaml_str = yaml_str.replace('\n      - id: ', '\n\n      - id: ')
    yaml_str = yaml_str.replace('\n      - direction: ', '\n\n      - direction: ')
    yaml_str = yaml_str.replace('\n      - type: ', '\n\n      - type: ')
    yaml_str = yaml_str.replace('\n        - sequence: ', '\n\n        - sequence: ')
    yaml_str = yaml_str.replace('\n    - id: ', '\n\n    - id: ')
    
    # 6. Fix double spaces and clean up
    yaml_str = re.sub(r'\n{3,}', '\n\n', yaml_str)
    
    # 7. Append KB comment
    kb_comment = """
# ============================================================
# 7. KNOWLEDGE BASE
# ============================================================

# Note: The Knowledge Base (KB) section contains highly technical game logic
# and grammar paths that are typically machine-generated and not intended
# for direct human editing in this YAML template.
# Its detailed structure is omitted here to simplify human perception.
"""
    yaml_str = yaml_str.strip() + "\\n" + kb_comment
    yaml_str = yaml_str.replace('\\n', '\n')
    return yaml_str

def format_yaml(data, room_name_map):
    wrapped_data = wrap_data_strings(data)
    yaml_str = yaml.dump(wrapped_data, Dumper=CustomDumper, indent=2, allow_unicode=True, width=1000)
    return post_process_yaml(yaml_str, room_name_map)
