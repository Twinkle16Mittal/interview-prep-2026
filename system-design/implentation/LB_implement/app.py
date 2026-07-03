from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/special")
def read_root():
    return {"message": f"Hello from instance {os.environ.get('INSTANCE_ID', 'unknown')}"}