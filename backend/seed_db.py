from database import SessionLocal
import models

def seed():
    db = SessionLocal()
    
    # Check if books already exist to avoid duplicates
    if db.query(models.Book).count() > 0:
        print("Database already contains data. Skipping seeding.")
        db.close()
        return

    sample_books = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "description": "A story of wealth, love, and the American Dream in the 1920s."
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "description": "A classic novel exploring racial injustice and the loss of innocence in the American South."
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "description": "A dystopian masterpiece about surveillance, totalitarianism, and the power of truth."
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "description": "An adventurous tale of Bilbo Baggins and his journey to the Lonely Mountain."
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "description": "A romantic comedy of manners in 19th-century England."
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "description": "A coming-of-age story about Holden Caulfield's experiences in New York City."
        },
        {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "description": "A visionary novel about a future society dominated by technology and pleasure."
        }
    ]

    for book_data in sample_books:
        book = models.Book(**book_data)
        db.add(book)
    
    db.commit()
    print(f"Successfully seeded {len(sample_books)} books!")
    db.close()

if __name__ == "__main__":
    seed()
