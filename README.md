# Dino Game (Windows, Pygame)

Базовая версия офлайн-игры как в Chrome: бесконечный раннер с кактусами, птеродактилями, счетчиком очков и сменой дня/ночи.

## Архитектура

```
src/
  main.py           # точка входа и игровой цикл
  game/
    config.py       # константы: размеры, скорости, цвета
    entities.py     # логика динозавра и препятствий
    world.py        # счет, скорость, смена дня/ночи
    ui.py           # отрисовка очков и сообщений
```

## Управление

- Прыжок: Space или стрелка вверх
- Выход: Esc
- Перезапуск после столкновения: Space

## Запуск на Windows

1. Установите Python 3.10+.
2. Откройте PowerShell в корне проекта.
3. Создайте и активируйте виртуальное окружение:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Установите зависимости:

```powershell
pip install -r requirements.txt
```

5. Запустите игру:

```powershell
python -m src.main
```

## Публикация на GitHub

Я не могу загружать репозиторий на GitHub от вашего имени, но вы можете сделать это так:

```powershell
git init
git add .
git commit -m "Initial Dino game"
git branch -M main
git remote add origin https://github.com/<ваш-логин>/<имя-репозитория>.git
git push -u origin main
```
