while 1:
    n = input()
    if n == "":
        break
    n = int(n)
    s = []
    target = [0] + list(map(int, input().split()))
    A, B, ok = 1, 1, 1
    while B <= n:
        if A == target[B]:
            A += 1
            B += 1
        elif len(s) != 0 and s[-1] == target[B]:
            s.pop(-1)
            B += 1
        elif A <= n:
            A += 1
            s.append(A)
        else:
            ok = 0
            break
    if ok == 1:
        print("Yes")
    else:
        print("No")