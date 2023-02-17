results=[]
right_answers=0
wrong_answers=0
no_answers=0
points=0

answer_1=input("Is 2+2=4? (answer 'yes' , 'no' or 'nothing'(if you don't know')")
if answer_1 == "yes":
    results.append("right")
    right_answers +=1
    points +=1
if answer_1 == "no":
    results.append("wrong")
    wrong_answers +=1
    points -=0.25
if answer_1 == "nothing":
    no_answers +=1
    points +=0
    results.append("no answer")

answer_2=input("Is 3*3=10? (answer 'yes' , 'no' or 'nothing'(if you don't know')")
if answer_2 == "yes":
    results.append("wrong")
    wrong_answers +=1
    points -=0.25
if answer_2 == "no":
    results.append("right")
    right_answers +=1
    points +=1
if answer_2 == "nothing":
    results.append("no_answer")
    no_answers +=1
    points +=0

answer_3=input("Is 5*5=25? (answer 'yes' , 'no' or 'nothing'(if you don't know')")
if answer_3 == "yes":
    results.append("right")
    right_answers +=1
    points +=1
if answer_3 == "no":
    results.append("wrong")
    wrong_answers +=1
    points -=0.25
if answer_3 == "nothing":
    results.append("no_answer")
    no_answers +=1
    points +=0

answer_4=input("Is 20+20=40? (answer 'yes' , 'no' or 'nothing'(if you don't know')")
if answer_4 == "yes":
    results.append("right")
    right_answers +=1
    points +=1
if answer_4 == "no":
    results.append("wrong")
    wrong_answers +=1
    points -=0.25
if answer_1 == "nothing":
    results.append("no_answer")
    no_answers +=1
    points +=0

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)
print("\nRight answers: " + str(right_answers))
print("Wrong answers: " + str(wrong_answers))
print("No_answers: " + str(no_answers))
print("Your points: " + str(points))
if right_answers == 4:
    print("\nYou passed the test. Your GPA is: " + str(right_answers/4*100) + " %")
if 2 <= right_answers <= 3 :
    print("\nYou passed the test. Your GPA is: " + str(right_answers/4*100) + " %")
if right_answers <= 1:
    print("\nYou didn't pass the test. Your GPA is: " + str(right_answers/4*100) + " %")

print("\nYour answers:")
print("1 - " + results[0])
print("2 - " + results[1])
print("3 - " + results[2])
print("4 - " + results[3])







    

