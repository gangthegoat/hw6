def print_gugudan(start, end):
    for i in range(1, 10):  # 각 단의 곱 (1~9)
        for dan in range(start, end + 1):  # 단의 범위 (2~5, 6~9)
            print(f"{dan} x {i} = {dan*i:2}", end="\t")
        print()  # 줄 바꿈

print_gugudan(2, 5)

print()  

print_gugudan(6, 9)