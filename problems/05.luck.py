def say_hello(k, contests):
    max_luck = 0

    contests = sorted(contests, key=lambda c: c[0], reverse=True)

    failed = 0
    for contest in contests:
        luck = contest[0]
        importance = contest[1]

        if importance == 0:
            max_luck += luck
        elif failed < k:
            max_luck += luck
            failed += 1
        else:
            max_luck -= luck

    return max_luck


print(say_hello(2, [[5, 1], [1, 1], [4, 0]]))
print(say_hello(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
