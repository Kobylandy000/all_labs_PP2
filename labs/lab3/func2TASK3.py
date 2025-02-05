import json
def connection():
    with open("data.json", "r") as file:
        movies = json.load(file)
        moviesList = movies["movies"]
        file.close()
    return moviesList

def moviesUnderCategory(category):
    subList = []
    for movie in connection():
        if movie["category"] == category:
            subList.append(movie)
    return subList

categories = ["Romance", "Thriller", "Suspense", "Comedy", "War", "Crime", "Adventure", "Drama", "Action"]
for i in range(len(categories)):
    print(i, categories[i])
index = int(input("PLEASE ENTER ID OF CATEGORY\t"))
print(moviesUnderCategory(categories[index]))