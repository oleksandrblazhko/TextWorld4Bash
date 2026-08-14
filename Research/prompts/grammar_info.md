# Опис елементів файлу textworld\generator\data\text_grammars\house_instruction.twg

| назва елементу | призначення елементу | приклад значень |
| :--- | :--- | :--- |
| obj_types | Типи об'єктів, які можна використовувати в інструкціях (o: object, k: key, f: food) | (o|k|f) |
| obj_types_no_key | Типи об'єктів без ключа | (o|f) |
| on_types | Типи поверхонь (c: container, s: supporter) | (c|s) |
| lock_types | Типи об'єктів, що замикаються (c: container, d: door) | (c|d) |
| eat_types | Типи об'єктів, які можна їсти (f: food) | (f) |
| close_open_types | Типи об'єктів, які можна відкривати/закривати (d: door, c: container) | (d|c) |
| lock_type_var | Варіації для фраз з об'єктами, що замикаються | #lock_types#;#lock_types# #in_the_(r)# |
| (s)_var | Варіації для фраз з поверхнями | (s);(s) #in_the_(r)# |
| (c)_var | Варіації для фраз з контейнерами | (c);(c) #in_the_(r)# |
| on_var | Варіації для фраз з поверхнями | #on_types#;#on_types# #in_the_(r)# |
| in_the_(r) | Синоніми для "в кімнаті" | in the (r);within the (r);inside the (r) |
| make_syn_u | Синоніми для "Make sure" (з великої літери) | Make sure;Assure;Make it so;Doublecheck;Look and see;Make absolutely sure |
| make_syn_v | Синоніми для "make sure" (з маленької літери) | make sure;assure;make it so;doublecheck;look and see;make absolutely sure |
| by_the_syn | Синоніми для "with the" | with the |
| init_syn | Синоніми для "in it" | in it;inside;placed inside |
| into_syn | Синоніми для "into" | into;inside |
| look | Команда "дивитись" | look around in (r). |
| examine | Команда "оглянути" | examine (o|k|f|d|c|s|t). |
| inventory | Команда "інвентар" | examine your inventory. |
| take | Команда "взяти" | #take_synonym_1# the #obj_types# in the (r).;#take_synonym_1# the #obj_types# from the (r).;#take_synonym_1# the #obj_types# that's in the (r). |
| take_synonym_1 | Синоніми для "take" | take;retrieve;recover;pick up |
| take/s | Взяти з поверхні | #take_synonym_1# the #obj_types# from the #on_var#. |
| take/c | Взяти з контейнера | #take_synonym_1# the #obj_types# from the #on_var#. |
| pick-up_synonym_1 | Синоніми для "pick-up" | pick-up;retrieve;recover;pick up;lift |
| pick-up_synonym_v | Синоніми для "Pick-up" (з великої літери) | Pick-up;Retrieve;Recover;Pick up;Lift |
| insert | Команда "вставити" | #insert_syn_1# the #obj_types# #into_syn# the #(c)_var#.;you can #insert_syn_1# the #obj_types# #into_syn# the #(c)_var#. |
| insert_syn_u | Синоніми для "Insert" (з великої літери) | Insert;Put;Place;Deposit |
| insert_syn_1 | Синоніми для "insert" | insert;put;place;deposit |
| insert_syn_v | Синоніми для "inserted" | inserted;put;placed;deposited |
| begood | Синоніми для "good" | good;great;fantastic;a great idea |
| put | Команда "покласти" | #put_syn_v# the #obj_types# on the #(s)_var#. |
| put_syn_u | Синоніми для "Put" (з великої літери) | Put;Place;Sit;Rest |
| put_syn_v | Синоніми для "put" | put;place;sit;rest |
| on_it_syn | Синоніми для "on it" | on it;upon it |
| drop | Команда "кинути" | #drop_syn_v# the #obj_types# on the floor of the (r). |
| drop_syn_u | Синоніми для "Place" (з великої літери, для drop) | Place |
| drop_syn_v | Синоніми для "place" (для drop) | place;drop;ditch;throw;toss;deposit |
| eat | Команда "їсти" | #eat_syn_1# the #eat_var#. |
| eat_syn_u | Синоніми для "Eat" (з великої літери) | Eat; |
| eat_syn_1 | Синоніми для "eat" | eat; |
| eat_syn_v | Синоніми для "eaten" | eaten; |
| open | Команда "відкрити" | open the #lock_type_var#.;ensure that the #lock_type_var# is open.;#make_syn_v# that the #lock_type_var# is #open_syn#. |
| open_syn | Синоніми для "opened" | opened;open;wide open;ajar |
| close | Команда "закрити" | close the #lock_type_var#.;#make_syn_v# that the #lock_type_var# is #closed_syn#. |
| closed_syn | Синоніми для "closed" | closed;shut |
| eat_var | Варіації для їжі | #eat_types#;#eat_types# |
| on_var | Варіації для поверхонь (дублюється) | #on_types#;#on_types# #in_the_(r)# |
| unlock | Команда "відімкнути" | #unlock_key#;#unlock_no_key# |
| unlock_key | Відімкнути ключем | unlock the #lock_type_var# #by_the_syn# (k).;check that the #lock_type_var# is unlocked #by_the_syn# (k).;#make_syn_v# that the #lock_type_var# is unlocked #by_the_syn# (k).;insert the (k) into the #lock_type_var#'s lock to unlock it. |
| unlock_no_key | Відімкнути без ключа | unlock the #lock_type_var#.;#make_syn_v# that the #lock_type_var# is unlocked. |
| lock | Команда "замкнути" | #lock_key#;#lock_no_key# |
| lock_key | Замкнути ключем | lock the #lock_type_var# #by_the_syn# (k).;#make_syn_v# that the #lock_type_var# is locked #by_the_syn# (k).;#insert_syn_u# the (k) into the #lock_type_var# to lock it. |
| lock_no_key | Замкнути без ключа | lock the #lock_type_var#.;#make_syn_v# the #lock_type_var# is locked.;#make_syn_v# that the #lock_type_var# is locked. |
| go/north | Команда "йти на північ" | #go_syn_l# north.;#tryto# #go_syn_l# north. |
| go/south | Команда "йти на південь" | #go_syn_l# south.;#tryto# #go_syn_l# south. |
| go/east | Команда "йти на схід" | #go_syn_l# east.;#tryto# #go_syn_l# east. |
| go/west | Команда "йти на захід" | #go_syn_l# west.;#tryto# #go_syn_l# west. |
| go/north/d | Команда "йти на північ через двері" | #go_syn_l# through the north (d).;#tryto# #go_syn_l# through the north (d). |
| go/south/d | Команда "йти на південь через двері" | #go_syn_l# through the south (d).;#tryto# #go_syn_l# through the south (d). |
| go/east/d | Команда "йти на схід через двері" | #go_syn_l# through the east (d).;#tryto# #go_syn_l# through the east (d). |
| go/west/d | Команда "йти на захід через двері" | #go_syn_l# through the west (d).;#tryto# #go_syn_l# through the west (d). |
| go_syn_u | Синоніми для "Go" (з великої літери) | Go;Head;Venture;Travel;Move;Go to the;Take a trip |
| go_syn_l | Синоніми для "go" (з маленької літери) | go;head;venture;travel;move;go to the;take a trip |
| go_syn_v | Синоніми для "visited" (минулий час) | visited;travelled;moved;ventured;gone |
| tryto | Синоніми для "try to" | try to;make an effort to;make an attempt to;attempt to |
| wait | Команда "чекати" | Wait. |
| ig_unlock_open | Складна команда: відімкнути і відкрити | open the locked #lock_types# using the (k).;unlock and open the #lock_types#.;unlock and open the #lock_types# using the (k).;open the #lock_types# using the (k). |
| ig_unlock_open_take | Складна команда: відімкнути, відкрити і взяти | open the locked #lock_types# using the (k) and take the #obj_types_no_key#.;unlock the #lock_types# and take the #obj_types_no_key#.;unlock the #lock_types# using the (k), and take the #obj_types_no_key#.;take the #obj_types_no_key# from within the locked #lock_types#. |
| ig_open_take | Складна команда: відкрити і взяти | take the #obj_types# from the (c).;open the (c) and take the #obj_types#.;from in the closed (c), take the #obj_types#. |
| ig_take/c_unlock | Складна команда: взяти з контейнера і відімкнути | take the (k) and use it to unlock the #lock_types#.;unlock the #lock_types#, with the (k).; |
| ig_take/s_unlock | Складна команда: взяти з поверхні і відімкнути | take the (k) and use it to unlock the #lock_types#.;unlock the #lock_types#, with the (k).; |
| ig_take_unlock | Складна команда: взяти і відімкнути | #pick-up_synonym_1# the (k) and use it to unlock the #lock_types#.;unlock the #lock_types#, with the (k).; |
| ig_open_insert | Складна команда: відкрити і вставити | open the (c) and place the #obj_types# in it.;put the #obj_types# in the closed (c).; |
| ig_insert_close | Складна команда: вставити і закрити | place the #obj_types# in the (c) and close it.;close (c) after placing the #obj_types# in it. |
| ig_close_lock | Складна команда: закрити і замкнути | close the #lock_types# and lock it.;close the #lock_types# and lock it with the (k). |
| quest | Шаблон для квесту | #prologue# (list_of_actions) #epilogue# |
| quest_one_action | Шаблон для квесту з однією дією | #prologue_one_action# (action) |
| prologue | Вступ до квесту | #welcome#! Here is your task for today. #newsentence#;#welcome#! Here is how to play! #newsentence#;#welcome#! #newsentence#;Hey, thanks for coming over to the TextWorld today, there is something I need you to do for me. #newsentence# |
| prologue_one_action | Вступ до квесту з однією дією | #welcome#! Your task for today is to;#welcome#!;Your objective is to;Hey, thanks for coming over to TextWorld! Please |
| newsentence | Початок нового речення | First off,;First of all,;First stop,;First step,;Your first objective is to;First thing I need you to do is to;First off, if it's not too much trouble, I need you to;First of all, you could, like,;First, it would be #begood# if you could |
| action_separator | Роздільник між діями | Then, ; Next, ; Following that, ; If you can #do# that, ; Once you #do# that, ; That done, ; With that over with, ; With that accomplished, ; With that done, ; Okay, and then, ; And then, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| epilogue | Заключна частина квесту | Once that's all handled, you can stop!;And once you've done that, you win!;And if you do that, you're the winner!;That's it!;Got that? Good!;Alright, thanks! |
| do | Синоніми для "do" | manage;do;accomplish;get around to doing;finish;succeed at;get through with |
| welcome | Привітання | Welcome to TextWorld;You are now playing a #exciting# #game# of TextWorld;Welcome to another #exciting# #game# of TextWorld;It's time to explore the amazing world of TextWorld;Get ready to pick stuff up and put it in places, because you've just entered TextWorld;I hope you're ready to go into rooms and interact with objects, because you've just entered TextWorld;Who's got a virtual machine and is about to play through an #exciting# round of TextWorld? You do; |
| exciting | Синоніми для "exciting" | exciting;fast paced;life changing;profound |
| game | Синоніми для "game" | game;round;session;episode |
| action_separator_take | Роздільник після дії "взяти" | #afterhave# #havetaken# the #obj_types#, ; #after# #taking# the #obj_types#, ; With the #obj_types#, ; If you can get your hands on the #obj_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_take/s | Роздільник після дії "взяти з поверхні" | #afterhave# #havetaken# the #obj_types#, ; #after# #taking# the #obj_types#, ; With the #obj_types#, ; If you can get your hands on the #obj_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_take/c | Роздільник після дії "взяти з контейнера" | #afterhave# #havetaken# the #obj_types#, ; #after# #taking# the #obj_types#, ; With the #obj_types#, ; If you can get your hands on the #obj_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_eat | Роздільник після дії "їсти" | #afterhave# #ate# the #eat_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_insert | Роздільник після дії "вставити" | #afterhave# #inserted# the #obj_types# into the (c), ; #after# #inserting# the #obj_types# into the (c), ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_put | Роздільник після дії "покласти" | #afterhave# #put_v# the #obj_types# on the (s), ; #after# #putting# the #obj_types# on the (s), ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_open | Роздільник після дії "відкрити" | #afterhave# #opened# the #close_open_types#, ; #after# #opening# the #close_open_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_unlock | Роздільник після дії "відімкнути" | #afterhave# #unlocked# the #lock_types#, ; #after# #unlocking# the #lock_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_lock | Роздільник після дії "замкнути" | #afterhave# #locked# the #lock_types#, ; #after# #locking# the #lock_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_seperator_go | Роздільник після дії "йти" | #afterhave# #gone# (dir), ; #after# #getting# (dir), ; once you're (dir), ; once you're in the (dir), ; If you can manage to go (dir), ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_seperator_go/south | Роздільник після дії "йти на південь" | #afterhave# gone south, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_seperator_go/north | Роздільник після дії "йти на північ" | #afterhave# gone north, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_seperator_go/east | Роздільник після дії "йти на схід" | #afterhave# gone east, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_seperator_go/west | Роздільник після дії "йти на захід" | #afterhave# gone west, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_close | Роздільник після дії "закрити" | #afterhave# #closed# the #close_open_types#, ; #after# #closing# the #close_open_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| action_separator_drop | Роздільник після дії "кинути" | #afterhave# #dropped# the #obj_types#, ; #after# #dropping# the #obj_types#, ;#emptyinstruction1#;#emptyinstruction2#;#emptyinstruction3#;#emptyinstruction4#;#emptyinstruction5#;#emptyinstruction6#;#emptyinstruction7#;#emptyinstruction8#;#emptyinstruction9#;#emptyinstruction10# |
| afterhave | Синоніми для "After you have" | After you have;Having;Once you have;If you have |
| havetaken | Синоніми для "taken" | taken;got;picked up |
| havepicked-up | Синоніми для "picked up" | taken;got;picked up |
| after | Синоніми для "After" | After; |
| taking | Синоніми для "taking" | taking;getting;picking up;stealing |
| picking-up | Синоніми для "picking up" | taking;getting;picking up;stealing |
| ate | Синоніми для "ate" | ate;consumed |
| inserted | Синоніми для "inserted" | inserted;put in |
| inserting | Синоніми для "inserting" | inserting;putting in |
| put_v | Синоніми для "put" (дієслово) | put;place;set;set down |
| putting | Синоніми для "putting" | putting;placing;setting;setting down |
| opening | Синоніми для "opening" | opening;pulling open |
| opened | Синоніми для "opened" | opened;pulled open |
| unlocked | Синоніми для "unlocked" | unlocked |
| unlocking | Синоніми для "unlocking" | unlocking |
| locked | Синоніми для "locked" | locked |
| locking | Синоніми для "locking" | locking |
| gone | Синоніми для "gone" | gone;gotten |
| getting | Синоніми для "getting" (в контексті руху) | going;getting |
| closed | Синоніми для "closed" | closed;shut |
| closing | Синоніми для "closing" | closing;shutting |
| dropped | Синоніми для "dropped" | dropped;ditched;tossed;left behind |
| dropping | Синоніми для "dropping" | dropping;leaving behind |
| emptyinstruction1 | Порожня інструкція (роздільник) | And then, ; |
| emptyinstruction2 | Порожня інструкція (роздільник) | Then, ; |
| emptyinstruction3 | Порожня інструкція (роздільник) | After that, ; |
| emptyinstruction4 | Порожня інструкція (роздільник) | And then, ; |
| emptyinstruction5 | Порожня інструкція (роздільник) | After that, ; |
| emptyinstruction6 | Порожня інструкція (роздільник) | Then, ; |
| emptyinstruction7 | Порожня інструкція (роздільник) | And then, ; |
| emptyinstruction8 | Порожня інструкція (роздільник) | After that, ; |
| emptyinstruction9 | Порожня інструкція (роздільник) | And then, ; |
| emptyinstruction10 | Порожня інструкція (роздільник) | Then, ;

