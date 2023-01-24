"""
8-6. Названия городов: напишите функцию city_country(), которая получает название города и страну. Функция должна 
возвращать строку в формате “Santiago, Chile”. Вызовите свою функцию по крайней мере для трех пар 
«город—страна» и выведите возвращенное 
значение."""

def city_country(city_name, country_name):
    """Возвращаемое значение (The value the function returns is called a return value.)"""
    full_info= city_name + ", " + country_name
    return full_info

info=city_country("Santiago", "Chile")
print(info)

info=city_country("Tashkent", "Uzbekistan")
print(info)

info=city_country("Stambul", "Turkey")
print(info)

""" 
8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Add an optional parameter to make_album() that allows you to store the 
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the 
album’s dictionary. Make at least one new function call that includes the number of tracks on an album"""

def make_album(atrist_name, album_title, number_of_tracks=""):
    """Return a dictionary of information about an album."""
    info={"artist" : atrist_name, "album" : album_title}
    if number_of_tracks:
        info['number of tracks'] = number_of_tracks
    return info

album=make_album("Tohir Sodiqov", "Kerak emas")
print(album)

album=make_album("Deep Forest", "Boheme", number_of_tracks=12)
print(album)

info=make_album("Leo Rohas", "Colors of Nature", 14)
print (info)

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created. Be sure to include a quit value in the while loop."""

# ========================================================================
def make_album(artist_name, album_title, tracks_number):
    full_info="Artist name: " + artist_name.title() + ", Album: " + album_title.title() + ", Tracks number: " + tracks_number
    return full_info.title()

while True: 
    print("\nEnter an info , please")
    print("(For quit, please enter 'q')")

    artist=input("Enter an artist name:")
    if artist == "q":
        break
    album=input("Enter an album name:")
    if album == "q":
        break
    tracks=input("Enter number of tracks:")
    if tracks == "q":
        break
    
info=make_album(artist, album, tracks)
print (info)
