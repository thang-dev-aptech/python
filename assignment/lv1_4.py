def count_ch(text):
    result = {}

    for ch in text:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result

print(count_ch("banana"))