import datetime


def find_duplicate_values(d):
    for post in posts:
        pairs = post.items()
        for val in pairs:
            if isinstance(val, (str, dict)):
                print(val)
"""
dict_items([('tags', 'django,music'), ('title', 'Random title'), ('body', 'dasdsadasdsa')])
dict_items([('tags', 'django, hiking'), ('title', 'Random title'), ('body', 'dasdsadasdsa')])
dict_items([('tags', 'django,music'), ('title', 'Random title'), ('body', 'dasdsadasdsa'), ('published', datetime.date(2023, 5, 12))])
dict_items([('tags', 'django,music'), ('title', 'Random title'), ('body', 'dasdsadasdsa'), ('published', datetime.date(2023, 5, 11))])
dict_items([('tags', 'jazz'), ('title', 'Random title'), ('body', 'dasdsadasdsa')])
"""
    
       
        
posts = [
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
    {
        'tags': 'django, hiking',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 12),
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 11),
    },
    {
        'tags': 'jazz',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
]

        
find_duplicate_values(posts)

