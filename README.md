# FastAPI Caching Service

A high-performance FastAPI-based caching service with database-backed persistence and response transformation.

## Features
- RESTful API endpoints
- Caching mechanism to optimize performance
- Database-backed payload storage
- Input validation for consistency

## Prerequisites
- Docker & Docker Compose installed

## How to Run (Using Docker)
1. Clone the repository:
   ```sh
   git clone git@github.com:omariut/fastapi-caching-service.git
   cd fastapi-caching-service
   ```
2. Create a `.env` file based on `env-example`.
3. Build and start the services:
   ```sh
   docker-compose up --build
   ```
4. The service should be running at:
   - **API**: http://localhost:<WEB_PORT>

   (*`WEB_PORT` is defined in your `.env` file.*)

## Running Tests
To run tests inside the Docker container:
```sh
   docker-compose exec web pytest -v
```

## Documentation
- **Interactive Docs**: [Swagger UI](http://localhost:8000/docs)
- **Redoc**: [Redoc UI](http://localhost:8000/redoc)
(*Assuming your `WEB_PORT` is defined as 8000 in your `.env` file.*)

