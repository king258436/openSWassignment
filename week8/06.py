from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


if __name__ == '__main__':
    print('선택 정렬을 수행합니다.')
    n = int(input("원소 수를 입력하세요. : "))
    x = [0]*n

    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))

    selection_sort(x)

    print('오름차순으로 정렬했습니다. ')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')
