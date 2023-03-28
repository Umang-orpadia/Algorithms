pattern = "abc"
string = "ababcabcabababd"


def brute_force_search(pattern, string):
    for i in range(len(string) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and pattern[j] == string[i+j]:
            j += 1
        if j == len(pattern):
            return i
    return -1
brute_force_search(pattern, string)

print(brute_force_search(pattern, string))
