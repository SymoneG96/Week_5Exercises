#List of fav movies
favorite_movies = ["The Butterfly Affect", "Inception", "The Freedom Writers Diary", "Friday", "Shrek"]

#Use the len() function to print the descriptive statement:
print(f"The list 'favorite_movies' includes my top {len(favorite_movies)} favorite movies.")
print(favorite_movies)

#Sorted list printed in two ways 
print(sorted(favorite_movies))
print(favorite_movies)

#The sorted() function creates a new sorted list, while the original favorite_movies list remains unchanged.

favorite_movies.sort()
print(favorite_movies)

#The .sort() method sorts the list in-place, so the original favorite_movies list is now sorted.

#Added movie
favorite_movies.append("The Godfather")
print(f"The list 'favorite_movies' includes my top {len(favorite_movies)} favorite movies.")
print(favorite_movies)

