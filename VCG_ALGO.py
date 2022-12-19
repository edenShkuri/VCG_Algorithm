import itertools
import numpy as np


def get_all_options(n):
    items = np.arange(n)
    options = list(itertools.permutations(items))
    return options


def get_sum_of_options(options_list, vals):
    # print("VALS = \n", vals)
    sums = [0] * len(options_list)
    for opt_num, opt in enumerate(options_list):
        # print("opt = ", opt)
        # print("opt_num = ", opt_num)
        for player_i in range(len(opt)):
            # print("player_i = ", player_i)
            sums[opt_num] += vals[opt[player_i]][player_i]
    return sums


def print_best_option(sums, options_list):
    max_sum = max(sums)
    best_opt_indx = sums.index(max_sum)
    print("the best option is: ")
    opt = options_list[best_opt_indx]
    for player_i in range(len(opt)):
        print("player ", player_i + 1, " get item ", opt[player_i] + 1)
    return best_opt_indx


def calc_payment(sums, options, vals, chosen_opt_num, n):
    sums_without_players = np.zeros((n, len(sums)))
    for i in range(n):
        sums_without_players[i, :] = sums.copy()
    for player_num in range(n):
        for i in range(len(sums)):
            opt = options[i]
            sums_without_players[player_num][i] -= vals[opt[player_num]][player_num]
    pay_list = [0]*n
    for i in range(n):
        max_val = np.max(sums_without_players[i, :])
        max_val_indx = list(sums_without_players[i, :]).index(max_val)
        if max_val_indx != chosen_opt_num:
            pay_list[i] = sums_without_players[i, max_val_indx] - sums_without_players[i, chosen_opt_num]
    return pay_list


def calc_utility(chosen_opt_num, options, payment, vals, n):
    opt = options[chosen_opt_num]
    utility_list = [0]*n
    for i in range(n):
        utility_list[i] = vals[opt[i]][i] - payment[i]
    return utility_list


def print_(payment, utility, vals, n, opt):
    print("player--payment--value--utility")
    for i in range(n):
        print("  "+str(i+1)+"        "+str(payment[i])+"     "+str(vals[opt[i]][i])+"     "+str(utility[i]))


def test_n_2():
    # row - item number, cols - player number
    vals = [[5, 4], [9, 7]]  # for 2 players, 2 items
    n = 2
    options = get_all_options(n)
    sums = get_sum_of_options(options, vals)
    chosen_opt_num = print_best_option(sums, options)
    payment = calc_payment(sums, options, vals, chosen_opt_num, n)
    utility = calc_utility(chosen_opt_num, options, payment, vals, n)
    print_(payment, utility, vals, n, options[chosen_opt_num])


def test_n_3():
    # row - item number, cols - player number
    vals = [[5, 3, 7], [9, 8, 6], [4, 9, 1]]  # for 3 players, 3 items
    n = 3
    options = get_all_options(n)
    sums = get_sum_of_options(options, vals)
    chosen_opt_num = print_best_option(sums, options)
    payment = calc_payment(sums, options, vals, chosen_opt_num, n)
    utility = calc_utility(chosen_opt_num, options, payment, vals, n)
    print_(payment, utility, vals, n, options[chosen_opt_num])


def your_test(vals, n):
    options = get_all_options(n)
    sums = get_sum_of_options(options, vals)
    chosen_opt_num = print_best_option(sums, options)
    payment = calc_payment(sums, options, vals, chosen_opt_num, n)
    utility = calc_utility(chosen_opt_num, options, payment, vals, n)
    print_(payment, utility, vals, n, options[chosen_opt_num])


if __name__ == '__main__':
    test_n_2()
    print("*"*50)
    test_n_3()

    # vals = [[], []]  # row - item number, cols - player number
    # your_test(vals, n)

