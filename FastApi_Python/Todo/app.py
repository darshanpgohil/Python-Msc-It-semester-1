from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

l = []

app = FastAPI()

class Todo(BaseModel):
    name: str
    due_date: date
    status: str

@app.get("/")
def read_root():
    return {"Mahadev": "Mahadev"}

@app.get("/items/{item_id}")
def get_item_id(item_id: int,user_id: int):
    return {"Item_id": item_id,"User_Id": user_id}

@app.post("/adds/")
def create_task(task: Todo):
    # return {"name":task.name,"due_date":task.due_date,"status":task.status}
    d = {}

    try:
        d["name"] = task.name
        d["due_date"] = task.due_date
        d["status"] = task.status

        l.append(d)
        print(l)

        return  {
                    "details":"Data Saved Successfully"
                }
    except Exception as e:
        return {
            "error": "somthing when wrong",
            "details": str(e)
            }

@app.get("/get/")
def show_todo():
    return l