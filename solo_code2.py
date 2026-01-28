#create a Movie, 
# add Reviews to it, 
# and then report on its average rating, 
# best Review, 
# and worst Review.
import random

class movie:
    def __init__(self, title):
       self.movie_title = title 
       self.list_review = []

    def add_review(self, review):
        self.list_review.append(review)

    def average_rating(self):
        if len(self.list_review) == 0:
            return 0
        total = 0
        for r in self.list_review:
            total += r.rating
        return total / len(self.list_review)
    
    def best_review(self):
        max_rating = max(r.rating for r in self.list_review)
        best = [review for review in self.list_review if review.rating == max_rating]
        return random.choice(best)
    
    def worst_review(self):
        min_rating = min(r.rating for r in self.list_review)  # ✅ find the lowest rating
        worst = [r for r in self.list_review if r.rating == min_rating]  # ✅ filter reviews with that rating
        return random.choice(worst)     
    
    def list_reviews(self):
        for r in self.list_review:
            print(r)



class Review: 
    def __init__(self, rating, text):
        self.rating = rating
        self.text = text
    
    def __str__(self):
        return f"{self.rating}/5 - {self.text}"

my_movie = movie("Toy Story")
my_movie.add_review(Review(5, "The original and greatest of Pixars films!"))
my_movie.add_review(Review(5, "if you do not like toy story i do not know what to tell you"))
my_movie.add_review(Review(4, "Woody sets out to save Andy's new favorite Buzz Lightyear toy from a psychotic neighbor boy. This is a Pixar classic and one of their best."))
my_movie.add_review(Review(3, "I was hoping for a different plot line but it was like watching the same movie all over again. Otherwise it was funny and entertaining."))

print("Movie:", my_movie.movie_title)
print("Average Rating:", my_movie.average_rating())

print("\nAll Reviews:")
my_movie.list_reviews()

print("\nBest Review:")
print(my_movie.best_review())

print("\nWorst Review:")
print(my_movie.worst_review())