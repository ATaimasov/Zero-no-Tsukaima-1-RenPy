import re
import msvcrt
from pathlib import Path

# ============================================================
# ПРОВЕРКА ПУНКТУАЦИИ REN'PY
# ============================================================


ENDING_MARKS = {
    ".",
    "!",
    "?",
    "…",
    "。",
    "！",
    "？",
}


# ============================================================
# ПРОВЕРКА КОНЦА СТРОКИ
# ============================================================


def needs_period(text):
    """
    Проверяет, заканчивается ли текст буквой или цифрой
    без знака окончания.
    """

    text = text.rstrip()

    if not text:
        return False

    last_char = text[-1]

    # Уже есть знак окончания
    if last_char in ENDING_MARKS:
        return False

    # Заканчивается буквой или цифрой
    if last_char.isalpha() or last_char.isdigit():
        return True

    return False


# ============================================================
# NEW — ИСПРАВЛЕНИЕ ТОЧКИ В КОНЦЕ
# ============================================================


def fix_new_line(line, line_number):

    match = re.match(r'^(\s*new\s+")(.+)("\s*)$', line)

    if not match:
        return line, False

    prefix = match.group(1)
    text = match.group(2)
    suffix = match.group(3)

    if not needs_period(text):
        return line, False

    stripped = text.rstrip()
    trailing_spaces = text[len(stripped):]

    new_text = stripped + "." + trailing_spaces
    new_line = prefix + new_text + suffix

    print(f"[NEW] Строка {line_number}")
    print(f"  Было:  {line.rstrip()}")
    print(f"  Стало: {new_line.rstrip()}")
    print()

    return new_line, True


# ============================================================
# OLD — ПРОВЕРКА ТОЧКИ В КОНЦЕ
# ============================================================


def check_old_line(line, line_number):

    match = re.match(r'^(\s*old\s+")(.+)("\s*)$', line)

    if not match:
        return False

    text = match.group(2)

    if needs_period(text):

        print(
            f"[OLD] Строка {line_number}: "
            f"отсутствует знак окончания"
        )

        print(f"      {line.rstrip()}")
        print()

        return True

    return False


# ============================================================
# ПРОВЕРКА МНОГОТОЧИЯ
# ============================================================


def has_old_ellipsis(text):
    """
    Проверяет наличие трёх и более обычных точек подряд.

    Например:

    ...
    ......
    ........

    """

    return bool(re.search(r'\.{3,}', text))


# ============================================================
# NEW — ИСПРАВЛЕНИЕ МНОГОТОЧИЯ
# ============================================================


def fix_ellipsis_new_line(line, line_number):

    match = re.match(r'^(\s*new\s+")(.+)("\s*)$', line)

    if not match:
        return line, False

    prefix = match.group(1)
    text = match.group(2)
    suffix = match.group(3)

    # Ищем три и более обычных точки
    if not has_old_ellipsis(text):
        return line, False

    # Любые 3+ точек подряд превращаем в …
    new_text = re.sub(r'\.{3,}', '…', text)

    new_line = prefix + new_text + suffix

    if new_line == line:
        return line, False

    print(f"[NEW] Строка {line_number}")
    print(f"  Было:  {line.rstrip()}")
    print(f"  Стало: {new_line.rstrip()}")
    print()

    return new_line, True


# ============================================================
# OLD — ПРОВЕРКА МНОГОТОЧИЯ
# ============================================================


def check_ellipsis_old_line(line, line_number):

    match = re.match(r'^(\s*old\s+")(.+)("\s*)$', line)

    if not match:
        return False

    text = match.group(2)

    if has_old_ellipsis(text):

        print(
            f"[OLD] Строка {line_number}: "
            f"используется ... вместо …"
        )

        print(f"      {line.rstrip()}")
        print()

        return True

    return False


# ============================================================
# РЕЖИМ 1 — ИСПРАВИТЬ NEW: ТОЧКИ
# ============================================================


def fix_new(input_file):

    input_path = Path(input_file)

    output_path = input_path.with_name(
        input_path.stem + "_fixed" + input_path.suffix
    )

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed_lines = []
    changes = 0

    for line_number, line in enumerate(lines, start=1):

        new_line, changed = fix_new_line(
            line,
            line_number
        )

        if changed:
            changes += 1

        fixed_lines.append(new_line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)

    print("=" * 60)
    print(f"NEW: исправлено строк: {changes}")
    print(f"Копия сохранена:")
    print(output_path)


# ============================================================
# РЕЖИМ 2 — ПРОВЕРИТЬ OLD: ТОЧКИ
# ============================================================


def check_old(input_file):

    input_path = Path(input_file)

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    problems = 0

    for line_number, line in enumerate(lines, start=1):

        if check_old_line(line, line_number):
            problems += 1

    print("=" * 60)

    if problems == 0:
        print("OLD: проблем не найдено.")
    else:
        print(
            f"OLD: найдено строк без знака окончания: "
            f"{problems}"
        )


