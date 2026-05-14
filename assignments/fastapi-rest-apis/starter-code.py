"""
FastAPI REST API Assignment - Starter Code

This is a template for building a REST API with FastAPI.
Complete the tasks by implementing the required endpoints.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI app
app = FastAPI(
    title="Book API",
    description="A simple REST API for managing a book collection",
    version="1.0.0"
)

# Define the Book model for data validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# In-memory data store (replace with database in Task 4)
books_db: List[Book] = [
    Book(id=1, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=2, title="1984", author="George Orwell", year=1949),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
]

# Track the next ID for new books
next_id = 4

# TODO: Implement all endpoints below
# Task 1: GET /books - Return all books
# Task 1: GET /books/{book_id} - Return a specific book
# Task 2: POST /books - Create a new book
# Task 2: DELETE /books/{book_id} - Delete a book
# Task 3: PUT /books/{book_id} - Update a book
# Task 3: GET /books/search - Search for books by title or author
# Task 4: Replace in-memory storage with SQLite (optional)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
