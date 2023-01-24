# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
# Examples input/output:
# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# My solution: 
def xo(s):
    s=s.lower()
    oxes=s.count("o")
    exes=s.count("x")   
    if oxes==exes:
        return True

print(xo("ooxXm"))

# Better solutions:
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo("ooxXm"))
# =========================================

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

print(xo("ooxXm"))

# =======================================================
# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
# Jaden Casing Strings
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
def to_jaden_case(string):
    new_str=string.split()   # -> ['How', 'can', 'mirrors', 'be', 'real', 'if', 'our', 'eyes', "aren't", 'real']
    result=[]
    for word in (new_str):
        result.append(word.capitalize()) # -> ['How', 'Can', 'Mirrors', 'Be', 'Real', 'If', 'Our', 'Eyes', "Aren't", 'Real']
    return " ".join(result)  # Output:   How Can Mirrors Be Real If Our Eyes Aren't Real
  
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# Better solutions: 
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
