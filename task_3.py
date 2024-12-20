import sys
from collections import Counter

def parse_log_line(line: str) -> dict:  # парсинг рядків логу
    try:
        date, time, level, *message = line.strip().split(' ', 3)
        return {
            'date': date,
            'time': time,
            'level': level,
            'message': ' '.join(message)
        }
    except ValueError:
        return None

def load_logs(file_path: str) -> list:  # завнтаження логу з файла
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [parse_log_line(line) for line in file.readlines() if parse_log_line(line)]
    except FileNotFoundError:
        print(f'Файл "{file_path}" не знайдено.')
        sys.exit(1)
    except Exception as ex:
        print(f'Виникла проблема при читанні файлу: {ex}')
        sys.exit(1)


def filter_logs_by_level(logs: list, level: str) -> list:   # фільтрація логів по рівню
    # return [log for log in logs if log['level'].upper() == level.upper()]
    return list(filter(lambda log: log['level'] == level.upper(), logs))



def count_logs_by_level(logs: list) -> dict:    # підрахунок логів за рівнем
    levels = [log['level'] for log in logs]
    return Counter(levels)

def display_log_counts(counts: dict):   # виведення результатів підрахунку
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print('{:<17}| {:<2}'.format(level, count))
    print('')
    
# ******************************************************************************
def main():
    if len(sys.argv) < 2:
        print("Синтаксис: python task_3.py <log_file_path> [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]     # отримати аргументи функції
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file_path)

    if log_level:                   # якщо є аргумент LEVEL
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} - {log['message']}")
        print('')
    else:                            # вивести кілкість записів по рівню логування
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

if __name__ == "__main__":
    main()
