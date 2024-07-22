# First API Rest basic example

This project is an API built using Python and FastAPI, designed to handle CRUD operations for a resource called "movie". Additionally, it includes a basic example of authentication using JWT (JSON Web Tokens). The database management system employed is SQLite, integrated with SQLAlchemy for data manipulation.

## Features

-   **CRUD Operations**: The API supports Create, Read, Update, and Delete (CRUD) operations for movie resources. Users can perform actions like adding a new movie, retrieving movie details, updating existing movie information, and deleting movies from the database.

-   **Authentication with JWT**: The project implements a simple authentication mechanism using JWT. Users can obtain a token by providing valid credentials, which they can then use to access protected endpoints for managing movie data.

## Example endpoints

-   `/movies/`: Endpoint for listing all movies or creating a new movie.
-   `/movies/{id}/`: Endpoint for retrieving, updating, or deleting a specific movie by its ID.
-   `/movies?category={category_name}`: Endpoint for listing movies filtered by category. Users can specify the category name as a parameter to retrieve movies belonging to that category.
-   `/login/`: Endpoint for obtaining a JWT token by providing valid credentials.

## What i leraned

Coming soon...

## Usage

Coming soon...
