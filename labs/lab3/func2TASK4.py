import json
def connection():
    with open("data.json", "r") as file:
        movies = json.load(file)
        moviesList = movies["movies"]
        file.close()
    return moviesList

def avg(movies):
    sum = 0
    count = 0
    for movie in movies:
        sum += movie["imdb"]
        count += 1
    print(sum / count)

avg(connection())