# ============================================================
# РЕЖИМ 3 — ИСПРАВИТЬ NEW: МНОГОТОЧИЕ
# ============================================================


def fix_ellipsis_new(input_file):

    input_path = Path(input_file)

    output_path = input_path.with_name(
        input_path.stem + "_fixed" + input_path.suffix
    )

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed_lines = []
    changes = 0

    for line_number, line in enumerate(lines, start=1):

        new_line, changed = fix_ellipsis_new_line(
            line,
            line_number
        )

        if changed:
            changes += 1

        fixed_lines.append(new_line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)

    print("=" * 60)
    print(f"NEW: исправлено многоточий: {changes}")
    print(f"Копия сохранена:")
    print(output_path)


# ============================================================
# РЕЖИМ 4 — ПРОВЕРИТЬ OLD: МНОГОТОЧИЕ
# ============================================================


def check_ellipsis_old(input_file):

    input_path = Path(input_file)

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    problems = 0

    for line_number, line in enumerate(lines, start=1):

        if check_ellipsis_old_line(line, line_number):
            problems += 1

    print("=" * 60)

    if problems == 0:
        print("OLD: неправильных многоточий не найдено.")
    else:
        print(
            f"OLD: найдено строк с ...: {problems}"
        )

# ============================================================
# ВЫБОР .RPY ФАЙЛА СТРЕЛКАМИ
# ============================================================

def select_rpy_file(start_path="."):
    current_dir = Path(start_path).resolve()

    while True:
        # Получаем содержимое папки
        items = []

        # Родительская папка
        if current_dir.parent != current_dir:
            items.append(("..", current_dir.parent, True))

        # Папки
        directories = sorted(
            [p for p in current_dir.iterdir() if p.is_dir()],
            key=lambda p: p.name.lower()
        )

        # .rpy файлы
        files = sorted(
            [p for p in current_dir.iterdir()
             if p.is_file() and p.suffix.lower() == ".rpy"],
            key=lambda p: p.name.lower()
        )

        for directory in directories:
            items.append(("📁 " + directory.name, directory, True))

        for file in files:
            items.append(("📄 " + file.name, file, False))

        if not items:
            print()
            print("Папка пуста.")
            input("Нажмите Enter...")
            return None

        selected = 0

        while True:
            # Очистка экрана
            print("\033[2J\033[H", end="")

            print("=" * 60)
            print("Выбор .rpy файла")
            print("=" * 60)
            print()
            print(f"Папка: {current_dir}")
            print()

            for i, (name, path, is_directory) in enumerate(items):
                if i == selected:
                    print(f"> {name}")
                else:
                    print(f"  {name}")

            print()
            print("↑ ↓ — выбор")
            print("Enter — открыть / выбрать")
            print("Backspace — назад")
            print("Q — выход")

            key = msvcrt.getwch()

            # Стрелка / специальные клавиши
            if key in ("\x00", "\xe0"):
                key = msvcrt.getwch()

                if key == "H":       # ↑
                    selected -= 1
                    if selected < 0:
                        selected = len(items) - 1

                elif key == "P":     # ↓
                    selected += 1
                    if selected >= len(items):
                        selected = 0

            elif key == "\r":        # Enter
                name, path, is_directory = items[selected]

                if is_directory:
                    current_dir = path
                    break
                else:
                    return path

            elif key == "\x08":      # Backspace
                if current_dir.parent != current_dir:
                    current_dir = current_dir.parent
                    break

            elif key.lower() == "q":
                return None


# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Проверка пунктуации Ren'Py")
    print("=" * 60)
    print()

    input_path = select_rpy_file(".")

    if input_path is None:
        print()
        print("Выход.")
        raise SystemExit

    print()
    print(f"Выбран файл:")
    print(input_path)

    while True:

        print()
        print("=" * 60)
        print("Выберите режим:")
        print()
        print("1 — Исправить NEW: точки в конце")
        print("2 — Проверить OLD: точки в конце")
        print("3 — Исправить NEW: многоточие ... → …")
        print("4 — Проверить OLD: многоточие ...")
        print()
        print("Enter — выйти")
        print()

        mode = input("Введите номер режима: ").strip()

        # Enter — выход
        if not mode:
            print()
            print("Выход.")
            break

        print()

        if mode == "1":
            fix_new(input_path)

        elif mode == "2":
            check_old(input_path)

        elif mode == "3":
            fix_ellipsis_new(input_path)

        elif mode == "4":
            check_ellipsis_old(input_path)

        else:
            print("ОШИБКА: неизвестный режим.")
            continue

        print()
        print("=" * 60)
        print("Проверка завершена.")
        print()
        print("Enter — вернуться к выбору режима")
        print("Q — выйти")
        print()

        answer = input("Ваш выбор: ").strip().lower()

        if answer == "q":
            print()
            print("Выход.")
            break