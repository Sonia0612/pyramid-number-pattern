
#using while function
def while_func(n):
    i = 1
    while i <= n:
        spaces = 1
        while spaces <= n - i:
            print(" ", end='')
            spaces = spaces + 1
        j = i
        while j >= 1:
            print(j, end='')
            j = j - 1
        p = 1
        k = 2
        p = i - 1
        while p >= 1:
            print(k, end='')
            p = p - 1
            k = k + 1
        print()
        i = i + 1


n=int(input())
while_func(n)

