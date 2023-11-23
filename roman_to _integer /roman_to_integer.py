def romanToInt(s):
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = []
    for i in s[::-1]:
        if len(res) == 0 or res[-1] <= d[i]:
            res.append(d[i])
        else:
            res[-1] -= d[i]
    return sum(res[::-1])

print(romanToInt('MCMXCIV'))