sudo apt update
sudo apt install -y build-essential libffi-dev python3-dev curl git

# 2. Клонування твого репозиторію
cd ~
git clone https://github.com/oleksandrblazhko/TextWorld4Bash.git

# 3. Перейти в проект
cd ~/TextWorld4Bash

# 4. Створити окреме virtual environment
python3 -m venv ~/venvs/textworld4bash

# 5. Активувати
source ~/venvs/textworld4bash/bin/activate

# 6. Оновити інструменти Python
python -m pip install --upgrade pip setuptools wheel

# 7. Встановити саме локальний TextWorld4Bash
pip install -e .
