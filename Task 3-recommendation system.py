# Basic Book Recommendation System

books = [
    {"title": "Harry Potter", "genre": "Fantasy"},
    {"title": "The Hobbit", "genre": "Fantasy"},
    {"title": "The Alchemist", "genre": "Adventure"},
    {"title": "The Da Vinci Code", "genre": "Mystery"},
    {"title": "Sherlock Holmes", "genre": "Mystery"},
    {"title": "Atomic Habits", "genre": "Self Help"},
    {"title": "The Power of Now", "genre": "Self Help"},
    {"title": "Rich Dad Poor Dad", "genre": "Finance"},
    {"title": "The Psychology of Money", "genre": "Finance"},
    {"title": "The Fault in Our Stars", "genre": "Romance"}
]

print("===== BOOK RECOMMENDATION SYSTEM =====")

# Display available genres
print("\nAvailable Genres:")
genres = set(book["genre"] for book in books)

for genre in genres:
    print("-", genre)

# Take user's choice
choice = input("\nEnter your favorite genre: ")

# Find matching books
recommendations = []

for book in books:
    if book["genre"].lower() == choice.lower():
        recommendations.append(book["title"])

# Display recommendations
if recommendations:
    print("\nRecommended Books for You:")
    
    for book in recommendations:
        print("📖", book)
else:
    print("\nSorry, no books found for this genre.")