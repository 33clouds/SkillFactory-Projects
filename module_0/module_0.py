#!/usr/bin/env python
# coding: utf-8

import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать,
       как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core(number):
    '''Находим загаданное число методом половинного деления.
       Функция принимает загаданное число и возвращает число попыток'''
    left = 1
    right = 100
    count = 1
    while True:
        predict = (left+right)//2
        if predict == number:
            break
        count += 1
        if predict < number:
            left = predict+1
        else:
            right = predict-1
    return(count)


score_game(game_core)

