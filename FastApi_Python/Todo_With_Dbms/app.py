from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from database import engine,Base,get_db
from model import Todo as TodoModel,User

# l = []

app = FastAPI()

Base.metadata.create_all(bind=engine)

class Todo(BaseModel):
    name: str
    due_date: date
    status: str

@app.post("/signup")
def signup_user(us: User,db: Session = Depends(get_db)):

    try:
        if us.username in newTask:
            raise HTTPException(
                status_code=400,
                detail="User Already Exiest"
            )

        newTask = User(
                username = us.username,
                email = us.email,
                password = us.password,
                timestamp = us.timestamp
            )

        return {
            "message":"User Created Successfully",
            "user":us.username
        }
    except Exception as e:
        return {
            "message":str(e)
        }

@app.get("/")
def read_root():
    return {"Mahadev": "Mahadev"}

@app.get("/items/{item_id}")
def get_item_id(item_id: int,user_id: int):
    return {"Item_id": item_id,"User_Id": user_id}

@app.post("/adds/")
def create_task(task: Todo,db: Session = Depends(get_db)):
    # d = {}

    try:
        # d["name"] = task.name
        # d["due_date"] = task.due_date
        # d["status"] = task.status

        # l.append(d)
        # print(l)
        
        newTask = TodoModel(
            name = task.name,
            due_date = task.due_date,
            status = task.status
        )
        
        db.add(newTask)
        db.commit()
        db.refresh(newTask)

        return  {
                    "details":"Data Saved Successfully"
                }
    except Exception as e:
        return {
            "error": "somthing when wrong",
            "details": str(e)
            }

@app.get("/get/")
def show_todo(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos
    # return l

@app.put("/update/{edit_id}")
def edit_data(edit_id: int,task: Todo,db: Session = Depends(get_db)):
    # if edit_id < 0 or edit_id >= len(l):
    #     return{
    #         "error":"Edit_id Is Wrong Given"
    #     }
    
    # l[edit_id]["name"] = task.name
    # l[edit_id]["due_date"] = task.due_date
    # l[edit_id]["status"] = task.status
    
    todos = db.query(TodoModel).filter(
        TodoModel.id == edit_id
    ).first()
    
    if todos == None:
        return{
            "error":"Updeted Id Not Exiest"
        }    
        
    todos.name = task.name
    todos.due_date = task.due_date
    todos.status = task.status
    
    db.commit()
    db.refresh(todos)
    
    return{
        "details":"Record Updated Successfully",
        "data": todos
    }
    
@app.delete("/delete/{delete_id}")
def delete_todo(delete_id: int,db: Session = Depends(get_db)):
    todos = db.query(TodoModel).filter(
        TodoModel.id == delete_id
    ).first()
    
    if todos is None:
        return{
            "error": "Deleted Id Not Exiest"
        }
        
    db.delete(todos)
    db.commit()
    
    return{
        "details":"Record Deleted Successfully",
        # "data": deleted_record
        "data": {
                    "id": delete_id 
                }
    }