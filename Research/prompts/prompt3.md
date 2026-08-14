# Persona

Було виконано: 
1) команду створення світу:
tw-make custom --force --theme house --world-size 1 --nb-objects 2 --seed 1234 --output tw_games/custom_2room.z8

2) виконано команду tw-play запуску світу, яка напочатку вивела наступне повідомлення:
Get ready to pick stuff up and put it in places, because you've just entered
TextWorld! Here is how to play! First step, recover the key from the floor of
the attic. Once you have got the key, assure that the chest is locked. Alright,
thanks!

3) Раніше ти проаналізував файл опису граматики інструкцій textworld\generator\data\text_grammars\house_*.twg 
та створив файл Research\prompts\grammar_info.md

# Tasks

1) детально поясни як програма створила початкове повідомлення.
2) поясни, чому у файлі опису граматики інструкцій елемент welcome не використовується для створення початкового повідомлення
2) поясни, чому у файлі опису граматики інструкцій елемент action_separator використовується для створення початкового повідомлення

# Format

Результат збережи у файлі Research\prompts\grammar_instruction_analyze.md