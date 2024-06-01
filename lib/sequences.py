def print_fibonacci(n):
    if n == 0:
        print([])
    elif n == 1:
        print([0])
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        print(sequence)