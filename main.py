from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageRequest(BaseModel):
    git_diff: str
    commit_type: str

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.head("/")
def head_root():
    return {"message": "API is running"}

@app.post("/generateCommit")
def process_message(request: MessageRequest):
    if request.commit_type == "feat":
        new_message = "Add a new feature"
    elif request.commit_type == "fix":
        new_message = "Fix a bug"
    else:
        new_message = "General commit"
    
    return {"commit_message": new_message}
