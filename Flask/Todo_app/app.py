from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
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
    return "Mahadev Mahadev"

@app.route("/home",methods=["GET","POST"])
def home():
    print(request.method)

    if request.method == "POST":
        name = request.form.get("todo-name")
        date = request.form.get("todo-date")
        status = request.form.get("todo-status")
        print(name,date,status)
        return name
    else:
        # return "Invalid Data"

        return render_template("index.html")

@app.route("/add",methods=['POST'])

def add_todo():
     todo_name = request.form.get("todo-name")
     todo_dueDate = request.form.get("todo-date")
     toDo_status = request.form.get("todo-status")
     with app.app_context():
          t1 = Todo(name=todo_name, due_date=todo_dueDate,status=toDo_status)

          db.session.add(t1)
          db.session.commit()


if __name__ == "__main__":
    with app.app_context():
            db.create_all()
    app.run(debug=True)