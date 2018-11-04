def shingle(input, k):
    k = min(len(input), k)
    start_combinations = [input[:i] for i in range(1, k)]
    kgrams = [input[i:i + k] for i in range(len(input) - k + 1)]
    end_combinations = [input[-i:] for i in range(k - 1, 0, -1)]
    return start_combinations + kgrams + end_combinations

def two_ends(input, k):
    basic = shingle(input, k)
    result =[]
    for i in range(1, len(basic) + 1):
        if i <= (len(input) - i + 2):
            result.append(str(i) + basic[i - 1]) # Append numbers from start
        else:
            result.append(basic[i - 1] + str(len(basic) - i + 1)) # Append numbers from end
    return result
