# Ланцюжок викликів граматики

Генерація тексту з файлів граматики (`.twg`) у TextWorld відбувається за наступним ланцюжком викликів:

1.  **`textworld.generator.maker.GameMaker.build()`**: Це головна точка входу для створення гри. Вона організовує весь процес генерації гри.

2.  **`textworld.generator.text_grammar.Grammar.__init__()`**: Всередині `GameMaker.build()` створюється об'єкт `Grammar`. Конструктор класу `Grammar` відповідає за завантаження файлів граматики.
    *   Він визначає `theme` (тему) з наданих `GrammarOptions`.
    *   Він знаходить усі файли `.twg`, що відповідають темі, у каталозі `textworld/generator/data/text_grammars`.
    *   Для кожного файлу `.twg` він викликає `self._parse()`.

3.  **`textworld.generator.text_grammar.Grammar._parse()`**: Цей метод зчитує вміст файлу `.twg`.
    *   Він використовує `textworld.textgen.TextGrammar.parse()` для розбору правил граматики з вмісту файлу.
    *   Розібрані правила зберігаються в об'єкті `Grammar`.

4.  **`textworld.generator.game.Game.change_grammar()`**: Повертаючись до `GameMaker.build()`, цей метод викликається для об'єкта `Game`. Він приймає новостворений об'єкт `Grammar` як вхідний параметр.

5.  **`textworld.generator.text_generation.generate_text_from_grammar()`**: `Game.change_grammar()` викликає цю функцію, яка є ядром процесу генерації тексту. Вона використовує об'єкт `Grammar` для генерації всього тексту в грі.

    Ця функція та її допоміжні функції (`assign_name_to_object`, `assign_description_to_room`, `describe_event` тощо) широко використовують `grammar.expand()` та інші методи класу `Grammar` для розширення правил граматики у фінальні текстові описи для кімнат, об'єктів та квестів.

## Зведення файлів та функцій

*   **Точка входу**: `textworld.generator.maker.GameMaker.build()`
*   **Завантаження граматики**:
    *   `textworld.generator.text_grammar.Grammar.__init__()`
    *   `textworld.generator.text_grammar.Grammar._parse()`
    *   `textworld.textgen.TextGrammar.parse()` (Фактичний парсер)
*   **Генерація тексту**:
    *   `textworld.generator.game.Game.change_grammar()`
    *   `textworld.generator.text_generation.generate_text_from_grammar()`
    *   Різні допоміжні функції у `textworld.generator.text_generation`.
