
def romanToInt(s: str) -> int:
    values = {
        "I":              1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000}
    
    sum_ = values[s[0]]
    for i in range(1, len(s)):
        sum_ += values[s[i]]
        if values[s[i]] > values[s[i-1]]:
            sum_ -= values[s[i-1]] * 2
    return sum_


# print(romanToInt("III"))
# # print(romanToInt("IIV"))
# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))