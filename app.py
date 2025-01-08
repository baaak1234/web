from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/saveUser",methods=['GET'])
def saveUser():
    id = request.args.get('id')
    pw = request.args.get('pw')



    return "ok-coding"






@app.route("/detail-todo")
def detailtodo():
    todo_id = request.args.get('todo_id')
    return render_template("detail-todo.html",
                           todo_id = todo_id)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/id-class")
def idclass():
    return render_template("id-class.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/front")
def front():
    return render_template("front.html")

@app.route("/js-basic")
def jsbasic():
    return render_template("js-basic.html")






if __name__ == "__main__":
    app.run(debug=True)
