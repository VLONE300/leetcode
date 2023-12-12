def longest_common_prefix(strs):
    if '' in strs:
        return ''
    elif len(strs) == 1:
        return strs[0]
    c = 0
    res = [i[:c] for i in strs]
    while len(set(res)) == 1:
        if res == strs:
            return strs[0]
        c += 1
        res = [i[:c] for i in strs]
    return res[0][:c - 1]


print(longest_common_prefix(["flower", "flow", "flight"]))
