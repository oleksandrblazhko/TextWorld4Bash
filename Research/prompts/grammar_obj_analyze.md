# Аналіз впливу house_obj.twg на повідомлення гри custom_3room.json

Цей документ детально описує, як правила з `textworld\generator\data\text_grammars\house_obj.twg` впливають на формування ігрових повідомлень, особливо на описи об'єктів, під час гри, згенерованої на основі `custom_3room.json`.

### 1. Початковий стан гри та завдання

Аналіз файлу `custom_3room.json` показує наступний стан:
*   **Гравець (P)** знаходиться в кімнаті `r_0` (горище).
*   **Об'єкти в кімнаті:**
    *   `c_0`: "chest" (скриня), стан: `closed` (закрита), `unlocked` (незамкнена, припущення на основі квесту).
    *   `k_0`: "key" (ключ), лежить у кімнаті.
*   **Квест:** Взяти ключ, а потім замкнути скриню цим ключем.

### 2. Детальний покроковий розбір генерації повідомлень (фокус на house_obj.twg)

#### Крок 1: Початкове повідомлення (Завдання)

*   **Повідомлення гри:**
    > "Hey, thanks for coming over to the TextWorld today, there is something I need you to do for me. First of all, recover the key from the floor of the attic. Then, make absolutely sure the chest inside the attic is locked. Once that's all handled, you can stop!"
*   **Внесок `house_obj.twg`:** Мінімальний. `house_obj.twg` переважно стосується назв та описів об'єктів, а не інструкцій квесту.

---

#### Крок 2: Опис початкової кімнати ("Attic")

Під час опису кімнати, правила `house_obj.twg` відіграють ключову роль у формуванні назв та базових описів об'єктів.

*   **Повідомлення гри (можливий варіант):**
    > "You are now in the Attic. You see a closed chest. There is a key on the floor."

*   **Покроковий аналіз генерації (фокус на `house_obj.twg`):**

    1.  **Назва та тип об'єктів:**
        *   Для скрині (`c_0`): `custom_3room.json` вказує `type: "c"`, що відповідає `(c)` в `house_obj.twg`.
            *   ` (c) ` -> `# (c)_adj_noun #`
            *   ` # (c)_adj_noun #` -> `# (c)_adj # | # (c)_noun #`
            *   ` # (c)_noun #` може розширитися до "chest".
            *   ` # (c)_adj #` може розширитися до "sturdy", "nice", "ugly" тощо.
            *   У цьому прикладі використовується лише іменник "chest", хоча міг би бути згенерований і прикметник.
        *   Для ключа (`k_0`): `custom_3room.json` вказує `type: "k"`, що відповідає `(k)` в `house_obj.twg`.
            *   ` (k) ` -> `# (k)_adj # | # (k)_noun #`
            *   ` # (k)_noun #` може розширитися до "key".
            *   ` # (k)_adj #` може розширитися до "iron", "brass", "metal" тощо.

    2.  **Базовий опис об'єктів (включно зі станом):**
        *   Правило `inform7` з `house2_room.twg` (яке використовує `(obj)`) визначає, як описати стан "closed" (закритий) для скрині. Однак сам іменник ("chest") походить з `house_obj.twg`.

---

#### Крок 3: Дія гравця "examine chest" (Оглянути скриню)

Ця дія викликає детальне функцію опису об'єкта, яка повністю визначена в `house_obj.twg`.

*   **Дія гравця:** `examine chest`
*   **Повідомлення гри (можливий варіант):**
    > "The chest looks strong, and impossible to break."

*   **Покроковий аналіз генерації (фокус на `house_obj.twg`):**

    1.  Система викликає функцію опису для контейнера `c_0`.
    2.  Основне правило: `(c)_desc` з `house_obj.twg`.
    3.  ` (c)_desc ` -> `The (name) looks strong, and impossible to #force_open#.`
    4.  `(name)` замінюється на "chest".
    5.  ` #force_open#` може розширитися до "break", "crack", "destroy".
    6.  **Результат:** "The chest looks strong, and impossible to break."

---

#### Крок 4: Дія гравця "examine key" (Оглянути ключ)

Аналогічно до скрині, опис ключа також походить з `house_obj.twg`.

*   **Дія гравця:** `examine key`
*   **Повідомлення гри (можливий варіант):**
    > "The key is cold to the touch. The metal of the key is rusty."

*   **Покроковий аналіз генерації (фокус на `house_obj.twg`):**

    1.  Система викликає функцію опису для ключа `k_0`.
    2.  Основне правило: `(k)_desc` з `house_obj.twg`.
    3.  ` (k)_desc ` -> `The (name) is cold to the touch`; `The (name) is #key_weight#`; `The metal of the (name) is #key_metal#`; `The (name) looks useful`.
    4.  Генератор обирає один або кілька варіантів.
    5.  `(name)` замінюється на "key".
    6.  ` #key_metal#` може розширитися до "antiqued", "brushed", "hammered", "polished", "satin", "rusty".
    7.  **Результат:** "The key is cold to the touch. The metal of the key is rusty."

---

#### Крок 5: Дія гравця "take key"

*   **Дія гравця:** `take key`
*   **Повідомлення гри:** "You take the key."
*   **Внесок `house_obj.twg`:** Об'єкт "key" та його ім'я походить з `house_obj.twg`. Однак саме повідомлення про успішність дії ("You take the...") генерується правилами з `house_instruction.twg`.

---

#### Крок 6: Дія гравця "lock chest with key"

*   **Дія гравця:** `lock chest with key`
*   **Повідомлення гри:** "You lock the chest with the key."
*   **Внесок `house_obj.twg`:** Об'єкти "chest" та "key" та їхні відповідні властивості (наприклад, `#lock_type_var#` розширюється до "chest") походять з `house_obj.twg`. Повідомлення про успішність дії генерується `house_instruction.twg`.
*   **Додатковий внесок `house_obj.twg`:** Правила відповідності ключів-контейнерів (`(k<->c)_match`) у `house_obj.twg` визначають, який ключ підходить до якого контейнера, що є критично важливим для успішного виконання цієї дії.

---

#### Крок 7: Завершення квесту

*   **Повідомлення гри:** "Once that's all handled, you can stop!"
*   **Внесок `house_obj.twg`:** Мінімальний, оскільки це фіксована частина епілогу квесту, що не залежить від опису об'єктів.