# Опис елементів файлу textworld\generator\data\text_grammars\house_room.twg

| назва елементу | призначення елементу | опис значення |
| :--- | :--- | :--- |
| i7_closed/open | Snippet для Inform7 | Генерує "an open" або "a closed" залежно від стану об'єкта. |
| i7_list_in | Snippet для Inform7 | Генерує список предметів, що знаходяться всередині об'єкта. |
| i7_list_on | Snippet для Inform7 | Генерує список предметів, що знаходяться на об'єкті. |
| i7_empty | Snippet для Inform7 | Генерує "an empty" або "a" залежно від того, чи порожній об'єкт. |
| inform7 | Snippet для Inform7 | Генерує опис стану об'єкта ("a locked", "an open", "a closed"). |
| inform7A | Snippet для Inform7 | Генерує опис стану об'єкта ("A locked", "An open", "A closed") з великої літери. |
| inform7noa | Snippet для Inform7 | Генерує опис стану об'єкта ("locked", "open", "closed") без невизначеного артикля. |
| inform7noun | Snippet для Inform7 | Генерує стан об'єкта як іменник ("locked", "open", "closed"). |
| inform7nounnoa | Snippet для Inform7 | Генерує стан об'єкта як іменник ("locked", "open", "closed") без невизначеного артикля. |
| dec | Основне правило для вступу в кімнату | Вибирає текст для представлення кімнати (при першому відвідуванні або повторному). |
| dec_type | Тип вступу в кімнату | Вибирає стиль представлення кімнати (звичайний, складний, грайливий тощо). |
| reg-0 | Шаблони введення кімнати (звичайний) | Посилання на шаблони `04`, `05`, `06`. |
| normal-0 | Шаблони введення кімнати (нормальний) | Посилання на шаблон `07`. |
| difficult-0 | Шаблони введення кімнати (складний) | Посилання на шаблон `016`. |
| moredifficult-0 | Шаблони введення кімнати (більш складний) | Посилання на шаблон `017`. |
| playful-0 | Шаблони введення кімнати (грайливий) | Посилання на різні грайливі шаблони `01`, `02`, `03`, `08`-`015`, `018`-`028`. |
| revisit | Текст для повторного відвідування кімнати | Різні фрази, що використовуються, коли гравець повертається в кімнату. |
| 01 | Шаблон для введення кімнати | "I am sorry to announce that you are now in the (name)". |
| 02 | Шаблон для введення кімнати | Опис кімнати як іменника з прикметниками, що передають атмосферу. |
| 03 | Шаблон для введення кімнати | Запитує, чи є кімната прикметником, і стверджує, що так. |
| 04 | Шаблон для введення кімнати | Опис знаходження в кімнаті, використовує `dec_find-yourself` або `dec_guess-what`. |
| 05 | Шаблон для введення кімнати | "Well, here we are in #dec_a_the# (name)". |
| 06 | Шаблон для введення кімнати | "You're now in #dec_a_the# (name)". |
| 07 | Шаблон для введення кімнати | "You've entered a (name);" або "You've just #dec_walked_into# a (name)". |
| 08 | Шаблон для введення кімнати | "This might come as a shock to you, but you've just #dec_entered# a (name)". |
| 09 | Шаблон для введення кімнати | Використовує `announce_mood` для оголошення про перебування в кімнаті. |
| 010 | Шаблон для введення кімнати | Розширений опис кімнати як іменника з прикметниками. |
| 011 | Шаблон для введення кімнати | "You have #dec_entered# the most (name-adj) of all possible (name-n)s". |
| 012 | Шаблон для введення кімнати | "Of every (name-n) you could have #dec_walked_into#, you had to #dec_walk_into# a (name-adj) one". |
| 013 | Шаблон для введення кімнати | "You have #dec_entered# a (name-n). Not the (name-n) you'd expect. No, this is a (name)". |
| 014 | Шаблон для введення кімнати | "You are in a (name-n). It seems to be pretty (name-adj) here". |
| 015 | Шаблон для введення кімнати | "You #dec_what# in a (name-adj) kind of place. That is to say, you're in a (name-n)". |
| 016 | Шаблон для введення кімнати | "You #dec_find-yourself# in a (name-n). A (name-adj) one". |
| 017 | Шаблон для введення кімнати | "You #dec_find-yourself# in a (name-n). A (name-adj) kind of place". |
| 018 | Шаблон для введення кімнати | Дублює шаблон `017`. |
| 019 | Шаблон для введення кімнати | Опис кімнати з емоційним забарвленням, що пояснює, чому все здається "(name-adj)". |
| 020 | Шаблон для введення кімнати | Пояснення, чому все "(name-adj)" тим, що ви щойно увійшли в "(name)". |
| 021 | Шаблон для введення кімнати | Грайливе привітання та опис несподіваного перебування в кімнаті. |
| 022 | Шаблон для введення кімнати | Фрази про невірогідність або несподіванку від входу в кімнату. |
| 023 | Шаблон для введення кімнати | Опис грандіозного входу в кімнату. |
| 024 | Шаблон для введення кімнати | Опис входу в кімнату як щось буденне для гравця. |
| 025 | Шаблон для введення кімнати | Заохочення озирнутися і відзначити унікальність кімнати. |
| 026 | Шаблон для введення кімнати | Порівняння кімнати з іншими та загальна позитивна оцінка. |
| 027 | Шаблон для введення кімнати | Опис кімнати через наявність знаку з привітанням. |
| 028 | Шаблон для введення кімнати | Різні короткі привітання та описи входу в кімнату. |
| GREETING! | Різні привітання | Варіанти привітань: "GREETING!", "GREETINGS!", "HELLO!", "ALRIGHT THEN!". |
| dec_entered | Синоніми для дієслова "увійшов" | "entered", "walked into", "fallen into", "moved into", "stumbled into", "come into". |
| dec_find-yourself | Фрази для "знайти себе" | "You #dec_what#". |
| dec_guess-what | Фрази типу "вгадайте що" | "Guess what", "Well how about that", "Well I'll be". |
| dec_well-guess | Фрази типу "ну, вгадайте" | "Guess what", "Well how about that", "Well I'll be". (Дублюється з dec_guess-what) |
| dec_what | Синоніми для "є" або "знайти себе" | "are", "find yourself", "arrive". |
| dec_a_the | Артиклі | "a", "the". |
| dec_in_at | Прийменники | "in", "at". |
| dec_walk_into | Синоніми для дієслова "зайти" | "walk into", "show up in", "saunter into", "come round". |
| dec_walked_into | Синоніми для дієслова "зайшов" (минулий час) | "walked into", "shown up in", "sauntered into". |
| announce_mood | Прикметники настрою оголошення | "sorry", "pleased", "excited", "stoked", "so happy", "honoured", "required", "obligated". |
| signquality | Прикметники якості знаку | "decrepit", "rusty", "laminated", "crooked", "well framed". |
| sign | Синоніми для іменника "знак" | "sign", "placard", "notice", "signboard", "board". |
| room_desc_(c) | Основне правило опису контейнерів | Комбінує опис зовнішнього вигляду контейнера з описом його вмісту. |
| containerdescription | Опис зовнішнього вигляду контейнерів | Використовує `room_desc_(c)_1_name` або `room_desc_(c)_1_noun`. |
| room_desc_(c)_content | Опис вмісту контейнера | Визначає, чи додавати опис вмісту, залежно від того, відкритий чи закритий контейнер. |
| opencontainer | Текст, що додається, якщо контейнер відкритий і має вміст | "The (name) contains #i7_list_in#". |
| emptyreaction | Текст, що додається, якщо відкритий контейнер порожній | Різні фрази, що виражають розчарування через порожній контейнер. |
| room_desc_(c)_1_name | Опис контейнера як прикметник + іменник | Вибирає шаблон опису залежно від рівня складності (наприклад, `reg-a`, `normal-a`). |
| room_desc_(c)_1_noun | Опис контейнера як іменник | Вибирає шаблон опису залежно від рівня складності (наприклад, `reg-b`, `normal-b`). |
| reg-a | Шаблони опису контейнера (прикметник+іменник, звичайний) | Посилання на шаблони `a1`, `a2`. |
| normal-a | Шаблони опису контейнера (прикметник+іменник, нормальний) | Посилання на шаблони `a3`, `a4`, `a5`. |
| difficult-a | Шаблони опису контейнера (прикметник+іменник, складний) | Посилання на шаблон `a6`. |
| moredifficult-a | Шаблони опису контейнера (прикметник+іменник, більш складний) | Посилання на шаблон `reg-a`. |
| playful-a | Шаблони опису контейнера (прикметник+іменник, грайливий) | Посилання на шаблон `reg-a`. |
| reg-b | Шаблони опису контейнера (іменник, звичайний) | Посилання на шаблони `b1`, `b2`. |
| normal-b | Шаблони опису контейнера (іменник, нормальний) | Посилання на шаблони `b3`, `b4`, `b5`. |
| difficult-b | Шаблони опису контейнера (іменник, складний) | Посилання на шаблон `reg-b`. |
| moredifficult-b | Шаблони опису контейнера (іменник, більш складний) | Посилання на шаблон `reg-b`. |
| playful-b | Шаблони опису контейнера (іменник, грайливий) | Посилання на шаблон `reg-b`. |
| room_desc_(c)_2_adj | Опис вмісту контейнера з прикметником | Комбінує прикметник зі списком вмісту. |
| room_desc_(c)_2 | Опис вмісту контейнера без прикметника | Генерує список вмісту. |
| room_desc_(c)_multi_noun | Опис кількох контейнерів (іменник) | Для сценаріїв з кількома контейнерами. |
| room_desc_(c)_multi_open_noun | Опис кількох відкритих контейнерів (іменник) | Для сценаріїв з кількома відкритими контейнерами. |
| room_desc_(c)_multi_adj | Опис кількох контейнерів (прикметник) | Для сценаріїв з кількома контейнерами. |
| room_desc_(c)_multi_open_adj | Опис кількох відкритих контейнерів (прикметник) | Для сценаріїв з кількома відкритими контейнерами. |
| a1 | Шаблон опису контейнера | "You see #inform7# (name)." або "a6". |
| a2 | Шаблон опису контейнера | "You see #inform7# #name_var# #here_alt#." або "a6". |
| a3 | Шаблон опису контейнера | "#inform7A# #name_var# is #here_alt#." або "a6". |
| a4 | Шаблон опису контейнера | Дублює `a1` або `a6`. |
| a5 | Шаблон опису контейнера | Дублює `a2` або `a6`. |
| a6 | Шаблон опису контейнера | "#prefix# (name)#suffix#". |
| b1 | Шаблон опису контейнера (іменник) | "You see #inform7# (name-n)." або "b5". |
| b2 | Шаблон опису контейнера (іменник) | "You see #inform7# (name-n) #here_alt#." або "b5". |
| b3 | Шаблон опису контейнера (іменник) | "#inform7A# (name-n) is #here_alt#." або "b5". |
| b4 | Шаблон опису контейнера (іменник) | Дублює `b1` або `b5`. |
| b5 | Шаблон опису контейнера (іменник) | "#prefix# (name-n)#suffix#". |
| c1 | Шаблон опису вмісту контейнера | "It is (name-adj), and #contains# #i7_list_in#." |
| c2 | Шаблон опису вмісту контейнера | "It is (name-adj). Also, there #listwithis# in it." |
| c3 | Шаблон опису вмісту контейнера | Дублює `c1`. |
| c4 | Шаблон опису вмісту контейнера | "ContentsC- [list of things in the (obj)]." |
| c5 | Шаблон опису вмісту контейнера | Опис вмісту з використанням `listwithis`. |
| c6 | Шаблон опису вмісту контейнера | Дублює `c9`. |
| c7 | Шаблон опису вмісту контейнера | Дублює `c9`. |
| c8 | Шаблон опису вмісту контейнера | "Let's see what's inside - #i7_list_in#." |
| c9 | Шаблон опису вмісту контейнера | Опис вмісту з посиланням на спогади. |
| d0 | Шаблон опису вмісту контейнера | "the (name) contains #i7_list_in#." |
| d1 | Шаблон опису вмісту контейнера | Використовує `contains` або `listwithis` для опису вмісту. |
| d2 | Шаблон опису вмісту контейнера | "There #listwithis# #foundin# it." |
| d3 | Шаблон опису вмісту контейнера | "You can see #i7_list_in# in the (name-n)." |
| d4 | Шаблон опису вмісту контейнера | "In it, you can see #i7_list_in#." |
| e1 | Шаблон опису кількох контейнерів (іменник) | Опис стану (відкритий/закритий/замкнений) кількох контейнерів. |
| f1 | Шаблон опису вмісту кількох відкритих контейнерів | "The (name-n) #contains# #i7_list_in#". |
| f2 | Шаблон опису вмісту кількох відкритих контейнерів | "There #listwithis# #foundin# the (name-n)". |
| f3 | Шаблон опису вмісту кількох відкритих контейнерів | "You can see #i7_list_in# in the (name-n)". |
| f4 | Шаблон опису вмісту кількох відкритих контейнерів | Дублює `f5` або `f6`. |
| f5 | Шаблон опису вмісту кількох відкритих контейнерів | Дублює `f6`. |
| f6 | Шаблон опису вмісту кількох відкритих контейнерів | Опис вмісту з посиланням на спогади. |
| g1 | Шаблон опису кількох контейнерів (прикметник) | Опис стану (відкритий/закритий/замкнений) кількох контейнерів з прикметником. |
| h1 | Шаблон опису вмісту кількох відкритих контейнерів (прикметник) | "The (name-adj) one #contains# #i7_list_in#". |
| h2 | Шаблон опису вмісту кількох відкритих контейнерів (прикметник) | "There #i7_list_in# #foundin# the (name-adj) one". |
| h3 | Шаблон опису вмісту кількох відкритих контейнерів (прикметник) | "You can see #i7_list_in# in the (name)". |
| h4 | Шаблон опису вмісту кількох відкритих контейнерів (прикметник) | "In the (name-adj) one, you can see #i7_list_in#". |
| it | Займенники або фрази | "It", "Something about it". |
| reminds_you | Фрази для спогадів/подібності | "reminds you of", "looks like", "floods your mind with memories of", "is reminiscent of", "is just like". |
| ofyouryouth | Фрази, пов'язані з молодістю | "of your youth", "that you knew in your youth", "that you knew so long ago", "that you knew so long ago, in your youth". |
| contains | Синоніми для дієслова "містить" | "contains", "has", "is filled with", "reveals inside it", "holds", "shelters", "offers you", "reveals to you". |
| foundin | Прийменники для "знайдено в" | "in", "found in". |
| it_is | Фрази для ствердження | "It is", "You can see that it is", "Upon examination, you see that it is". |
| name_var | Варіації для назви об'єкта | "(name)", "(name-n), which looks (name-adj),", "(name-adj) looking (name-n)". |
| contained | Синоніми для дієслова "містив" (минулий час) | "contained", "held", "had", "had in it", "revealed", "concealed", "sheltered", "offered you", "revealed to you", "guarded", "protected". |
| listwithis | Фраза для переліку предметів | "[is-are a list of things in the (obj)]". |
| lookthere | Вигуки для привернення уваги | "Look over there", "Wow! look at that". |
| ContentsC- | Префікси для переліку вмісту контейнера | "Contents-", "Contained within-", "Inside are the following-", "Inventory is as follows-", "Here's what's inside". |
| room_desc_(s) | Основне правило опису поверхонь (supporters) | Комбінує опис поверхонь з описом предметів на них. |
| room_desc_(s)_1_noun | Опис поверхні без прикметника | Використовує префікс і назву поверхні. |
| room_desc_(s)_1_name | Опис поверхні з прикметником | Використовує префікс і назву поверхні. |
| room_desc_(s)_2_adj | Опис вмісту поверхні з прикметником | Комбінує прикметник з описом предметів на поверхні. |
| room_desc_(s)_2 | Опис вмісту поверхні без прикметника | Опис предметів на поверхні. |
| room_desc_(s)_multi_noun | Опис кількох поверхонь (іменник) | Для сценаріїв з кількома поверхнями. |
| room_desc_(s)_multi_adj | Опис кількох поверхонь (прикметник) | Для сценаріїв з кількома поверхнями. |
| emptysupporter | Текст, коли поверхня порожня | Різні фрази, що виражають порожнечу поверхні. |
| emptysupporter_multi | Текст, коли кілька поверхонь порожні | Різні фрази, що виражають порожнечу кількох поверхонь. |
| on_it | Синоніми для "на ньому" | "on it", "lying on it", "resting on it", "upon it". |
| ContentsS- | Префікси для переліку вмісту поверхні | "Contents-", "Upon it are displayed the following-", "Upon it you may see the following-", "Upon it lie the following-", "Upon the (name-n) are displayed the following-", "Upon the (name-n) you may see the following-", "Upon the (name-n) lie the following-". |
| held | Синоніми для "утримувався" | "held", "carried", "had", "presented", "held up", "was used to support". |
| trash | Синоніми для "сміття" | "trash", "garbage", "junk". |
| room_desc_group | Опис групи об'єктів | Генерує опис групи об'єктів у кімнаті. |
| this_the | Артиклі/вказівні займенники | "this", "the". |
| room | Синоніми для "кімната" | "room", "place", "part of the game", "zone", "chamber", "area", "sector". |
| room_desc_(d) | Опис дверей | Генерує опис однієї двері в кімнаті, включаючи її стан (відкриті/закриті). |
| room_desc_(dir) | Опис неблокованого виходу | Генерує опис неблокованого виходу в певному напрямку. |
| room_exit_desc | Опис кількох розблокованих виходів | Описує кілька розблокованих виходів у кімнаті (вибирає шаблон залежно від складності). |
| room_desc_exits | Опис виходів | Генерує опис виходів (однина/множина). |
| room_desc_doors_closed | Опис групи закритих дверей | Описує групу закритих дверей у кімнаті. |
| room_desc_doors_open | Опис групи відкритих дверей | Описує групу відкритих дверей у кімнаті. |
| easy0a | Шаблон опису закритих дверей | "There are (^) closed doors, (name-indefinite), here", "Let's see how many closed doors there are. Looks like (^), (name-indefinite)", "There are (^) closed doors here, (name-indefinite)". |
| easy0b | Шаблон опису відкритих дверей | "There are (^) open doors, (name-indefinite), here", "Let's see how many open doors there are. Looks like (^), (name-indefinite)". |
| easy1 | Шаблон опису виходу | "There [is an|are] #unblocked# [exit|exits] to the (dir)", "There [is an|are] [exit|exits] to the (dir). And hey, don't worry, [they are|it's] #unblocked#". |
| medium1 | Шаблон опису виходу | "[An exit|Exits] #unblocked# [lies|lie] to the (dir)", "You can go (dir) from here without having to deal with any doors". |
| hard1 | Шаблон опису виходу | Різні фрази, що пропонують вихід у певному напрямку, уникаючи дверей. |
| easy2 | Шаблон опису дверей | "There [is a door|are doors], #looks# (name-adj), leading (dir)", "a (name) leads (dir)", "There is (name-indefinite) leading (dir)". |
| easy21 | Шаблон опису дверей | "There [is a door|are doors], #looks# (name-adj), leading (dir);a (name) leads (dir)". |
| easy22 | Шаблон опису дверей | "There is (name-indefinite) leading (dir)". |
| medium2 | Шаблон опису дверей | "You #canshould# see [the door|a door] [at the|blocking the] (dir) [exit|exits]". |
| hard2 | Шаблон опису дверей | "How do you get out? Well, there [is a door|are doors] to the (dir) of you". |
| easy3 | Шаблон опису дверей | "The [exit|exits] to the (dir) [is|are] going through (name)". |
| medium3 | Шаблон опису дверей | "The (dir) [exit|exits] [has|have] (name-indefinite) blocking [it|them]". |
| hard3 | Шаблон опису дверей | "The (dir) [exit|exits] [has|have] (name-n-indefinite) blocking [it|them]. the (name-n) [is|are] (name-adj)". |
| yourthing | Синоніми для "твоя справа" | "thing", "bag", "style", "cup of tea". |
| door_what | Дієслова для дії дверей | "leading", "facing", "heading". |
| unblocked | Прикметники для неблокованого виходу | "unblocked", "unguarded". |
| prefix | Префікс для описів об'єктів | Різні фрази, що вводять опис об'єкта в кімнаті. |
| prefix-multi | Префікс для описів кількох об'єктів | Різні фрази, що вводять опис кількох об'єктів у кімнаті. |
| prefix_(c) | Префікс для описів контейнерів | Використовує `prefix`. |
| prefix_(s) | Префікс для описів поверхонь | Використовує `prefix`. |
| suffix_meta | Мета-коментарі (суфікси) | Різні коментарі, що додаються до опису об'єкта. |
| suffix_fulfillment | Суфікси, пов'язані з виконанням | Різні фрази, що виражають чи об'єкт є тим, що шукали. |
| suffix_price_schtick | Суфікси, пов'язані з ціною | Різні фрази, що коментують ціну об'єкта. |
| suffix_(r) | Суфікси, пов'язані з кімнатою | Різні фрази, що стосуються кімнати. |
| suffix | Загальні суфікси | Різні загальні фрази, що додаються до опису. |
| suffix-multi | Суфікси для кількох об'єктів | Різні фрази, що додаються до опису кількох об'єктів. |
| suffix_(s)_mid | Суфікси для середини опису поверхні | Різні фрази, що додаються в середину опису поверхні. |
| suffix_(s)_end | Суфікси для кінця опису поверхні | Різні фрази, що додаються в кінець опису поверхні. |
| suffix_(s)_end_angry | Суфікси для кінця опису поверхні (гнівні) | Різні фрази, що виражають розчарування через порожню поверхню. |
| smelltype | Тип запаху | "an #ansmell#", "a #asmell#". |
| ansmell | Прикметники для запаху | "interesting", "awful", "intriguing". |
| asmell | Прикметники для запаху | "hideous", "pungent", "sickening", "terrible", "wretched", "lovely", "great", "fine". |
| upsetwith | Фрази для "розчарований" | "upset with", "angry about", "infuriated by", "depressed by", "done caring about", "upset by", "furious with". |
| pricetagexplain | Фрази для пояснення цінника | "that's still affixed to the (name-n)", "that the (name-n)'s owner still hasn't taken off", "that hangs off the (name-n)", "on the (name-n)", "glued to the (name-n)". |
| pricebad | Фрази для високої ціни | "#bignumber# dollars", "#bignumber# bucks", "#bignumber# big ones". |
| resourcenumber | Числові варіанти | Числа від 10 до 100 з кроком 5. |
| bignumber | Числові назви | "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "A hundred", "Two hundred", "Three hundred". |
| Iknow | Фрази для "Я знаю" | "I know a", "I got this", "I have a", "You know, I know a", "You know, I got a", "You know what, I've got a". |
| youknow | Фрази для "Ти знаєш" | "You know", "Do you know", "Did you ever meet", "You ever meet". |
| afriend | Фрази для опису друга/знайомого | "person, they work out of #friendplace#", "person", "friend", "person who works for #friendcompany#", "person, their #inlaw# works for #cooljob#". |
| inlaw | Родинні зв'язки/друзі | "uncle", "aunt", "sister-in-law", "brother-in-law", "cousin", "other friend", "buddy", "pal", "roommate", "dad", "mom", "brother", "sister", "neighbour". |
| myfriend | Фрази для "мій друг" | "they work for #friendcompany#". |
| cooljob | Опис "крутої роботи" | "the store", "#friendcompany#", "the mayor", "the president", "the prime minister", "the internet". |
| friendplace | Місце роботи друга | "the bank", "the big city", "city hall". |
| friendcompany | Компанія друга | "the government", "the post office", "the mayor", "a company". |
| friendtype | Тип друга | "buddy", "pal", "friend", "good friend". |
| pricefriend | Фрази для "ціна від друга" | "half that much", "half that", "six bucks", "practically nothing". |
| pricegood | Фрази для "гарна ціна" | "#resourcenumber# bucks". |
| expensiveplace | Фрази для "дороге місце" | "some kind of expensive place", "some kind of expensive store". |
| intheblank | Фрази для "викинути" | "in the dump", "in a fire", "into a pit", "into the garbage". |
| canshould | Дієслова можливості/пропозиції | "can", "should", "should be able to", "may". |
| looks | Синоніми для "виглядає" | "seems to be", "looks", "seems", "appears". |
| here_alt | Альтернативні фрази для "тут" | "here", "in the room", "nearby", "close by", "in the corner", "right there by you". |
| here_alt_u | Альтернативні фрази для "Туті" (з великої літери) | "Here", "In the room", "Nearby", "Close by", "In the corner", "Right there by you". |
| how_see | Фрази для "як ви бачите" | "You #you_what#", "You can #you_what#". |
| how_see_u | Фрази для "як ви бачите" (з великої літери) | "you #you_what#", "you can #you_what#". |
| there_what | Фрази для "там є/здається" | "is", "seems to be". |
| you_what | Дієслова для "ви бачите/розрізняєте" | "see", "make out". |
| emptymainperiod | Порожні інструкції (з крапкою) | Різні порожні інструкції, що закінчуються крапкою. |
| emptymain | Порожні інструкції | Різні порожні інструкції. |
| empty1-empty63 | Порожні інструкції | Різні порожні інструкції (для заповнення простору). |

