def longest_substring(word):
    left, right, length = 0, 1, 0
    while word[left] == word[right]:
        right += 1
        left += 1
    for i in range(right, len(word)):
        if word[left] != word[right]:
            right += 1
            length = max((right - left + 1), length)
        else:
            left += 1

    return length


if __name__ == '__main__':
    print(longest_substring('aaaaaaaaaaaabcabcdabcdeabab'))  #
