from fastapi import FastAPI

app = FastAPI(title="Guardian Circle Backend")

latest_event = None


@app.get("/")
def root():
    return {"status": "Guardian Circle backend is running"}


@app.post("/fall")
def fall_detected():
    global latest_event

    latest_event = {
        "status": "received",
        "event": "fall",
        "risk": "critical"
    }

    return latest_event


@app.get("/latest")
def get_latest_event():
    if latest_event is None:
        return {
            "status": "none"
        }

    return latest_event