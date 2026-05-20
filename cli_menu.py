#!/usr/bin/env python3
import os
import sys

try:
    import questionary
    from rich.console import Console
except ImportError:
    print("Ошибка: Необходимы библиотеки 'questionary' и 'rich'.")
    print("Выполните: pip install questionary rich")
    sys.exit(1)

console = Console()

def main():
    console.clear()
    console.print("[bold cyan]========================================[/bold cyan]")
    console.print("[bold cyan]   🛠️  MY CLI TOOLS - Глобальное меню[/bold cyan]")
    console.print("[bold cyan]========================================[/bold cyan]\n")

    # Здесь в будущем можно сделать динамический поиск скриптов по папкам
    choices = [
        questionary.Choice("📂 Объединить файлы (combine)", value="combine"),
        questionary.Choice("🌳 Построить дерево файлов (tree)", value="tree"),
        questionary.Choice("🌐 Проверить переводы VMS", value="vms_trans"),
        questionary.Separator(),
        questionary.Choice("❌ Выход", value="exit")
    ]

    action = questionary.select(
        "Выберите утилиту для запуска:",
        choices=choices,
        style=questionary.Style([('highlighted', 'fg:#00ffff bold')])
    ).ask()

    if action == "exit" or action is None:
        console.print("[yellow]Выход.[/yellow]")
        sys.exit(0)

    console.print(f"[bold green]Вы выбрали: {action} (Скрипт пока в разработке)[/bold green]")
    # Пример вызова другого скрипта:
    # if action == "combine":
    #     os.system("python tools/file_ops/combine.py")

if __name__ == "__main__":
    main()
