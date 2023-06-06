def max_berry_collection(berries):
    n = len(berries)
    if n == 0:
        return 0, -1

    dp = [0] * n
    dp[0] = berries[0]

    if n == 1:
        return dp[0], 0

    dp[1] = max(berries[0], berries[1])
    prev_prev_sum = berries[0]

    for i in range(2, n):
        dp[i] = max(dp[i-1], prev_prev_sum + berries[i])
        prev_prev_sum = max(prev_prev_sum, dp[i-2])

    max_collection = dp[-1]
    max_index = dp.index(max_collection)

    return max_collection, max_index


berries1 = [1, 2, 3, 4, 5, 6, 7, 8]
max_collection1, max_index1 = max_berry_collection(berries1)
print("Максимальное количество ягод:", max_collection1)
print("Собрано для куста номер:", max_index1)

berries2 = [11, 92, 1, 42, 15, 12, 11, 81]
max_collection2, max_index2 = max_berry_collection(berries2)
print("Максимальное количество ягод:", max_collection2)
print("Собрано для куста номер:", max_index2)
