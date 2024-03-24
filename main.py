import timeit
from prettytable import PrettyTable

DENOMINATIONS = [50, 25, 10, 5, 2, 1]


# Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins_used = {}

    for coin in DENOMINATIONS:
        count = amount // coin
        if count > 0:
            coins_used[coin] = count
            amount -= count * coin

    return coins_used


# Функція динамічного програмування
def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in DENOMINATIONS:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


if __name__ == "__main__":
    table = PrettyTable()
    table.field_names = ["Amount", "Greedy Algorithm Time", "Greedy Algorithm Result", "Amount of coins (greedy)"
                         ,"Dynamic Programming Algorithm Time", "Dynamic Programming Algorithm Result", "Amount of coins (dynamic)"]

    # Порівняння ефективності
    amounts_to_test = [57, 1013, 9995, 54544, 100142]

    for amount in amounts_to_test:
        # Вимірювання часу для find_coins_greedy та отримання результату
        greedy_time = timeit.timeit("find_coins_greedy({})".format(
            amount), globals=globals(), number=200)
        greedy_result = find_coins_greedy(amount)

        # Вимірювання часу для find_min_coins та отримання результату
        dp_time = timeit.timeit("find_min_coins({})".format(
            amount), globals=globals(), number=200)
        dp_result = find_min_coins(amount)

        # Додавання рядка до таблиці
        table.add_row([amount, round(greedy_time, 6), greedy_result, sum(greedy_result.values()), round(dp_time, 6), dp_result, sum(dp_result.values())])

    # Виведення результатів
    print(table)

    DENOMINATIONS = [4,3,1]
    table.clear_rows()
    
    amounts_to_test = [50, 66, 5002, 100002]

    #тести для неканонічного набору монет
    for amount in amounts_to_test:
        # Вимірювання часу для find_coins_greedy та отримання результату
        greedy_time = timeit.timeit("find_coins_greedy({})".format(
            amount), globals=globals(), number=200)
        greedy_result = find_coins_greedy(amount)

        # Вимірювання часу для find_min_coins та отримання результату
        dp_time = timeit.timeit("find_min_coins({})".format(
            amount), globals=globals(), number=200)
        dp_result = find_min_coins(amount)

        # Додавання рядка до таблиці
        table.add_row([amount, round(greedy_time, 8), greedy_result, sum(greedy_result.values()), round(dp_time, 6), dp_result, sum(dp_result.values())])

    # Виведення результатів
    print(table)