H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
elif M < 45:
    if H == 0:
        print(23, (M+60-45))
    else:
        print(H-1, (M+60-45))