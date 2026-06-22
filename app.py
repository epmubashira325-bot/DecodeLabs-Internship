movies = {
    "Avengers": ["Action", "Sci-Fi"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "John Wick": ["Action", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "The Conjuring": ["Horror", "Thriller"],
    "Avatar": ["Action", "Sci-Fi"],
    "The Notebook": ["Romance", "Drama"]
}

user_input = input("Enter your favorite genres (comma separated): ")

user_preferences = [genre.strip().title() for genre in user_input.split(",")]

recommendations = []

for movie, genres in movies.items():
    score = 0

    for preference in user_preferences:
        if preference in genres:
            score += 1

    if score > 0:
        recommendations.append((movie, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Movies:")

if recommendations:
    for movie, score in recommendations:
        print(f"{movie} - Match Score: {score}")
else:
    print("No recommendations found.")