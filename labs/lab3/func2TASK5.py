import json
def connection():
    with open("data.json", "r") as file:
        movies = json.load(file)
        moviesList = movies["movies"]
        file.close()
    return moviesList

def avgByCategory(category):
    sum = 0
    count = 0
    for movie in connection():
        if movie["category"] == category:
            sum += movie["imdb"]
            count += 1
    print(sum/count)


categories = ["Romance", "Thriller", "Suspense", "Comedy", "War", "Crime", "Adventure", "Drama", "Action"]
for i in range(len(categories)):
    print(i, categories[i])
index = int(input("PLEASE ENTER ID OF CATEGORY\t"))
avgByCategory(categories[index])