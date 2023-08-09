# Todo List API

This repository holds the Todo List API, a fully-featured CRUD (Create, Retrieve, Update, Delete) API for maintaining a Todo list, with additional options for listing completed and deleted tasks.
The application is developed using FastAPI and uses PostgreSQL as its database backend. The API is containerized using Docker, which means it can be easily set up and run on any system with Docker installed. The repository also includes a comprehensive suite of tests that can be run inside the Docker container.

## Features
- Full CRUD API for Todos.
- Listing of completed and deleted tasks.
- Test suite.
- Automated API documentation via FastAPI's Swagger UI.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) (or just [Docker Desktop](https://www.docker.com/products/docker-desktop/))

## Running the Application

To run the Todo List API, follow these steps:


```
# Clone the repository
git clone https://github.com/tntath/todo-app-fastapi.git

# Navigate into the directory
cd todo-app-fastapi

# Start the Docker containers
docker-compose up -d
```
## API Documentation

Once the Docker containers are up and running, you can visit the Swagger UI to interact with the API: [http://localhost:8000/docs](http://localhost:8000/docs)

It is automatically generated by the FastAPI framework and includes API documentation and input validation.

## Running Tests

To run the test suite, you can execute the following command:

```bash
# Running the test suite
docker-compose exec web pytest . -v
```

## Database

This application uses PostgreSQL for data storage. The connection settings for the database are configured in the `.env` file. Note that you don't need to install PostgreSQL on your system as the application uses the PostgreSQL Docker image. You can also access it through the Adminer UI at [http://localhost:8080/](http://localhost:8080/) with the following credentials:
- System: PostgreSQL
- Server: db
- Usernmame: myuser
- password: mypassword
- Database: mydb

## Next Steps

The next steps for this project could be the addition of integration tests and support for multiple users.

Please note that this project is an implementation of a coding challenge and is meant for demonstration purposes only.

## License

This project uses the [MIT](https://choosealicense.com/licenses/mit/) license.
