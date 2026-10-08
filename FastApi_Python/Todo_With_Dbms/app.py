from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from datetime import date, datetime, timedelta, timezone
from sqlalchemy.orm import Session
from database import engine,Base,get_db
from model import Todo as TodoModel,User,LoginTrack
import jwt
import secrets
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


SECRETE_KEY = secrets.token_urlsafe(32)
ALGORITHM="HS256"
TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") 

Base.metadata.create_all(bind=engine)

class Todo(BaseModel):
    name: str
    due_date: date
    status: str
    
class UserSignup(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username:str
    password:str

@app.get("/")
def read_root():
    return {"Mahadev": "Mahadev"}

@app.post("/signup")
def signup_todo(us: UserSignup, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.username == us.username        
    ).first()
    
    if user is not None:
        raise HTTPException(
            status_code=400,
            detail="User Already Exiest"
        )
        
    newUser = User(
     username = us.username,
     email = us.email,
     password = us.password   
    )
    
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    
    return{
        "message":"User Created Successfully",
        "user": us.username
    }

@app.post("/login")
def todo_login(ul: UserLogin, db: Session=Depends(get_db)):
    print("login")
    print(ul.username)
    print(ul.password)
    if not (ul.username == "" and ul.password == ""):

        l_user=db.query(User).filter(
            User.username == ul.username,
            User.password == ul.password
        ).first()
        
        if  l_user:
            userLog = LoginTrack(
            username=ul.username,
            )

            db.add(userLog)
            db.commit()
            db.refresh(userLog)
            
            expire = datetime.now(timezone.utc) + timedelta(
                minutes = TOKEN_EXPIRE_MINUTES
            )
            
            payload = {
                "name": l_user.username,
                "exp": expire
            }
            
            TOKEN = jwt.encode(
                payload,
                SECRETE_KEY,
                algorithm=ALGORITHM
            )

            return{
                "access_tocken": TOKEN,
                "detail": "User Login SuccessFully"
            }
        else:
            return{
                "error": "Invalid Credential"
            }
    else:
        return{
            "error": "Username or Password are Empty"
        }

def validate_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRETE_KEY,
            algorithm=[ALGORITHM]
        )
        
        username = payload.get("name")
        
        if username is None:
            HTTPException(
                status_code=401,
                detail="Invalid tocken"
            )
            
        user = User.get(username)
        
        if user is None:
            HTTPException(
                status_code=401,
                detail="User Not Found"
            )
            
        return user
    except :
        pass
    
@app.get("/profile")
def user_profile(
    current_user: dict = Depends(validate_user)
):
    pass

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

@app.put("/update/{edit_id}")
def edit_data(edit_id: int,task: Todo,db: Session = Depends(get_db)):
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
        # "data": l[edit_id]
        "data": todos 
    }
    
@app.delete("/delete/{delete_id}")
def delete_todo(delete_id: int,db: Session = Depends(get_db)):
    # if delete_id < 0 or delete_id >= len(l):
    #     return{
    #         "error":"Deleted Id Is Wrong"
    #     }
        
    # try:
    #     deleted_record = l.pop(delete_id)
    # except IndexError:
    #     return{
    #         "error":"Index Out Of Range"
    #     }
    
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