# Опис елементів файлу textworld\generator\data\text_grammars\house_obj.twg

| назва елементу | призначення елементу | опис значення |
| :--- | :--- | :--- |
| ordinary_adj | Загальні прикметники | Список загальних прикметників: "ordinary", "normal", "typical", "standard", "usual". |
| adj_stripped | Спрощені прикметники | Посилання на `simpleadj`. |
| simpleadj | Прості прикметники | Список простих прикметників: "good", "bad", "small", "big", "heavy", "light", "great", "terrible", "expensive", "cheap". |
| number | Числові значення | Числа від 0 до 9. |
| room_type | Категорії кімнат | Список категорій кімнат: "clean", "cook", "rest", "work", "storage". |
| (P) | Опис гравця | Комбінація прикметника та іменника гравця. |
| (P)_noun | Іменники для гравця | Зазвичай порожньо ("None"). |
| (P)_adj | Прикметники для гравця | Зазвичай порожньо ("None"). |
| (r) | Загальний опис кімнати | Комбінація прикметника та іменника кімнати. |
| (r)_noun | Загальні іменники кімнат | Список іменників: "washroom", "bathroom", "cupboard", "pantry", "basement", "closet", "kitchen", "kitchenette". |
| (r)_adj | Загальні прикметники кімнат | Список прикметників: "nondescript", "plain". |
| clean_(r) | Опис "чистої" кімнати | Комбінації прикметників та іменників для різних типів чистих кімнат. |
| clean_(r)_noun_type_1 | Іменники для кімнат "самоочищення" | "washroom", "bathroom", "restroom". |
| clean_(r)_adj_type_1 | Прикметники для кімнат "самоочищення" | "spotless", "clean", "cramped". |
| clean_(r)_noun_type_2 | Іменники для кімнат "очищення речей" | "launderette", "laundromat", "laundry place". |
| clean_(r)_adj_type_2 | Прикметники для кімнат "очищення речей" | "spotless", "steamy", "misty", "crowded", "cramped", "cheap". |
| clean_(r)_noun_type_3 | Іменники для кімнат всередині кімнати (душ) | "shower". |
| clean_(r)_adj_type_3 | Прикметники для кімнат всередині кімнати | "spotless", "steamy", "misty", "marbled". |
| clean_(r)_noun_type_4 | Іменники для саун/парних | "sauna", "steam room". |
| clean_(r)_adj_type_4 | Прикметники для саун/парних | "spotless", "steamy", "misty", "luxurious", "damp". |
| storage_(r) | Опис "комірчини" | Комбінація прикметника та іменника. |
| storage_(r)_noun | Іменники для "комірчини" | "pantry", "basement", "closet", "attic", "garage", "vault", "cellar", "spare room". |
| storage_(r)_adj | Прикметники для "комірчини" | "spacious", "roomy", "cramped", "stuffed", "messy", "forgotten", "ugly", "gloomy". |
| cook_(r) | Опис "кухні" | Комбінація прикметника та іменника. |
| cook_(r)_noun | Іменники для "кухні" | "kitchen", "kitchenette", "canteen", "cookery", "scullery", "cookhouse", "dish-pit". |
| cook_(r)_adj | Прикметники для "кухні" | Посилання на `hot-adj`, "hot", "steamy", "sweaty", "balmy". |
| rest_(r) | Опис "кімнати відпочинку" | Комбінації прикметників та іменників для різних типів кімнат відпочинку. |
| rest_(r)_noun_type_1 | Іменники для "спалень" | "bedroom", "bedchamber", "chamber". |
| rest_(r)_adj_type_1 | Прикметники для "спалень" | "cozy", "relaxing", "pleasant", "sleepy". |
| rest_(r)_noun_type_2 | Іменники для "соціальних кімнат" | "lounge", "bar", "parlor", "salon", "playroom", "recreation zone". |
| rest_(r)_adj_type_2 | Прикметники для "соціальних кімнат" | "fun", "entertaining", "exciting", "well lit". |
| work_(r) | Опис "робочої кімнати" | Комбінація прикметника та іменника. |
| work_(r)_noun | Іменники для "робочої кімнати" | "office", "studio", "workshop", "cubicle", "study". |
| work_(r)_adj | Прикметники для "робочої кімнати" | "silent", "austere", "serious", "still". |
| hot-adj | Прикметники для "гарячих" описів | "super", "unreasonably", "absurdly", "alarmingly", "upsettingly". |
| (c) | Загальний опис контейнера | Комбінація прикметника та іменника. |
| (c)_noun | Загальні іменники контейнерів | "chest", "box", "safe", "locker". |
| (c)_adj | Загальні прикметники контейнерів | "sturdy", "nice", "ugly". |
| (c)_adj_noun | Комбінація прикметника та іменника контейнера | Розширюється до `(c)_adj | (c)_noun`. |
| clean_(c) | Опис "чистого" контейнера | Комбінації прикметників та іменників для різних типів чистих контейнерів. |
| clean_(c)_noun_type_1 | Іменники для типу 1 "чистих" контейнерів | "cabinet", "basket", "box", "safe", "trunk", "case". |
| clean_(c)_adj_type_1 | Прикметники для типу 1 "чистих" контейнерів | "gross", "stained", "spotless", "plain". |
| clean_(c)_noun_type_2 | Іменники для типу 2 "чистих" контейнерів | "drawer", "dresser", "cabinet". |
| clean_(c)_adj_type_2 | Прикметники для типу 2 "чистих" контейнерів | Посилання на `wood_type` + "wood". |
| storage_(c) | Опис "контейнера для зберігання" | Комбінація прикметника та іменника. |
| storage_(c)_noun | Іменники для "контейнера для зберігання" | "toolbox", "chest", "safe", "locker", "trunk", "coffer", "cabinet", "crate", "case", "suitcase", "display". |
| storage_(c)_adj | Прикметники для "контейнера для зберігання" | "rusty", "neglected", "brand new". |
| cook_(c) | Опис "кухонного контейнера" | Комбінація прикметника та іменника. |
| cook_(c)_noun | Іменники для "кухонного контейнера" | "fridge", "refrigerator", "freezer", "chest", "cabinet", "case". |
| cook_(c)_adj | Прикметники для "кухонного контейнера" | "fancy", "big", "small". |
| rest_(c) | Опис "контейнера для відпочинку" | Комбінація прикметника та іменника. |
| rest_(c)_noun | Іменники для "контейнера для відпочинку" | "dresser", "chest", "basket", "box", "safe", "locker", "trunk", "coffer", "suitcase", "portmanteau". |
| rest_(c)_adj | Прикметники для "контейнера для відпочинку" | "new", "dusty", "clean", "amazing". |
| work_(c) | Опис "робочого контейнера" | Комбінація прикметника та іменника. |
| work_(c)_noun | Іменники для "робочого контейнера" | "cabinet", "box", "safe", "locker", "trunk", "bureau", "coffer", "case", "suitcase", "toolbox", "portmanteau", "display". |
| work_(c)_adj | Прикметники для "робочого контейнера" | "iron", "rusty", "ancient". |
| fruit | Фрукти | Список назв фруктів: "watermelon", "melon", "honeydew", "strawberry", "apple", "pear", "grape", "kiwi", "cantaloupe". |
| (d) | Загальний опис дверей | Комбінація прикметника та іменника. |
| (d)_adj | Прикметники для дверей | Посилання на `wood_type`, "wooden", "stone". |
| madeof | Фраза "зроблено з" | Статична фраза: "made of". |
| wood_type | Типи деревини | Список типів деревини: "oak", "birch", "maple", "balsam", "beech", "mahogany", "walnut", "cedar", "pine". |
| (d)_noun | Іменники для дверей | "door", "portal", "gate", "passageway", "gateway", "hatch". |
| (s) | Загальний опис поверхні (supporter) | Комбінація прикметника та іменника. |
| (s)_noun | Загальні іменники поверхонь | "shelf", "table", "pedestal", "slab". |
| (s)_adj | Загальні прикметники поверхонь | Посилання на `(o)_adj`. |
| clean_(s) | Опис "чистої" поверхні | Комбінація прикметника та іменника. |
| clean_(s)_noun | Іменники для "чистої" поверхні | "board", "shelf", "table", "counter", "rack", "bench". |
| clean_(s)_adj | Прикметники для "чистої" поверхні | "dusty", "chipped", "shiny". |
| storage_(s) | Опис "поверхні для зберігання" | Комбінація прикметника та іменника. |
| storage_(s)_noun | Іменники для "поверхні для зберігання" | "shelf", "table", "workbench", "counter", "rack", "stand". |
| storage_(s)_adj | Прикметники для "поверхні для зберігання" | "rusty", "shoddy", "splintery", "rough". |
| cook_(s) | Опис "кухонної поверхні" | Комбінація прикметника та іменника. |
| cook_(s)_noun | Іменники для "кухонної поверхні" | "counter", "board", "shelf", "table", "rack", "chair", "plate", "bowl", "pan", "platter", "saucepan". |
| cook_(s)_adj | Прикметники для "кухонної поверхні" | "greasy", "soaped down", "filthy", "messy". |
| rest_(s) | Опис "поверхні для відпочинку" | Комбінація прикметника та іменника. |
| rest_(s)_noun | Іменники для "поверхні для відпочинку" | "bed", "couch", "shelf", "bookshelf", "desk", "bed stand", "mantelpiece", "mantle", "bar", "bench", "stand", "recliner". |
| rest_(s)_adj | Прикметники для "поверхні для відпочинку" | "comfy", "warm", "worn-out". |
| work_(s) | Опис "робочої поверхні" | Комбінація прикметника та іменника. |
| work_(s)_noun | Іменники для "робочої поверхні" | "stand", "bookshelf", "table", "chair", "shelf", "desk", "mantelpiece", "mantle", "stand", "armchair". |
| work_(s)_adj | Прикметники для "робочої поверхні" | "stern", "solid", "worn", "gross". |
| (o) | Загальний опис об'єкта | Комбінація прикметника та іменника. |
| (o)_noun | Загальні іменники об'єктів | "pencil", "pen". |
| (o)_adj | Загальні прикметники об'єктів | Список прикметників: "new", "old", "used", "dusty", "clean", "large", "small", "fancy", "plain", "ornate", "antique", "contemporary", "modern", "dirty", "elegant", "simple", "hefty", "modest", "austere". |
| clean_(o) | Опис "чистого" об'єкта | Комбінації прикметників та іменників для різних типів чистих об'єктів. |
| clean_(o)_noun | Іменники для "чистих" об'єктів | Посилання на `clean_(o)_noun_type_1`, `clean_(o)_noun_type_2`, `clean_(o)_noun_type_3`. |
| clean_(o)_adj | Прикметники для "чистих" об'єктів | Посилання на `clean_(o)_adj_type_1`, `clean_(o)_adj_type_2`, `clean_(o)_adj_type_3`. |
| clean_(o)_adj_noun | Комбінація прикметника та іменника "чистого" об'єкта | Посилання на відповідні `clean_(o)_adj_type` та `clean_(o)_noun_type`. |
| clean_(o)_noun_type_1 | Іменники для типу 1 "чистих" об'єктів (прилади) | "iron", "mop", "broom", "vacuum". |
| clean_(o)_adj_type_1 | Прикметники для типу 1 "чистих" об'єктів | Список прикметників, що описують стан приладів. |
| clean_(o)_noun_type_2 | Іменники для типу 2 "чистих" об'єктів (паперові вироби) | "paper towel", "sponge". |
| clean_(o)_adj_type_2 | Прикметники для типу 2 "чистих" об'єктів | Список прикметників, що описують стан паперових виробів. |
| clean_(o)_noun_type_3 | Іменники для типу 3 "чистих" об'єктів (неодноразові) | "mat", "towel", "soap dispenser", "mop", "broom", "shirt", "sock", "sponge". |
| clean_(o)_adj_type_3 | Прикметники для типу 3 "чистих" об'єктів | Список прикметників, що описують стан неодноразових предметів. |
| storage_(o) | Опис "об'єкта для зберігання" | Комбінації прикметників та іменників для різних типів об'єктів для зберігання. |
| storage_(o)_noun_type_1 | Іменники для типу 1 "об'єктів для зберігання" (одяг) | "shirt", "sock", "shoe", "glove", "hat", "scarf", "cloak", "top hat", "pair of pants". |
| storage_(o)_adj_type_1 | Прикметники для типу 1 "об'єктів для зберігання" | Список прикметників, що описують стан одягу. |
| storage_(o)_noun_type_2 | Іменники для типу 2 "об'єктів для зберігання" (прилади) | "lightbulb", "broom", "cane", "pair of headphones", "lampshade", "frisbee", "golf #golf#". |
| storage_(o)_adj_type_2 | Прикметники для типу 2 "об'єктів для зберігання" | Список прикметників, що описують стан приладів. |
| golf | Пов'язані з гольфом іменники | "club", "tee", "ball". |
| bugobject | Опис об'єкта-комахи | Комбінації прикметників та іменників, що описують комах або пов'язані з ними об'єкти. |
| storage_(o)_adj_type_4 | Прикметники для об'єктів-комах | "wriggling", "grotesque", "repulsive", "tiny". |
| storage_(o)_noun_type_4 | Іменники для об'єктів-комах | "worm", "fly larva", "bug", "insect", "nest of #bugs#", "butterfly", "shadfly". |
| bugs | Комахи | Список назв комах та схожих істот. |
| cook_(o) | Опис "кухонного об'єкта" | Комбінації прикметників та іменників для різних типів кухонних об'єктів. |
| cook_(o)_noun_type_1 | Іменники для типу 1 "кухонних об'єктів" (столові прилади) | "fork", "knife", "spoon", "spork", "teaspoon". |
| cook_(o)_adj_type_1 | Прикметники для типу 1 "кухонних об'єктів" | Список прикметників, що описують столові прилади. |
| cook_(o)_noun_type_2 | Іменники для типу 2 "кухонних об'єктів" (кухонні прилади) | "napkin", "whisk", "ladle", "blender", "kettle", "teapot". |
| cook_(o)_adj_type_2 | Прикметники для типу 2 "кухонних об'єктів" | Список прикметників, що описують кухонні прилади. |
| cook_(o)_noun_type_3 | Іменники для типу 3 "кухонних об'єктів" (посуд) | "mug", "bowl", "teacup", "glass", "coffee cup". |
| cook_(o)_adj_type_3 | Прикметники для типу 3 "кухонних об'єктів" | Список прикметників, що описують посуд. |
| rest_(o) | Опис "об'єкта для відпочинку" | Комбінації прикметників та іменників для різних типів об'єктів для відпочинку. |
| rest_(o)_noun_type_1 | Іменники для типу 1 "об'єктів для відпочинку" (екран) | "tv", "laptop", "tablet", "monitor". |
| rest_(o)_adj_type_1 | Прикметники для типу 1 "об'єктів для відпочинку" | "shiny", "widescreen", "shut off", "flat-screen". |
| rest_(o)_noun_type_2 | Іменники для типу 2 "об'єктів для відпочинку" (електроніка) | "tv", "controller", "dvd", "cd", "lamp", "laptop", "synthesizer". |
| rest_(o)_adj_type_2 | Прикметники для типу 2 "об'єктів для відпочинку" | Список прикметників, що описують електроніку. |
| rest_(o)_noun_type_3 | Іменники для типу 3 "об'єктів для відпочинку" (комфортні речі) | "pillow", "blanket", "plant", "cushion". |
| rest_(o)_adj_type_3 | Прикметники для типу 3 "об'єктів для відпочинку" | "cozy", "comfy", "comfortable", "plush", "frilly", "nice", "small", "big", "heavy", "cute". |
| rest_(o)_adj_type_5 | Прикметники для типу 5 "об'єктів для відпочинку" (дивна книга) | "cool", "gigantic", "enormous", "famous", "old". |
| rest_(o)_noun_type_5 | Іменники для типу 5 "об'єктів для відпочинку" (дивна книга) | "novel", "book", "manuscript", "poem", "textbook". |
| work_(o) | Опис "робочого об'єкта" | Комбінації прикметників та іменників для різних типів робочих об'єктів. |
| work_(o)_noun_type_1 | Іменники для типу 1 "робочих об'єктів" (канцелярія) | "pen", "pencil", "staple", "mug", "disk", "cd", "book", "backup calendar". |
| work_(o)_adj_type_1 | Прикметники для типу 1 "робочих об'єктів" | Список прикметників, що описують канцелярію. |
| work_(o)_noun_type_2 | Іменники для типу 2 "робочих об'єктів" (електроніка) | "printer", "mouse", "keyboard", "laptop", "desktop computer", "telephone". |
| work_(o)_adj_type_2 | Прикметники для типу 2 "робочих об'єктів" | "fancy", "broken", "operational", "working". |
| work_(o)_noun_type_3 | Іменники для типу 3 "робочих об'єктів" (календар) | "Cat Calendar", "Comic Strip Calendar", "Quote of the Day Calendar", "Advent Calendar". |
| work_(o)_adj_type_3 | Прикметники для типу 3 "робочих об'єктів" | "heartwarming", "hilarious", "mind-expanding", "out of date", "typo-riddled". |
| work_(o)_noun_type_4 | Іменники для типу 4 "робочих об'єктів" (пристрій для іншого пристрою) | "stapler", "printer", "mouse", "keyboard", "folder", "binder". |
| work_(o)_adj_type_4 | Прикметники для типу 4 "робочих об'єктів" | "operational", "broken", "expensive", "useless", "outmoded". |
| (f) | Загальний опис їжі | Комбінація прикметника та іменника. |
| (f)_adj | Прикметники для їжі | Посилання на `(f)_adj_good`, `(f)_adj_bad`, `(f)_adj_neutral`. |
| (f)_noun | Іменники для їжі | Посилання на `(f)_noun_fruit`, `(f)_noun_vegetable`, `(f)_noun_grain`, `(f)_noun_protein`, `(f)_noun_dairy`, `candy`. |
| (f)_noun_fruit | Іменники для фруктів | Список назв фруктів та ягід. |
| (f)_noun_vegetable | Іменники для овочів | Список назв овочів та деяких страв. |
| (f)_noun_grain | Іменники для зернових | "loaf of bread", "sandwich". |
| (f)_noun_protein | Іменники для білкових продуктів | "legume", "cashew", "peanut", "burger". |
| (f)_noun_dairy | Іменники для молочних продуктів | "stick of butter", "fondue". |
| (f)_adj_good | Прикметники для "хорошої" їжі | "fresh", "maturing", "soft", "chilled", "organic". |
| (f)_adj_bad | Прикметники для "поганої" їжі | "aging", "half-eaten", "rotting". |
| (f)_adj_neutral | Прикметники для "нейтральної" їжі | "frozen", "large", "small", "massive", "tiny", "hefty", "sizable", "dried", "dry", "pureed". |
| berry | Ягоди | Список назв ягід. |
| clean_(f) | "Чиста" їжа | Посилання на `(f)`. |
| storage_(f) | "Зберігання" їжі | Посилання на `(f)`. |
| cook_(f) | "Приготування" їжі | Посилання на `(f)`. |
| rest_(f) | "Відпочинок" їжі | Посилання на `(f)`. |
| work_(f) | "Робота" їжі | Посилання на `(f)`. |
| candy | Цукерки | "chocolate bar", "gummy bear", "candy bar", "licorice strip", "cookie". |
| (k) | Загальний опис ключа | Комбінація прикметника та іменника. |
| (k)_adj | Прикметники для ключів | "iron", "brass", "metal", "rusty", "steel", "iron", "aluminum", "copper". |
| (k)_noun | Іменники для ключів | "key", "keycard", "latchkey", "passkey". |
| (P)_desc | Функція опису гравця | "It's you." |
| (c)_desc | Функція опису контейнера | "The (name) looks strong, and impossible to #force_open#." |
| force_open | Дієслова для "силового відкриття" | "break", "crack", "destroy". |
| (s)_desc | Функція опису поверхні | "The (name) is #supp_stable#." |
| supp_stable | Прикметники стабільності поверхні | "stable", "wobbly", "unstable", "balanced", "durable", "reliable", "solid", "undependable", "solidly built", "an unstable piece of #garbage#", "shaky". |
| garbage | Синоніми для "сміття" | "garbage", "trash", "junk". |
| (o)_desc | Функція опису об'єкта | "The (name) is #obj_what#."; "The (name) #looks_seems# #out_in_place# here". |
| obj_what | Прикметники для опису об'єкта | "unremarkable", "clean", "dirty", "modern", "antiquated", "well-used", "brand new", "expensive looking", "cheap looking". |
| looks_seems | Синоніми для "виглядає/здається" | "looks", "seems", "appears", "appears to be", "would seem to be". |
| out_in_place | Фрази для розміщення об'єкта | "out of place", "to fit in", "well matched to everything else". |
| restaurant | Назви ресторанів | "Burger#place#". |
| place | Назви місць | "town", "village", "hamlet", "burg", "ville", "City". |
| (f)_desc | Функція опису їжі | "The (name) looks #food_what#."; "that's a (name-adj) (name-n)!"; "You couldn't pay me to eat that (name-adj) thing." |
| food_what | Прикметники для привабливості їжі | "appetizing", "delicious", "tasty", "appealing", "delectable", "heavenly", "inviting", "savory", "tantalizing", "tempting". |
| (k)_desc | Функція опису ключа | "The (name) is cold to the touch"; "The (name) is #key_weight#."; "The metal of the (name) is #key_metal#."; "The (name) looks useful". |
| key_weight | Прикметники для ваги ключа | "heavy", "light", "weighty", "surprisingly heavy", "heavier than it looks". |
| key_metal | Прикметники для металу ключа | "antiqued", "brushed", "hammered", "polished", "satin", "rusty". |
| (d)_desc | Функція опису дверей | "The (name) looks #door_what_is#."; "it's a #door_what_is# (name-n)"; "it is what it is, a (name)". |
| door_what_is | Прикметники для вигляду дверей | "imposing", "sturdy", "well-built", "durable", "robust", "rugged", "hefty", "commanding", "grand", "noble", "ominous", "towering", "manageable", "solid", "stuffy". |
| openable_desc | Опис стану відкривається об'єкта | "It is open." / "It is closed." / "It is locked." або "You can see inside it." / "You can't see inside it..." / "There is a lock on it.". |
| on_desc | Опис предметів на об'єкті | Різні фрази, що описують предмети, що лежать на об'єкті. |
| letter | Літери | Літери англійського алфавіту: "A" - "Z". |
| clearancelevel | Тип рівня допуску | "type #number#", "type #letter#", "#brand#", "#shape#", "#smell# scented". |
| brand | Типи брендів | "#brandname# style", "#brandname# limited edition", "#brandname#". |
| brandname | Назви брендів | "Microsoft", "American", "Canadian", "Henderson's", "TextWorld". |
| shape | Форми | "rectangular", "cuboid", "spherical", "formless", "non-euclidean". |
| colour | Кольори | "red", "blue", "chartreuse", "purple", "violet", "orange", "yellow", "green", "brown", "teal", "cyan". |
| smell | Запахи | "vanilla", "lavender", "cake", "fudge", "fresh laundry", "soap". |
| (k<->d)_match | Опис відповідності ключа-двері | Комбінація прикметника ключа та рівня допуску з іменником ключа, що відповідає прикметнику дверей та рівню допуску з іменником дверей, або колір ключа відповідає кольору дверей. |
| (k<->c)_match | Опис відповідності ключа-контейнера | Комбінація прикметника ключа та рівня допуску з іменником ключа, що відповідає прикметнику контейнера та рівню допуску з іменником контейнера, або колір ключа відповідає кольору контейнера. |
