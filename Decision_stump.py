'''
https://coderun.yandex.ru/problem/stump?currentPage=1&pageSize=10&tag=first_2023_ml&rowNumber=6
'''

import sys
import numpy as np

def main():
    n = int(input())
    x_y_arr = []
    for i in range(n):
        line = input()
        line_int = [int(i) for i in line.split(' ')]
        x_y_arr.append(line_int)
    # print(x_y_arr)

    x_splits = [x_y_arr[i][0] for i in range(len(x_y_arr))]
    init_variance = np.var(np.array(x_y_arr).T[1])
    variance_reduction = []
    y_splited_arr = []
    best_c_index = 0
    for c in x_splits:
        split_1 = []
        split_2 = []
        for i in range(0, len(x_y_arr)):
            if x_y_arr[i][0] < c:
                split_1.append(x_y_arr[i][1])
            else:
                split_2.append(x_y_arr[i][1])
        y_splited_arr.append([split_1, split_2])
        if len(split_1) == 0:
            var_1 = 0
        else:
            var_1 = np.var(split_1)
        if len(split_2) == 0:
            var_2 = 0
        else:
            var_2 = np.var(split_2)
        var_reduction = init_variance - ((len(split_1) / len(x_y_arr)) * var_1 + (len(split_2) / len(x_y_arr)) * var_2)
        variance_reduction.append(var_reduction)
    best_c_index = np.argmax(variance_reduction)
    best_split = y_splited_arr[best_c_index]
    c = x_splits[best_c_index]
    a = np.mean(best_split[0])
    b = np.mean(best_split[1])

    print(a, b, c)

if __name__ == '__main__':
    main()