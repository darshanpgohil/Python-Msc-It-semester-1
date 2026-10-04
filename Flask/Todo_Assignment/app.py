from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Date
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(200), nullable=False)
    description = db.Column(String(200), nullable=False)
    priority = db.Column(String(200), nullable=False)
    is_complited = db.Column(String(5), nullable=False)
    due_date = db.Column(Date, nullable=False)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title")
    description = request.form.get("description")
    priority = request.form.get("priority")
    is_completed = request.form.get("is_complited")
    due_date = request.form.get("due_date")
    # print(f"{title}, {description}, {priority}, {is_completed}, {due_date}")
    
    due_date = datetime.strptime(due_date, '%Y-%m-%d')
    
    t1 = Todo(title=title,description=description,priority=priority,is_complited=is_completed,due_date=due_date)
    
    db.session.add(t1)
    db.session.commit()
    
    return render_template("index.html", message="Todo added successfully")

@app.route("/get", methods=['GET'])
def get_todo():
    t1 = Todo.query.all()
    print(t1)
    
    return render_template("index.html",data=t1)

@app.route("/toggle/<int:id>", methods=['GET'])
def toggle_todo(id):
    t1 = Todo.query.get(id)
    
    if t1.is_complited == "True":
        t1.is_complited = "False"
    else:
        t1.is_complited = "True"
        
    db.session.commit()
        
    return redirect("/get")

@app.route("/edit", methods=['GET','POST'])
def edit_todo():
    if request.method == 'GET':
        e_id = request.args.get("e_id")
        t1 = Todo.query.get(e_id)
        
        return render_template("edit_todo.html",t1=t1)
    else:
        e_id = request.form.get("e_id")
        t1 = Todo.query.get(e_id)
        print(e_id)
        print(t1)
        
        edit_title = request.form.get("e_title")
        edit_description = request.form.get("e_description")
        edit_priority = request.form.get("e_priority")
        edit_is_completed = request.form.get("e_is_completed")
        edit_due_date = request.form.get("e_due_date")
        
        t1.title = edit_title
        t1.description = edit_description
        t1.priority = edit_priority
        t1.is_complited = edit_is_completed
        
        edit_due_date = datetime.strptime(edit_due_date, '%Y-%m-%d')
        
        t1.due_date = edit_due_date
        
        db.session.commit()
        
        # print(edit_title,edit_description,edit_priority,edit_is_completed,edit_due_date)
    return redirect("/get")

@app.route("/delete", methods=['POST'])
def delete_todo():
    d_id = request.form.get("d_id")
    print(d_id)
    
    t1 = Todo.query.get(d_id)
    
    db.session.delete(t1)
    db.session.commit()
    
    return redirect("/get")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)