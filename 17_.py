if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = [int(i) for i in f]

    count = 0
    max_sum = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % 120 == 0:
                count += 1
                max_sum = max(max_sum, a[i] + a[j])

    print(count, max_sum)