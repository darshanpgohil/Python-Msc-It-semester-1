from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy import create_engine,Column,Integer,String,Boolean,Date
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="Mahadev_Bholenath_Shankar_180905_Kailash",
    same_site="lax",
    https_only=False
)

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush = False,
    bind= engine
)

Base = declarative_base()
templates = Jinja2Templates(directory="templates")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(150), default=None)
    description = Column(String(300), default=None)
    priority = Column(String(20), default=None)
    is_completed = Column(Boolean, default=False)
    created_by = Column(String(100), nullable=False)
    due_date = Column(Date, default=datetime.now)
    
Base.metadata.create_all(bind=engine)

print("Database successfully created")

# @app.get("/")
# def root():
#     return {"Message" : "Mahadev Mahadev"}

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
def get_username(request: Request):
    username = request.session.get("username")

    if not username:
        raise HTTPException(
            status_code=401,
            detail="Please Login First"
        )
        
    return username


def get_user_task(task_id:int, username: str, db: Session):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.username == username
    ).first()
    
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )
        
    return task

@app.get("/")
def home(request:Request, db: Session = Depends(get_db)):
    username = request.session.get("username")
    
    if not username:
        return RedirectResponse("/login", status_code=303)
    
    tasks = db.query(Task).filter(
        Task.created_by == username
    ).order_by(Task.id.desc()).all()
    
    pending_task = [t for t in tasks if not t.is_completed]
    complited_task = [t for t in tasks if t.is_completed]
    
    theme = request.cookie.get("theme", "light")
    
    if theme not in ("light","dark"):
        theme = "light"
        
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "username":username,
            "pending_tasks": pending_task,
            "complited_task": complited_task,
            "theme": theme
        }
    )