def my_func(a, b, c):
    result = []
    counts = [a, b, c]
    for p in range(1, len(counts)):
        for i in range(1, len(counts)):
            max_count = max(counts)
            if counts[i] == max_count:
                result.append(max_count)
                counts.pop(i)

    return sum(result)


print(my_func(2, 5, 7))