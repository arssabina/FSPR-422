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
   
import csv
with open('semester 2 ')



# ---------------------------------------  2-задание ---------------------------------------------
text_1 = """
I'm friends with the monster that's under my bed            
Get along with the voices inside of my head
You're trying to save me, stop holding your breath
And you think I'm crazy, yeah, you think I'm crazy

I wanted the fame, but not the cover of Newsweek
Oh well, guess beggers can't be choosey
Wanted to receive attention for my music
Wanted to be left alone in public, excuse me
Been wanting my cake, and eat it too, and wanting it both ways
Fame made me a balloon cause my ego inflated
When I blew see, it was confusing
Cause all I wanted to do is be the Bruce Lee of loose leaf
Abused ink, used it as a tool when I blew steam (wooh!)
Hit the lottery, oh wee
With what I gave up to get was bittersweet
It was like winning a huge meet
Ironic cause I think I'm getting so huge I need a shrink
I'm beginning to lose sleep: one sheep, two sheep
Going cucko and cooky as Kool Keith
But I'm actually weirder than you think
Cause I'm

I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're trying to save me, stop holding your breath
And you think I'm crazy, yeah, you think I'm crazy

Well, that's not fair
Well, that's not fair

Now I ain't much of a poet, but I know somebody once
Told me to seize the moment and don't squander it
Cause you never know when it all
Could be over tomorrow so I keep conjuring
Sometimes I wonder where these thoughts spawn from
(Yeah, ponder it. Do you wonder there's no wonder
You're losing your mind. The way you're brought up?)
Yo-lo-lo-lo-yee-whoo
I think you've been wandering off down yonder
And stumbled onto Jeff VanVonderen
Cause I need an interventionist
To intervene between me and this monster
And save me from myself and all this conflict
Cause the very thing that I love is killing me and I can't conquer it
My OCD is conking me in the head
Keep knocking, nobody's home, I'm sleepwalking
I'm just relaying what the voice in my head's saying
Don't shoot the messenger, I'm just friends with the

I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're trying to save me, stop holding your breath
And you think I'm crazy, yeah, you think I'm crazy

Well, that's not fair
Well, that's not fair

Call me crazy, but I had this vision
One day that I'd walk amongst you a regular civilian
But until then drums get killed I'm coming straight at
Emcees, blood get spilled and I
Take it back to the days that I get on a Dre track
Give every kid who got played that
Pumped the villian and shit that say back
To the kids who played 'em
I ain't here to save the f**king children
But if one kid out of a hundred million
Who are going through a struggle feels and relates that's great
It's payback, Russell Wilson falling way back
In the draft, turn nothing into something, still can make that
Straw into gold chump, I will spin Rumpelstiltskin in a hay stack
Maybe I need a straightjacket, face facts
I am nuts for real, but I'm okay with that
It's nothing, I'm still friends with the

I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're trying to save me, stop holding your breath
And you think I'm crazy, yeah, you think I'm crazy

I'm friends with the monste
r that's under my bed 
Get along with the voices inside of my head
You're trying to save me, stop holding your breath
And you think I'm crazy, yeah, you think I'm crazy

Well, that's not fair
Well, that's not fair"""

for word in text_1:
    if word == "monster" or "Monster":
        text_1=text_1.replace("monster", "***")
        counter=text_1.count("***")
print(text_1)
print("\nMonster count: " + str(counter))


# ---------------------------------------  3-задание ---------------------------------------------
message = input("\nWrite your message: ")
words = message.split(' ')
filtred=[]
counter=0

for word in words:
    if word == "my" or word=="My":
        counter += 1
        if counter > 3:
            break        
    filtred.append(word)


newmessage = ' '.join(filtred)
print("\nNew filtred message: " + newmessage)
