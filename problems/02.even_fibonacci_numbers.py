def say_hello():
    sum = 0
    fibonacci_seq = [1]

    current_index = 1
    next_term = 2
    while next_term < 4000000:
        if next_term % 2 == 0:
            sum += next_term
        fibonacci_seq.append(next_term)
        current_index += 1
        next_term = fibonacci_seq[current_index - 1] + fibonacci_seq[current_index - 2]

    return sum


print(say_hello())
