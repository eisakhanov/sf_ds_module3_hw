""""Модуль, предоставляющий функцию для угадывания числа и функцию для оценки"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число от 1 до 100. Дефолтное значение 1.

    Returns:
        int: Число попыток
    """

    min_value = 1
    max_value = 100

    if number > max_value or number < min_value:
        raise ValueError("Число должно находиться в диапозоне от 1 до 100")

    count = 0

    while max_value >= min_value:
        count += 1

        predict_value = (max_value + min_value) // 2
        if predict_value == number:
            break
        elif predict_value > number:
            max_value = predict_value - 1
        else:
            min_value = predict_value + 1

    return count


def score_game(random_predict_function) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(42)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
