# SDET Practice Project

A hands-on testing playground designed to explore and demonstrate **Software Development Engineer in Test (SDET)** practices using [Robot Framework](https://robotframework.org/).

The project provides a minimal full-stack web application consisting of a React frontend and a FastAPI backend. Its primary purpose is to serve as a testing environment for developing and experimenting with different levels of automated testing.

## Project Structure

```text
.
├── README.md
├── RobotTests/
│   ├── Tests/
│   └── requirements.txt
├── backend/
│   ├── Dockerfile
│   ├── README.md
│   ├── app/
│   ├── backend-entrypoint.sh
│   ├── pyproject.toml
│   └── tests/
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   └── src/
└── run.sh
```

## Application Overview

The application consists of two independent components:

### Backend

The backend is built with [FastAPI](https://fastapi.tiangolo.com/) and currently exposes a single endpoint responsible for user authentication.

Authentication credentials are configured through environment variables.

### Frontend

The frontend is built with [React](https://react.dev/) and provides a simple login page where users can enter their username and password.

Depending on the authentication result, the application displays one of two messages:

- **Successful login** — displayed in green when valid credentials are provided.
- **Authentication failed** — displayed in red when the credentials are incorrect.

## Getting Started

### Prerequisites

Make sure the following tools are installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Running the Application

The entire application can be started using the provided shell script:

```bash
./run.sh
```

Alternatively, you can start the services directly using Docker Compose:

```bash
docker compose up --build
```

The script `run.sh` serves as a convenient entry point for building and starting the application.

For additional configuration details, refer to the corresponding backend and frontend configuration files.

## Testing Strategy

The project follows the **Testing Pyramid** approach, covering three major levels of automated testing.

### 1. Unit Tests

Unit tests verify individual functions, methods, and classes in isolation.

- Typically written in the same programming language as the code under test.
- Usually maintained by developers.
- Fast, inexpensive, and focused on specific units of functionality.

The backend currently uses [pytest](https://docs.pytest.org/) for unit testing.

Tests are located in:

```text
backend/tests/
```

They are currently executed as part of the backend container startup process through `backend/backend-entrypoint.sh`.

### 2. Integration Tests

Integration tests verify interactions between different modules and components.

Examples include:

- Checking communication between the FastAPI application and a database.
- Verifying interactions between application services.
- Testing API behavior together with its dependencies.

### 3. End-to-End (E2E) and UX Tests

End-to-end tests validate the application as a whole by simulating real user interactions.

For example:

1. Open the application in a browser.
2. Navigate to the login page.
3. Enter valid or invalid credentials.
4. Submit the login form.
5. Verify that the expected authentication result is displayed.

These tests are generally more expensive to develop and maintain, but they provide confidence that the application works from the end user's perspective.

## Robot Framework

[Robot Framework](https://robotframework.org/) is the primary focus of this project.

The `RobotTests/` directory is intended to contain automated tests written using Robot Framework.

The goal is to use the framework to implement and explore browser-based testing scenarios, API testing, and other automation techniques relevant to SDET workflows.

## Roadmap

The following improvements are planned:

- [ ] Implement automated tests using Robot Framework.
- [ ] Move backend unit test execution from `backend/backend-entrypoint.sh` into a dedicated Docker Compose service.
- [ ] Add PostgreSQL as a separate service and configure test users.
- [ ] Improve the backend unit test structure by introducing shared fixtures, configuration, and other pytest best practices.

Some of these improvements are outside the primary scope of the SDET practice, but they will help make the project architecture more consistent and maintainable.

---

**Project status:** Work in progress.