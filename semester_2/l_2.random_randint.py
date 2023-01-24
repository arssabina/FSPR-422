import random 

counter=0
start=0
money=0
tries=20

x=random.randint(0,100)
print("\nGuess the infinite number")

while start <tries:
    number=int(input("Enter your number: "))
    start += 1

    if number < x: 
        counter +=1
        print("Enter number greater than this")
    if number > x: 
        counter +=1
        print("Enter number smaller than this")
    if number == x: 
        counter +=1
        print("\nYou find the random number. It's " + str(x))
        break
    
print(number)
print ("\nYour number of attempts: " + str(counter))

if counter == 1:
    money += 1000000 
    print("You won " + str(money) + " $")
if counter == 2: 
    money += 350 
    print("You won " + str(money) + " $")
if counter == 3:
    money += 300
    print("You won " + str(money) + "$")
if counter == 4:
    money += 200
    print("You won " + str(money) + " $")
if counter == 5:
    money += 100
    print("You won " + str(money) + " $")
if counter == 6:
    money +=0
    print("You didn't win anything " + str(money) + " $")
if counter > 6:
    money_number = counter-6
    print("\nYour number of attempts is more than 6, you lose. Your dubt is " +  "-" + str(money_number*100) + " $")
   


