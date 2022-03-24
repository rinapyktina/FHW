if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = [int(i) for i in f]

    count = 0
    max_sum = 0
    for i in range(len(a)):
        if i != len(a) - 2:
            x = max(a[i], a[i + 1], a[i + 2]) * max(a[i], a[i + 1], a[i + 2])
            y = a[i] + a[i + 1] + a[i + 2] - min(a[i], a[i + 1], a[i + 2]) - max(a[i], a[i + 1], a[i + 2])
            z = min(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2]) + y * y
            if x == z:
                count += 1
                max_sum = max(max_sum, a[i] + a[i + 1] + a[i + 2])
        else:
            break

    print(count, max_sum)