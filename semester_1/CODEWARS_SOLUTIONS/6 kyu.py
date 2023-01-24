def solution(n):
    result=[]
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return result

print(solution(6))

# ----------------------------------------------------------------------------

# https://www.codewars.com/kata/5264d2b162488dc400000001/solutions/python

def spin_words(s):
    new_s=[]
    for word in s.split(): 
        if len(word) >=5:
           new_s.append(word[::-1])
        else: 
            new_s.append(word)
    result=" ".join(new_s)
    return result

print (spin_words("Hey fellow warriors"))

# best solution: 

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])\

def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
    

# --------------------------------------------------------------------------------------------
def digital_root(n):
    for num in str(n):
        sums=sum(list(int(num)))
    return sums

# print(digital_root(467)) ??????????????????????

# ============================================================================

