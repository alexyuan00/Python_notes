print("This is for Github test")

def type_of_album(artist, album, year_released):

    print(artist, album, year_released)
    if year_released > 2000:
        return "Modern"
    else:
        return "Oldie"
x= type_of_album("Taylor Swift", "Red", 2012)
print(x)

