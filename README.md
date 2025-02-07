# Number Classification API

This is a FastAPI-powered Number Classification API that takes an integer as input and returns various mathematical properties along with a fun fact about the number.

## Features
- Determines if a number is **prime**, **perfect**, or **Armstrong**.
- Identifies whether a number is **odd** or **even**.
- Computes the **sum of the digits**.
- Fetches a fun fact about the number using the **Numbers API**.
- Supports **CORS** for cross-origin requests.

## Tech Stack
- **FastAPI** (Python Web Framework)
- **Uvicorn** (ASGI Server)
- **Requests** (For fetching fun facts)
- **Render** (For Deployment)

---

## Getting Started

### 1. Clone the Repository
```sh
 git clone https://github.com/GrailRoyal/number-classification-api.git
 cd number-classification-api
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```sh
 python -m venv venv
 source venv/bin/activate   # On macOS/Linux
 venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4. Run the API Locally
```sh
 uvicorn main:app --reload
```
The API will now be accessible at:
```
http://127.0.0.1:8000
```

## API Endpoints
### 1. Classify a Number
**Endpoint:**
```
GET /api/classify-number?number=<integer>
```

**Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Response (400 Bad Request for invalid input):**
```json
{
    "error": true,
    "number": "alphabet"
}
```

---

## Deployment on Render
### 1. Push Code to GitHub
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Deploy on Render
1. Go to [Render](https://render.com/).
2. Click **New Web Service**.
3. Connect to your GitHub repository.
4. Select **Python** as the environment.
5. Set the **Start Command** to:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```
6. Deploy and wait for your public URL.

### 3. Test Deployed API
```sh
https://stage1-api-1.onrender.com/api/classify-number?number=371

## Author
**Abiodun Richard Fagbuyi** - DevOps Intern at HNG



