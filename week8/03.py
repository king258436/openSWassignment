from typing import MutableSequence


def bubble_sort_verbose(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    for i in range(n-1):
        exchng = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
        if exchng == 0:
            break


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    n = int(input("원소 수를 입력하세요. : "))
    x = [0]*n

    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))

    bubble_sort_verbose(x)

    print('오름차순으로 정렬했습니다. ')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')
