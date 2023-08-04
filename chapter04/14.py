# Problem: Money exchange

# A function that calculates sum of indexed element(s)
def sum_indexed_elements(arr, indices):
    S = 0
    for i in indices:
        S += arr[i]
    
    return S

# A function that prints indexed element(s)
def print_indexed(arr, indices):
    for i in indices:
        print(arr[i], end=' ')
    print()

# A function that exchanges money
result_ways = set()
def exchange_money(list_cash, total_money, indices = []):
    temp_sum = sum_indexed_elements(list_cash, indices)
    
    if temp_sum == total_money:
        tuple_indices = tuple(sorted(indices))
        # Consider [1 1 2] and [1 2 1] are the same
        if tuple_indices not in result_ways:
            print_indexed(list_cash, indices)
            result_ways.add(tuple_indices)

        return
    elif temp_sum > total_money:
        return
    
    for i in range(len(list_cash)):
        exchange_money(list_cash, total_money, indices + [i])

# Enter input
cash_inp = input('Enter a list of cash (each number is separated by a space): ')
total_money = int(input('Enter total money that you need to exchange: '))

list_cash = [int(e) for e in cash_inp.strip().split()]

# Print output
exchange_money(list_cash, total_money)