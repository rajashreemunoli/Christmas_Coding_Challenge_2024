#13 Roman to Integer
def romanToInt(s):
    roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

    result=0

    for i, char in enumerate(s):
        if (i<len(s)-1 and roman[char]<roman[s[i+1]]):
            result-=roman[char]
        else:
            result+=roman[char]
    return result


print(romanToInt("MCMXCIV"))