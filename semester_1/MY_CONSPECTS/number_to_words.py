# =================================from 1 to 1000===============================================

n=int(input("Enter number:"))
first_digit=n//100              # к примеру число 356//100=3,56   берём целое число 3
last_digit=n%10                 # 356//10=35.6  берём остаток от деления 6  
middle_digit=n//10              # 356//10=35,6 нужно целое число 35, которое мы еще поделим чтобы получить остаток от деления
second_digit=middle_digit%10    # 35//10=3,5  берём остаток от деления 5, это у нас десяток числа, которе мы задали
# print(first_digit, last_digit)
from_one_to_twenty=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades=['none', 'ten','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred=['hundred']
if n<20:
    result=from_one_to_twenty[n]
    print(result)
if n<100:
    result=decades[middle_digit] +" " + from_one_to_twenty[last_digit]
    print(result)
if n>100:
    result=from_one_to_twenty[first_digit] + " " + hundred[0] +  " " + decades [second_digit] + " " + from_one_to_twenty[last_digit] 
    print(result)
if n>999:
    break
    print("Your number is thousandths")


# ========================from 1 to 99 =============================================
n=int(input("Enter number:"))
first_digit=n//10
last_digit=n%10
# print(first_digit, last_digit)
from_one_to_twenty=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades=['none', 'ten','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
if n<1 or n>=100:
    print("invalide input")
if n<20:
    result=from_one_to_twenty[n]
    print(result)
if n>20:
    result=decades[first_digit] +" " + from_one_to_twenty[last_digit]
    print(result)