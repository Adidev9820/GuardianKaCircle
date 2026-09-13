from fastapi import FastAPI

app = FastAPI(title="Guardian Circle Backend")


@app.get("/")
def root():
    return {"status": "Guardian Circle backend is running"}


@app.post("/fall")
def fall_detected():
    return {
        "status": "received",
        "event": "fall",
        "risk": "critical"
    }