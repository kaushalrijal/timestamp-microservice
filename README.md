# Timestamp Microservice

A simple microservice to convert between **UNIX** and **UTC** time formats. Built with [FastAPI](https://fastapi.tiangolo.com/) and containerized using [Docker](https://www.docker.com/).

---

## Features

- Convert UNIX timestamps to UTC datetime strings and vice versa
- Get the current time in both UNIX and UTC formats
- Clean, minimal API with clear error handling
- Ready for local development or containerized deployment

---

## API Endpoints

| Method | Endpoint                | Description                                 | Example                                      |
|--------|------------------------|---------------------------------------------|----------------------------------------------|
| GET    | `/api/to-utc`          | Convert UNIX timestamp to UTC               | `/api/to-utc?unix=1715820810`                |
| GET    | `/api/to-unix`         | Convert UTC datetime to UNIX timestamp      | `/api/to-unix?utc=2025-05-16T02:53:00Z`      |
| GET    | `/api/now`             | Get current time in both formats            | `/api/now`                                   |
| GET    | `/`                    | HTML landing page with usage instructions   | `/`                                          |

---

## Running Locally

### 1. Clone the repository

```sh
git clone https://github.com/kaushalrijal/timestamp-microservice.git
cd timestamp-microservice
```

### 2. Create and activate a virtual environment (optional but recommended)

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and edit as needed:

```sh
cp .env.example .env
```

Example `.env`:
```
APP_NAME=Timestamp Microservice
DEBUG=true
HOST=0.0.0.0
PORT=8000
```

### 5. Run the application

```sh
uvicorn app.main:app --reload --host $(grep HOST .env | cut -d '=' -f2) --port $(grep PORT .env | cut -d '=' -f2)
```

Or, export variables before running:

```sh
export $(grep -v '^#' .env | xargs)
uvicorn app.main:app --reload --host $HOST --port $PORT
```

---

## Running with Docker

### 1. Build the Docker image

```sh
docker build -t timestamp-microservice .
```

### 2. Run the container

```sh
docker run --env-file .env -p 8000:8000 timestamp-microservice
```

The service will be available at [http://localhost:8000](http://localhost:8000).

---

## Configuration & Setup Notes

- **Environment Variables:**  
  All configuration is managed via environment variables. See `.env.example` for available options.
- **Dependencies:**  
  All Python dependencies are listed in `requirements.txt`.
- **Testing:**  
  Tests are located in the `test/` directory and can be run with `pytest`.
- **Pre-commit Hooks:**  
  Code style is enforced with [Black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort) via [pre-commit](https://pre-commit.com/). Install hooks with:
  ```sh
  pre-commit install
  ```

---

## Example Usage

- Convert UNIX to UTC:  
  `GET /api/to-utc?unix=1715820810`
- Convert UTC to UNIX:  
  `GET /api/to-unix?utc=2025-05-16T02:53:00Z`
- Get current time:  
  `GET /api/now`
