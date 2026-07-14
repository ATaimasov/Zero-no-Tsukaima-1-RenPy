import argparse
from pathlib import Path

def main():
    # 1. Настраиваем парсер аргументов
    parser = argparse.ArgumentParser(description="Сборка .rpy файлов Ren'Py в один .md файл для нейросети.")
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Искать файлы также во всех вложенных папках (рекурсивно).'
    )
    parser.add_argument(
        '-i', '--ignore',
        nargs='*',
        default=[],
        help='Имена папок, которые нужно игнорировать при поиске (например: -i tl cache images).'
    )
    args = parser.parse_args()

    current_dir = Path('.')

    # 2. Ищем файлы в зависимости от флага
    if args.recursive:
        print("Режим: Рекурсивный поиск (включая вложенные папки)...")
        rpy_files = sorted(current_dir.rglob('*.rpy'))
    else:
        print("Режим: Поиск только в текущей папке (без вложенности)...")
        rpy_files = sorted(current_dir.glob('*.rpy'))

    # Исключаем сам файл результата, если он вдруг окажется в папке (на всякий случай)
    output_file = current_dir / 'combined_rpy.md'
    rpy_files = [f for f in rpy_files if f != output_file]

    # 2.5. Исключаем файлы из указанных игнорируемых папок
    if args.ignore:
        ignore_dirs = set(args.ignore)
        filtered_files = []
        for f in rpy_files:
            # f.parent.parts возвращает кортеж с именами всех папок в пути (например: ('game', 'tl', 'russian'))
            # Если пересечение с игнорируемыми папками пустое, значит файл не в игнорируемой папке
            if not ignore_dirs.intersection(f.parent.parts):
                filtered_files.append(f)

        rpy_files = filtered_files
        print(f"Игнорируются папки: {', '.join(args.ignore)}")

    if not rpy_files:
        print("Ошибка: не найдено ни одного .rpy файла (возможно, все были отфильтрованы).")
        return

    print(f"Найдено файлов: {len(rpy_files)}. Начинаю сборку...")

    # 3. Собираем всё в один Markdown файл
    with output_file.open('w', encoding='utf-8') as out_f:
        out_f.write("# Combined Ren'Py Scripts\n\n")
        mode_desc = "с учетом вложенных папок" if args.recursive else "только из текущей директории"
        out_f.write(f"Объединенный файл скриптов ({mode_desc}).\n\n")

        # Добавляем пометку для нейросети, что некоторые папки были пропущены
        if args.ignore:
            out_f.write(f"*Примечание: при сборке были намеренно проигнорированы папки: {', '.join(args.ignore)}.*\n\n")

        for rpy_file in rpy_files:
            # Получаем относительный путь, чтобы ИИ видел структуру папок
            rel_path = rpy_file.relative_to(current_dir)

            out_f.write(f"## Файл: `{rel_path}`\n\n")
            out_f.write("```renpy\n")

            with rpy_file.open('r', encoding='utf-8') as in_f:
                out_f.write(in_f.read())

            out_f.write("\n```\n\n")

    print(f"Готово! Результат сохранен в '{output_file.name}'")

if __name__ == "__main__":
    main()


# Рекурсивно, но без папок с переводами и кэшем
#python script.py -r -i tl cache

# Только в текущей папке, игнорируя папки images и audio
#python script.py -i images audio
