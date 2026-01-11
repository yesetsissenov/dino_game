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
2. Откройте PowerShell в корне проекта (папка, где лежит `requirements.txt` и папка `src`).
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

## Частые ошибки

**Ошибка:** `ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'`

**Что делать:**
- Убедитесь, что вы находитесь в корне проекта. В этой папке должны быть файлы `README.md` и `requirements.txt`, а также каталог `src`.
- Если вы скачали ZIP с GitHub, папка обычно называется `dino_game-main`. Перейдите в неё:

```powershell
cd $env:USERPROFILE\Desktop\dino_game-main
```

Затем снова выполните:

```powershell
pip install -r requirements.txt
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
