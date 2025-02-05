import json

def above5p5(movie):
    if movie["imdb"] > 5.5:
        return True
    return False

def connection():
    with open("data.json", "r") as file:
        movies = json.load(file)
        moviesList = movies["movies"]
        file.close()
    return moviesList

moviesList = connection()
for movie in moviesList:
    print(above5p5(movie))