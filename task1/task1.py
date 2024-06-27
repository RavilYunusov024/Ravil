from itertools import cycle

if __name__ == '__main__':
    n, m = input().split()
    array_cycle = cycle([x for x in range(1, int(n) + 1)])
    count = 1
    result = '1'
    next_item = next(array_cycle)
    while True:
        count += 1
        num = next(array_cycle)
        if num == 1 and count % int(m) == 0:
            break
        elif count == int(m) and num != 1:
            count = 1
            result += str(num)
    print(result)