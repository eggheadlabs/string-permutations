# How do you find all permutations of a string?
# Example: "xyz" ==> "xyz", "xzy", "yxz", "yzx", "zxy", "zyx"

def permutations(s, level=0):
    if level < len(s):
        for i in range(level, len(s)):
            s = list(s)
            s[level], s[i] = s[i], s[level]     # swap elements
            permutations(s, level+1)
    else:
        print(''.join(s))

s = "xyz"
print(permutations(s))