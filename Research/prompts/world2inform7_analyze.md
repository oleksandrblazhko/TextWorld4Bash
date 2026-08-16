У програмі textworld для стандартних файлів граматики (тема house) створено файли з українською транслітерацією.
Файли граматики містять слова, словосполучання для взаємодії з користувачем.
Виявилося, що частина слів та словосполучень розміщено у модулі textworld\generator\inform7\world2inform7.py



Так. У цьому файлі видно важливий момент: частина текстів, які користувач бачить під час гри, справді не належить до файлів граматики. Вони генеруються безпосередньо в world2inform7.py.

Зокрема, є кілька категорій.

1. Команди та їх опис у help

У gen_source() безпосередньо генерується:

say "  look:                describe the current room[line break]";
say "  goal:                print the goal of this game[line break]";
say "  inventory:           print player's inventory[line break]";
say "  go <dir>:            move the player north, east, south or west[line break]";
...

Тобто тут є англомовні слова і словосполучення, які не будуть замінені зміною граматики.

2. Команди Understand

Наприклад:

Understand "goal" as printing the objective.

і:

Understand "help" as displaying help message.

Також:

Understand "take all" as taking all.
Understand "get all" as taking all.
Understand "pick up all" as taking all.

Це вже не повідомлення, а лексика, яку Inform 7 розпізнає як команду користувача.

Тому для української транслітерації тут треба розрізняти:

що користувач вводить;
що TextWorld виводить;
що є внутрішнім ідентифікатором Inform 7.
3. Повідомлення про виконання дій

Наприклад:

Report taking something from the location:
    say "You pick up [the noun] from the ground." instead.


Report taking something:
    say "You take [the noun] from [the previous locale]." instead.


Report dropping something:
    say "You drop [the noun] on the ground." instead.

Ці рядки теж не беруться з граматики.

Тобто навіть якщо граматика повністю перекладена/транслітерована, результат може залишатися англійським:

You take the key from the chest.
4. Системні повідомлення

Є ще багато таких рядків:

say "Room contents:[line break]";
say "World: [line break]";
say "You are carrying: ";
say "Nowhere:[line break]";
say "There is [L with indefinite articles] on the floor.";

і:

say "You have to open the [blocking door] first.";
say "The [locked door] is welded shut.";
say "You have to unlock the [locked door] with the [X] first.";

Вони також зашиті безпосередньо в Python-коді.

5. Але важливіше: не всі слова треба перекладати

Наприклад:

Understand "goal" as printing the objective.

goal — це вхідна команда, яку треба замінити на потрібний варіант української транслітерації, якщо ми хочемо, щоб користувач вводив українські команди.

А от:

Printing the objective is an action applying to nothing.

Printing the objective — це внутрішня назва action Inform 7. Її перекладати не потрібно.

Те саме стосується:

quest{quest_id}
printing the objective
taking all
reporting max score
printing the id of player

Це частина внутрішнього коду.

Висновок

Для створення української транслітерації нам фактично треба аналізувати три джерела лексики:

grammar/*.i7
        │
        ├── команди та їх синтаксис
        │
        ▼
world2inform7.py
        │
        ├── Understand "..."
        ├── say "..."
        ├── Report ...: say "..."
        └── інші повідомлення
        │
        ▼
Inform 7 / generated .ni
        │
        ▼
.z8

І я б не перекладав усі рядки, які містять say. Це буде неправильний критерій.

Правильніше створити список користувацької лексики:

Understand "..." — вхідні команди/синоніми.
say "..." — текст, який бачить користувач.
Report ... say "..." — повідомлення про дії.
Before ... say "..." — повідомлення про помилки/обмеження.
Rule for ... say "..." — системні повідомлення.
help — окремий блок опису команд.
При цьому не чіпати внутрішні імена Inform 7.

Це також пояснює, чому переклад лише стандартних grammar-файлів у house виявився недостатнім. У вашому випадку транслітерація має охоплювати і grammar-файли, і шаблон генерації Inform 7 у world2inform7.py.