from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
print("Database Successfully Connected To Flask")

class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(100), nullable=False)


@app.route("/")
def root():
    # return "Mahadev Mahadev"
    # with app.app_context():
    #     t1 = Todo.query.all()
    #     print(t1)
    return render_template("home.html")

# @app.route("/home",methods=["GET","POST"])
# def home():
#     print(request.method)

#     if request.method == "POST":
#         name = request.form.get("todo-name")
#         date = request.form.get("todo-date")
#         status = request.form.get("todo-status")
#         print(name,date,status)
#         return name
#     else:
#         with app.app_context():
#                 t1 = Todo.query.all()
#                 return render_template("home.html", data=t1)

@app.route("/add",methods=['POST'])
def add_todo():
     todo_name = request.form.get("todo-name")
     todo_dueDate = request.form.get("todo-date")
     toDo_status = request.form.get("todo-status")
     
     todo_dueDate = datetime.strptime(todo_dueDate,"%Y-%m-%d")
     
     with app.app_context():
          t1 = Todo(name=todo_name, due_date=todo_dueDate,status=toDo_status)

          db.session.add(t1)
          db.session.commit()
          
          return redirect("/")
      
@app.route("/get",methods=['GET'])
def get_todo():
    with app.app_context():
        t1 = Todo.query.all()
        print(t1)
    return render_template("home.html",data=t1)

@app.route("/edit",methods=['GET','POST'])
def edit_todo():
    if request.method == 'GET':
        todo_id = request.args.get("id")
        
        todo = Todo.query.get(todo_id)
        
        return render_template("edit.html",todo=todo)
    else:
        todo_id = request.form.get("id")
        todo = Todo.query.get(todo_id)
        
        todo.name = request.form.get("todo-name")
        todo.due_date = datetime.strptime(request.form.get("todo-date"),"%Y-%m-%d")
        todo.status = request.form.get("todo-status")

        db.session.commit()
        
        return redirect("/")

if __name__ == "__main__":
    with app.app_context():
            db.create_all()
    app.run(debug=True)