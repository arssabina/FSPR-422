print(__name__)

ITEMS = {
    "dog": 3,
    "cat": 2,
    "hamster": 5
}


def buy(animal): 
    for item, count in ITEMS.items():
        if item == animal and count:
            ITEMS[item] -= 1
            return animal
    return "We don't have this animal"

if __name__=="__main__":
    print(buy("cat"))
    print(buy("fish"))

