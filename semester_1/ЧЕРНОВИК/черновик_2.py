def greet_user(names):
    for name in names:
        message="Hello, " + name.title() + "!"
        print(message)

names=['Farina', 'Tamina', 'Hanifa']
greet_user(names) 


unprinted_designs=['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design) 
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for model in completed_models:
    print("\t" + model)



def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for model in completed_models:
        print("\n We have been printed the following models: ")
        print("\t" + model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



