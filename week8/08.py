from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n//2
    while h >0:
        for i in range(h,n):
            j = i-h
            tmp = a[i]
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h//=2

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    n = int(input("원소 수를 입력하세요. : "))
    x = [0]*n

    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))
    
    shell_sort(x)

    print('오름차순으로 정렬했습니다. ')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')
