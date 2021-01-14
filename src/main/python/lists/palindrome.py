def is_palindrome(s):
    start, end = 0, len(s) - 1

    while start <= end:
        if s[start] != s[end]:
            return False
        start, end = start + 1, end - 1
    return True

print(is_palindrome('racecar'))
print(is_palindrome('sameer'))