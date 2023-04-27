from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1] , a[j] = a[j], a[j-1]
                last = j
        left = last

if __name__ == '__main__':
    print('셰이커 정렬을 수행합니다.')
    n = int(input("원소 수를 입력하세요. : "))
    x = [0]*n

    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))
    
    shaker_sort(x)

    print('오름차순으로 정렬했습니다. ')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')
