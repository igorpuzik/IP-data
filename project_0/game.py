"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def median_guessing(number: int=1) -> int:
    """Медианно угадываем число

    Args:
        number (int, optional): _description_. Defaults to np.random.randin(1, 101).

    Returns:
        int: _description_
    """
    min = 1
    max = 101

    count = 0

    while True:
        count+=1
        mid = (min+max) // 2
    
        if mid > number:
          max = mid
    
        elif mid < number:
          min = mid

        else:
            break #Конец игры выход из цикла
    return count


def score_game(median_guessing) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        median_guessing([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(median_guessing(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(median_guessing)
