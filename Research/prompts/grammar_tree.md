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

---

# Ланцюжок виводу тексту на екран

Процес виводу згенерованого тексту на екран під час інтерактивної гри відбувається окремо від генерації граматики. Ось як це працює:

1.  **Ігровий цикл**: Основний ігровий цикл знаходиться у файлі `scripts/tw-play` (а також у `textworld/helpers.py` у функції `play`).
    *   У циклі `for` програма отримує команду від агента (`agent.act()`), надсилає її до середовища (`env.step()`) і отримує новий стан гри (`game_state`).

2.  **Виклик рендерингу**: Після кожного кроку гри викликається метод `env.render()`.
    ```python
    # Уривок з scripts/tw-play
    ...
    game_state, reward, done = env.step(command)

    if args.mode == "human" or args.verbose:
        env.render()
    ...
    ```

3.  **Реалізація `render()`**: Метод `render()` реалізовано в базовому класі `Environment` у файлі `textworld/core.py`.
    *   Він отримує основний текст для виводу з атрибуту `game_state.feedback`.
    *   Форматує текст, наприклад, переносячи його по 80 символів для зручності читання.
    *   Записує фінальне повідомлення у стандартний вивід (`sys.stdout`), що і призводить до його появи на екрані.

    ```python
    # Уривок з textworld/core.py

    * Якщо mode (режим виведення) є 'ansi' або 'text', тоді outfile присвоюється об'єкт StringIO(). Це спеціальний об'єкт, який діє як текстовий файл у пам'яті, дозволяючи функції render() записувати 
     в нього текст, який потім можна буде отримати як рядок. Це корисно для тестування або для подальшої обробки тексту.
    * Якщо mode не є 'ansi' або 'text' (наприклад, для режиму 'human', який використовується для відображення у консолі), тоді outfile присвоюється sys.stdout. sys.stdout — це стандартний потік       
     виведення, який зазвичай є консоллю або терміналом, де користувач бачить повідомлення програми.

    def render(self, mode: str = "human") -> Optional[str]:
        ...
        outfile = StringIO() if mode in ['ansi', "text"] else sys.stdout
        msg = self.state.feedback.rstrip() + "\n"
        ...
        outfile.write(msg + "\n")
        ...
    ```

## Зведення файлів та функцій для виводу

*   **Точка входу**: Ігровий цикл у `scripts/tw-play` або `textworld.helpers.play`.
*   **Основний виклик**: `env.render()`
*   **Джерело тексту**: `game_state.feedback`
*   **Фінальна функція виводу**: `outfile.write()`, де `outfile` посилається на `sys.stdout`.
*   **Розташування**: `textworld.core.Environment.render()`
