# Personal Library Management API

This is a RESTful API developed using Django and Django REST Framework for managing a personal library system. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on their personal library of books. Each book entry contains information such as title, authors, publication date, ISBN, and a short description.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run migrations to create necessary database tables:**

    ```bash
    python manage.py migrate
    ```

2. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

3. **Access the API endpoints through your web browser or a REST client like Postman.**

## API Endpoints

- **List Books**: `GET /api/books/`

  Returns a list of all books in the library.

- **Add Book**: `POST /api/books/`

  Allows adding a new book to the library. All book details must be provided, except for the optional ones.

- **Book Details**: `GET /api/books/<isbn>/`

  Retrieves the details of a book identified by its ISBN.

- **Update Book**: `PUT /api/books/<isbn>/`

  Updates the details of a specific book. All book details must be provided, as this is a complete update.

- **Delete Book**: `DELETE /api/books/<isbn>/`

  Deletes a specific book from the library.

## Models

The following model is used for book representation:

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publication_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True)
