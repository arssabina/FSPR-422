def shades_of_grey(n):
    shades=[]
    hex="123456789abcdef"
    counter=0
    for i in range(n): # n =20
        if counter ==15:
            counter=0
        grey=f"#0{hex[counter]}0{hex[counter]}0{hex[counter]}"
        if i >=15:
            grey = f"#1{hex[counter]}1{hex[counter]}1{hex[counter]}"
        shades.append(grey)
        counter +=1
    return shades
print(shades_of_grey(50))

# Написать функцию, которая принимает два аргумента: n и num - и на основе них, создает список. 
# n для определения длины списка. num умножить на все значения в списке. Значениями списка могут быть числа, 
# которые вы получаете из цикла

# def multiply (n, num):
#     result=[]
#     for i in range(n):
#         result.append(i*num)
#     return result
# print(multiply(20,1))
# print(multiply(10,4))

def func(a, default = "hi"):
    print(a, default)

# func(12)
# func(12, "not hi")

def func (a,b,default = "hi"):
    print("a=", a, "b=", b, default)

func(12,4)
func(b=12, a=4)
func(12,5, "not hi")

#арги
def func (a,b, default = "hi", *args):
    print(a,b, "default=", default, "args=", args)

func(12,4, "yeeee", 3,4, [2,3,4])

def any_arg (*args):
    """Функция которая принимает любое кол-во аргументов и выводит их на экран"""
    print("args = ", args) 
    for arg in args: 
        print(arg)

any_arg (2,3,4, "goooo", "nooooo", {1:1}, [], {3,4,5})
any_arg()

