# правило передачи аргументов
def order_of_args(name, default="go", *args, sep="separator", username, end="\n", **kwargs):
    print(name, default, args, username, end, sep, kwargs)
order_of_args("Behruz", 123, 4,5,6, username="apo", end="not enter", sep="not sep", email="e@com", loot = [2,3])

def arguments(*args, **kwargs):
    print(args, kwargs)
arguments(2,3,4,[5], user= {"name": "Ya"}, goal = ("win championship"))