num_q = int(input())

# 3
while num_q:

    first_line = input()  # 6 10
    x, y = first_line.split()  # ["6", "10"]
    x = int(x)
    y = int(y)

    smaller, bigger = min(x, y), max(x, y)
    dividers = []
    to_divide = 1

    # A,B의 최소공배수 * 최대공약수 = A*B

    for each in range(1, smaller+1):
        if smaller % each == 0:
            dividers.append(each)
    #print("dividers:", dividers)  # [1, 2, 3, 6]

    for d_each in reversed(dividers):
        if bigger % d_each == 0:
            gcd = d_each  # 2
            #print("lastly...:", gcd)
            break

    # 6 * 10 / 2
    print(int(smaller/gcd*bigger))

    num_q -= 1

