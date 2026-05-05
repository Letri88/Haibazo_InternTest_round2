from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware to allow the React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        if db.query(models.Book).count() == 0:
            sample_books = [
                {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A story of wealth, love, and the American Dream in the 1920s."},
                {"title": "To Kill a Mockingbird", "author": "Harper Lee", "description": "A classic novel exploring racial injustice and the loss of innocence."},
                {"title": "1984", "author": "George Orwell", "description": "A dystopian masterpiece about surveillance and totalitarianism."},
                {"title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "An adventurous tale of Bilbo Baggins and his journey."},
                {"title": "Pride and Prejudice", "author": "Jane Austen", "description": "A romantic comedy of manners in 19th-century England."},
            ]
            for book_data in sample_books:
                db.add(models.Book(**book_data))
            db.commit()
    finally:
        db.close()

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Compatible with both Pydantic v1 and v2
    book_data = book.model_dump() if hasattr(book, "model_dump") else book.dict()
    new_book = models.Book(**book_data)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=44, detail="Book not found")
    return book