# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you'll build a fully functional REST API using the FastAPI framework. You'll learn how to create endpoints, handle HTTP requests and responses, validate data, and interact with a simple database to manage resources.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI Application with GET Endpoints

#### Description
Set up a FastAPI application and create GET endpoints to retrieve data. You'll start with a simple in-memory data store of books and implement endpoints to get all books and retrieve a specific book by ID.

#### Requirements
Your application should:

- Initialize a FastAPI app with proper imports
- Define a Book model using Pydantic with at least `id`, `title`, `author`, and `year` fields
- Create an in-memory list of sample books (at least 3 books)
- Implement a GET endpoint at `/books` that returns all books
- Implement a GET endpoint at `/books/{book_id}` that returns a specific book by ID
- Return appropriate HTTP status codes (200 for success, 404 if book not found)

### 🛠️ Task 2: Implement POST and DELETE Endpoints

#### Description
Extend your API to support creating and deleting books. Users should be able to add new books to the collection and remove books by ID.

#### Requirements
Your application should:

- Implement a POST endpoint at `/books` that accepts a book title, author, and year
- Automatically generate unique IDs for new books
- Return the created book with a 201 status code
- Implement a DELETE endpoint at `/books/{book_id}` that removes a book by ID
- Return a confirmation message with 200 status for successful deletion
- Return a 404 error if attempting to delete a non-existent book
- Prevent duplicate book titles (optional: return 400 status if attempted)

### 🛠️ Task 3: Add Data Validation and Search Functionality

#### Description
Enhance your API with input validation and a search feature. Implement query parameters to filter books and validate that required fields are provided.

#### Requirements
Your application should:

- Use Pydantic models for request/response validation
- Add a search endpoint at `/books/search?query=` that filters books by title or author (partial matching)
- Implement a PUT endpoint at `/books/{book_id}` to update an existing book's information
- Validate that book title and author are non-empty strings
- Validate that year is a reasonable integer (e.g., 1000–current year)
- Return informative error messages for invalid requests (422 status)
- Test all endpoints manually using a tool like Postman, curl, or the built-in Swagger UI

### 🛠️ Task 4 (Stretch Goal): Persist Data with SQLite

#### Description
Connect your API to a SQLite database instead of using in-memory storage. This makes your API more realistic and persistent.

#### Requirements
Your application should:

- Set up a SQLite database connection (using sqlalchemy or sqlite3)
- Create a database table for books
- Replace in-memory list with database queries
- All previous endpoints should continue to work with database persistence
- Implement proper error handling for database operations
