for _ in range(int(input())):
    N=int(input())
    S=input()
    if "I" in S:
        print("INDIAN")
    elif "I" not in S:
        if "Y" not in S:
            print("NOT SURE")
        elif "Y" in S:
            print("NOT INDIAN")