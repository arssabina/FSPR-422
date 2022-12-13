def get_user_info(name, clan="Trident", *args, **kwargs):
    if args and kwargs:
        args="".join([f"\n- {arg}" for arg in args]) 
        kwargs="".join([f"\n- {key}: {value}" for key, value in kwargs.items()])
        return f"Your name is {name} and your clan is {clan}. Other information:{args}.\n\n Key skills: {kwargs}"
    else: 
        return f"Your name is {name} and your clan is {clan}."

print(get_user_info("Behruz"))
print(get_user_info("Behruz", "Shunko"))
print(get_user_info("Behruz", "Shunko", 'sonic speed', 'lightning', 'programming',  db="SQL"))

