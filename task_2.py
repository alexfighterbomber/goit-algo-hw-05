from typing import Callable
import re

def generator_numbers(text: str):    # знаходить дійсні числа в тексті
    pattern = r'\d+\.\d+'  # регулярний вираз для пошуку дійсних чисел \d+\.\d+
    for num in re.findall(pattern, text):
        yield float(num)  # генератор повертає числа по одному


def sum_profit(text: str, func: Callable[[str], float]):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
