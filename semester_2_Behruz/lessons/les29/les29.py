def plus(num): 
    try: 
        return num + 5
    except ValueError as err: 
        return err

num = 1
isinstance (num, int) 


if __name__ == "__main__":
    print(plus(5))
    print(plus('5'))
    print(plus('a'))
    print(plus('-1'))


