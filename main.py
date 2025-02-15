from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageRequest(BaseModel):
    git_diff: str
    commit_type:str

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/generateCommit")
def process_message(request: MessageRequest):
    # print(request.message)
    # LLM function
    new_message = "first comit"
    return {"new_message": new_message}