
from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze")
def analyze(payload: dict):
    return {
        "rootCause": "Database connection pool exhaustion",
        "severity": "HIGH",
        "summary": "Traffic spike caused DB pool exhaustion."
    }
