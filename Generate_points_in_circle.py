'''
Петя написал два генератора точек в круге:

Даны 100 наборов по 1000 точек, каждый набор сгенерирован каким-то одним из этих двух алгоритмов. Необходимо определить для каждого набора, первый или второй алгоритм использовался для его генерации.

Для того, чтобы получить ОК по этой задаче, надо предсказать правильный генератор хотя бы для 98 наборов.
Формат ввода

Даны 100 строк. Каждая строка отвечает за свой набор точек.

В каждой строке находится 2000 действительных чисел (−1≤ai≤1−1≤ai​≤1), разделённых пробелом. Точки идут подряд, то есть формат строки: x0x0​ y0y0​ x1x1​ y1y1​ x2x2​ y2y2​ ... x999x999​ y999y999​
Формат вывода

Нужно вывести 100 строк, в каждой из которой должно быть 1 число: 1 или 2, в зависимости от того, первым или вторым генератором был сгенерирован данный набор точек.
'''

import numpy as np
import sys

# def get_list_of_answers():
#     file_no_target = open("/home/opv002/py_notes/git_repos/ML_trainings/data/points_in_circle_data_no_target.txt", "r")
#     lines_no_target = []
#     for line in file_no_target.readlines():
#         line_float = [float(i) for i in line.split(' ')]
#         lines_no_target.append(line_float)

#     # lines_no_target = []
#     # for i in range(100):
#     #     line = input()
#     #     line_float = [float(i) for i in line.split(' ')]
#     #     lines_no_target.append(line_float)

#     sets_arr_no_target = []
#     for line in lines_no_target:
#         x_arr = [0] * (len(line) // 2)
#         y_arr = [0] * (len(line) // 2)
#         for i in range(0, len(line)):
#             if i % 2 == 0:
#                 x_arr[i // 2] = line[i]
#             else:
#                 y_arr[i // 2] = line[i]
#         sets_arr_no_target.append([x_arr, y_arr])

#     ans_list_no_target = [0] * len(sets_arr_no_target)
#     for i in range(0, len(sets_arr_no_target)):
#         x2_plus_y2 = np.array(sets_arr_no_target[i][1])**2 + np.array(sets_arr_no_target[i][0])**2
#         is_in_mean = (x2_plus_y2 <= 1/np.sqrt(2)).mean()
#         if is_in_mean <= 0.7:
#             ans_list_no_target[i] = 2
#         else:
#             ans_list_no_target[i] = 1
    
#     return ans_list_no_target

# ans = get_list_of_answers()
# for a in ans:
#     print(a)

# # lines_no_target = []
# # for i in range(1):
# #     line = input()
# #     line_float = [float(i) for i in line.split(' ')]
# #     lines_no_target.append(line_float)

# # print(lines_no_target)


def main():
    file_no_target = open("/home/opv002/py_notes/git_repos/ML_trainings/data/points_in_circle_data_no_target.txt", "r")
    lines_no_target = []
    for line in file_no_target.readlines():
        line_float = [float(i) for i in line.split(' ')]
        lines_no_target.append(line_float)

    # lines_no_target = []
    # for i in range(100):
    #     line = input()
    #     line_float = [float(i) for i in line.split(' ')]
    #     lines_no_target.append(line_float)

    sets_arr_no_target = []
    for line in lines_no_target:
        x_arr = [0] * (len(line) // 2)
        y_arr = [0] * (len(line) // 2)
        for i in range(0, len(line)):
            if i % 2 == 0:
                x_arr[i // 2] = line[i]
            else:
                y_arr[i // 2] = line[i]
        sets_arr_no_target.append([x_arr, y_arr])

    ans_list_no_target = [0] * len(sets_arr_no_target)
    for i in range(0, len(sets_arr_no_target)):
        x2_plus_y2 = np.array(sets_arr_no_target[i][1])**2 + np.array(sets_arr_no_target[i][0])**2
        is_in_mean = (x2_plus_y2 <= 1/np.sqrt(2)).mean()
        if is_in_mean <= 0.7:
            ans_list_no_target[i] = 2
        else:
            ans_list_no_target[i] = 1
    
    for a in ans_list_no_target:
        print(a)

if __name__ == '__main__':
    main()

    

