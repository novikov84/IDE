"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def binary_search(number: int = 1) -> int:
    """Ищем ответ путем бинарного поиска, опираясь на ответы 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    pass



def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
        
    # Исходный диапазон поиска - от 1 до 100
    start_range = 1
    end_range = 101
    
    # Начинаем с середине диапазона поиска
    predict = 51
    
    while number != predict:
        count += 1
        # Предсказываем число из середины текущего диапазона поиска
        predict = start_range + (end_range - start_range) // 2
        
        # В зависимости от результата уменьшаем диапазон поиска в два раза
        if number > predict:
            start_range = predict
        elif number < predict:
            end_range = predict

    return count


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
