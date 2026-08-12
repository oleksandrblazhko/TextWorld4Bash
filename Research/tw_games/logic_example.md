# supporter
type s : t {
    predicates {
        on(o, s);
    }

    inform7 {
        type {
            kind :: "supporter";
            definition :: "supporters are fixed in place.";
        }

        predicates {
            on(o, s) :: "The {o} is on the {s}";
        }
    }
}


# object
type o : t {
    constraints {
        obj1 :: in(o, I) & in(o, c) -> fail();
        obj2 :: in(o, I) & on(o, s) -> fail();
        obj3 :: in(o, I) & at(o, r) -> fail();
        obj4 :: in(o, c) & on(o, s) -> fail();
        obj5 :: in(o, c) & at(o, r) -> fail();
        obj6 :: on(o, s) & at(o, r) -> fail();
        obj7 :: at(o, r) & at(o, r') -> fail();
        obj8 :: in(o, c) & in(o, c') -> fail();
        obj9 :: on(o, s) & on(o, s') -> fail();
    }

    inform7 {
        type {
            kind :: "object-like";
            definition :: "object-like is portable.";
        }
    }
}


# food
type f : o {
    predicates {
        edible(f);
        eaten(f);
    }

    rules {
        eat :: in(f, I) -> eaten(f);
    }

    constraints {
        eaten1 :: eaten(f) & in(f, I) -> fail();
        eaten2 :: eaten(f) & in(f, c) -> fail();
        eaten3 :: eaten(f) & on(f, s) -> fail();
        eaten4 :: eaten(f) & at(f, r) -> fail();
    }

    inform7 {
        type {
            kind :: "food";
            definition :: "food is edible.";
        }

        predicates {
            edible(f) :: "The {f} is edible";
            eaten(f) :: "The {f} is nowhere";
        }

        commands {
            eat :: "eat {f}" :: "eating the {f}";
        }
    }
}


# door
type d : t {
    predicates {
        open(d);
        closed(d);
        locked(d);

        link(r, d, r);
    }

    rules {
        lock/d   :: $at(P, r) & $link(r, d, r') & $link(r', d, r)
                  & $in(k, I) & $match(k, d) & closed(d)
                  -> locked(d);

        unlock/d :: $at(P, r) & $link(r, d, r') & $link(r', d, r)
                  & $in(k, I) & $match(k, d) & locked(d)
                  -> closed(d);

        open/d   :: $at(P, r) & $link(r, d, r') & $link(r', d, r)
                  & closed(d)
                  -> open(d) & free(r, r') & free(r', r);

        close/d  :: $at(P, r) & $link(r, d, r') & $link(r', d, r)
                  & open(d) & free(r, r') & free(r', r)
                  -> closed(d);

        examine/d :: at(P, r) & $link(r, d, r')
                  -> at(P, r);
    }

    reverse_rules {
        lock/d :: unlock/d;
        open/d :: close/d;

        examine/d :: examine/d;
    }

    constraints {
        d1 :: open(d) & closed(d) -> fail();
        d2 :: open(d) & locked(d) -> fail();
        d3 :: closed(d) & locked(d) -> fail();

        # A door can't be used to link more than two rooms.
        link1 :: link(r, d, r') & link(r, d, r'') -> fail();
        link2 :: link(r, d, r') & link(r'', d, r''') -> fail();

        # There's already a door linking two rooms.
        link3 :: link(r, d, r') & link(r, d', r') -> fail();

        # There cannot be more than four doors in a room.
        too_many_doors ::
            link(r, d1: d, r1: r)
            & link(r, d2: d, r2: r)
            & link(r, d3: d, r3: r)
            & link(r, d4: d, r4: r)
            & link(r, d5: d, r5: r)
            -> fail();

        # There cannot be more than four doors in a room.
        dr1 ::
            free(r, r1: r)
            & link(r, d2: d, r2: r)
            & link(r, d3: d, r3: r)
            & link(r, d4: d, r4: r)
            & link(r, d5: d, r5: r)
            -> fail();

        dr2 ::
            free(r, r1: r)
            & free(r, r2: r)
            & link(r, d3: d, r3: r)
            & link(r, d4: d, r4: r)
            & link(r, d5: d, r5: r)
            -> fail();

        dr3 ::
            free(r, r1: r)
            & free(r, r2: r)
            & free(r, r3: r)
            & link(r, d4: d, r4: r)
            & link(r, d5: d, r5: r)
            -> fail();

        dr4 ::
            free(r, r1: r)
            & free(r, r2: r)
            & free(r, r3: r)
            & free(r, r4: r)
            & link(r, d5: d, r5: r)
            -> fail();

        free1 ::
            link(r, d, r') & free(r, r') & closed(d)
            -> fail();

        free2 ::
            link(r, d, r') & free(r, r') & locked(d)
            -> fail();
    }

    inform7 {
        type {
            kind :: "door";
            definition :: "door is openable and lockable.";
        }

        predicates {
            open(d) :: "The {d} is open";
            closed(d) :: "The {d} is closed";
            locked(d) :: "The {d} is locked";

            link(r, d, r') :: "";
            # No equivalent in Inform7.
        }

        commands {
            open/d ::
                "open {d}" ::
                "opening {d}";

            close/d ::
                "close {d}" ::
                "closing {d}";

            unlock/d ::
                "unlock {d} with {k}" ::
                "unlocking {d} with the {k}";

            lock/d ::
                "lock {d} with {k}" ::
                "locking {d} with the {k}";

            examine/d ::
                "examine {d}" ::
                "examining {d}";
        }
    }
}


# Player
type P {
    rules {
        look :: at(P, r) -> at(P, r);
        # Nothing changes.
    }

    reverse_rules {
        look :: look;
    }

    inform7 {
        commands {
            look :: "look" :: "looking";
        }
    }
}


# room
type r {
    predicates {
        at(P, r);
        at(t, r);

        north_of(r, r);
        west_of(r, r);

        north_of/d(r, d, r);
        west_of/d(r, d, r);

        free(r, r);

        south_of(r, r') = north_of(r', r);
        east_of(r, r') = west_of(r', r);

        south_of/d(r, d, r') = north_of/d(r', d, r);
        east_of/d(r, d, r') = west_of/d(r', d, r);
    }

    rules {
        go/north ::
            at(P, r)
            & $north_of(r', r)
            & $free(r, r')
            & $free(r', r)
            -> at(P, r');

        go/south ::
            at(P, r)
            & $south_of(r', r)
            & $free(r, r')
            & $free(r', r)
            -> at(P, r');

        go/east ::
            at(P, r)
            & $east_of(r', r)
            & $free(r, r')
            & $free(r', r)
            -> at(P, r');

        go/west ::
            at(P, r)
            & $west_of(r', r)
            & $free(r, r')
            & $free(r', r)
            -> at(P, r');
    }

    reverse_rules {
        go/north :: go/south;
        go/west :: go/east;
    }

    constraints {
        r1 :: at(P, r) & at(P, r') -> fail();
        r2 :: at(s, r) & at(s, r') -> fail();
        r3 :: at(c, r) & at(c, r') -> fail();

        # An exit direction can only lead to one room.
        nav_rr1 ::
            north_of(r, r') & north_of(r'', r')
            -> fail();

        nav_rr2 ::
            south_of(r, r') & south_of(r'', r')
            -> fail();

        nav_rr3 ::
            east_of(r, r') & east_of(r'', r')
            -> fail();

        nav_rr4 ::
            west_of(r, r') & west_of(r'', r')
            -> fail();

        # Two rooms can only be connected once with each other.
        nav_rrA ::
            north_of(r, r') & south_of(r', r)
            -> fail();

        nav_rrB ::
            north_of(r, r') & west_of(r', r)
            -> fail();

        nav_rrC ::
            north_of(r, r') & east_of(r', r)
            -> fail();

        nav_rrD ::
            south_of(r, r') & west_of(r', r)
            -> fail();

        nav_rrE ::
            south_of(r, r') & east_of(r', r)
            -> fail();

        nav_rrF ::
            west_of(r, r') & east_of(r', r)
            -> fail();
    }

    inform7 {
        type {
            kind :: "room";
        }

        predicates {
            at(P, r) ::
                "The player is in {r}";

            at(t, r) ::
                "The {t} is in {r}";

            free(r, r') ::
                "";
            # No equivalent in Inform7.

            north_of(r, r') ::
                "The {r} is mapped north of {r'}";

            south_of(r, r') ::
                "The {r} is mapped south of {r'}";

            east_of(r, r') ::
                "The {r} is mapped east of {r'}";

            west_of(r, r') ::
                "The {r} is mapped west of {r'}";

            north_of/d(r, d, r') ::
                "South of {r} and north of {r'} is a door called {d}";

            south_of/d(r, d, r') ::
                "North of {r} and south of {r'} is a door called {d}";

            east_of/d(r, d, r') ::
                "West of {r} and east of {r'} is a door called {d}";

            west_of/d(r, d, r') ::
                "East of {r} and west of {r'} is a door called {d}";
        }

        commands {
            go/north ::
                "go north" ::
                "going north";

            go/south ::
                "go south" ::
                "going south";

            go/east ::
                "go east" ::
                "going east";

            go/west ::
                "go west" ::
                "going west";
        }
    }
}


# thing
type t {
    rules {
        examine/t ::
            at(P, r) & $at(t, r)
            -> at(P, r);
    }

    reverse_rules {
        examine/t :: examine/t;
    }

    inform7 {
        type {
            kind :: "thing";
        }

        commands {
            examine/t ::
                "examine {t}" ::
                "examining the {t}";
        }
    }
}


# container
type c : t {
    predicates {
        open(c);
        closed(c);
        locked(c);

        in(o, c);
    }

    rules {
        lock/c ::
            $at(P, r)
            & $at(c, r)
            & $in(k, I)
            & $match(k, c)
            & closed(c)
            -> locked(c);

        unlock/c ::
            $at(P, r)
            & $at(c, r)
            & $in(k, I)
            & $match(k, c)
            & locked(c)
            -> closed(c);

        open/c ::
            $at(P, r)
            & $at(c, r)
            & closed(c)
            -> open(c);

        close/c ::
            $at(P, r)
            & $at(c, r)
            & open(c)
            -> closed(c);
    }

    reverse_rules {
        lock/c :: unlock/c;
        open/c :: close/c;
    }

    constraints {
        c1 :: open(c) & closed(c) -> fail();
        c2 :: open(c) & locked(c) -> fail();
        c3 :: closed(c) & locked(c) -> fail();
    }

    inform7 {
        type {
            kind :: "container";

            definition ::
                "containers are openable, lockable and fixed in place. containers are usually closed.";
        }

        predicates {
            open(c) ::
                "The {c} is open";

            closed(c) ::
                "The {c} is closed";

            locked(c) ::
                "The {c} is locked";

            in(o, c) ::
                "The {o} is in the {c}";
        }

        commands {
            open/c ::
                "open {c}" ::
                "opening the {c}";

            close/c ::
                "close {c}" ::
                "closing the {c}";

            lock/c ::
                "lock {c} with {k}" ::
                "locking the {c} with the {k}";

            unlock/c ::
                "unlock {c} with {k}" ::
                "unlocking the {c} with the {k}";
        }
    }
}


# key
type k : o {
    predicates {
        match(k, c);
        match(k, d);
    }

    constraints {
        k1 ::
            match(k, c) & match(k', c)
            -> fail();

        k2 ::
            match(k, c) & match(k, c')
            -> fail();

        k3 ::
            match(k, d) & match(k', d)
            -> fail();

        k4 ::
            match(k, d) & match(k, d')
            -> fail();
    }

    inform7 {
        type {
            kind :: "key";
        }

        predicates {
            match(k, c) ::
                "The matching key of the {c} is the {k}";

            match(k, d) ::
                "The matching key of the {d} is the {k}";
        }
    }
}


# Inventory
type I {
    predicates {
        in(o, I);
    }

    rules {
        inventory ::
            at(P, r)
            -> at(P, r);
        # Nothing changes.

        take ::
            $at(P, r) & at(o, r)
            -> in(o, I);

        drop ::
            $at(P, r) & in(o, I)
            -> at(o, r);

        take/c ::
            $at(P, r)
            & $at(c, r)
            & $open(c)
            & in(o, c)
            -> in(o, I);

        insert ::
            $at(P, r)
            & $at(c, r)
            & $open(c)
            & in(o, I)
            -> in(o, c);

        take/s ::
            $at(P, r)
            & $at(s, r)
            & on(o, s)
            -> in(o, I);

        put ::
            $at(P, r)
            & $at(s, r)
            & in(o, I)
            -> on(o, s);

        examine/I ::
            in(o, I)
            -> in(o, I);
        # Nothing changes.

        examine/s ::
            at(P, r)
            & $at(s, r)
            & $on(o, s)
            -> at(P, r);
        # Nothing changes.

        examine/c ::
            at(P, r)
            & $at(c, r)
            & $open(c)
            & $in(o, c)
            -> at(P, r);
        # Nothing changes.
    }

    reverse_rules {
        inventory :: inventory;

        take :: drop;
        take/c :: insert;
        take/s :: put;

        examine/I :: examine/I;
        examine/s :: examine/s;
        examine/c :: examine/c;
    }

    inform7 {
        predicates {
            in(o, I) ::
                "The player carries the {o}";
        }

        commands {
            take ::
                "take {o}" ::
                "taking the {o}";

            drop ::
                "drop {o}" ::
                "dropping the {o}";

            take/c ::
                "take {o} from {c}" ::
                "removing the {o} from the {c}";

            insert ::
                "insert {o} into {c}" ::
                "inserting the {o} into the {c}";

            take/s ::
                "take {o} from {s}" ::
                "removing the {o} from the {s}";

            put ::
                "put {o} on {s}" ::
                "putting the {o} on the {s}";

            inventory ::
                "inventory" ::
                "taking inventory";

            examine/I ::
                "examine {o}" ::
                "examining the {o}";

            examine/s ::
                "examine {o}" ::
                "examining the {o}";

            examine/c ::
                "examine {o}" ::
                "examining the {o}";
        }
    }
}


# look
type ? {
    rules {
        look ::
            at(P, r)
            -> at(P, r);
        # Nothing changes.
    }

    reverse_rules {
        look :: look;
    }

    inform7 {
        commands {
            look ::
                "look" ::
                "looking";
        }
    }
}