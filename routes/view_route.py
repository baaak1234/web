from flask import render_template,request,jsonify,Blueprint

view_route = Blueprint('view',__name__)

@view_route.route('/index')
def index():
    return render_template('index.html')



@view_route.route("/detail-todo")
def detailtodo():
    todo_id = request.args.get('todo_id')
    return render_template("detail-todo.html",
                           todo_id = todo_id)

@view_route.route("/")
def home():
    return render_template("index.html")


@view_route.route("/login")
def login():
    return render_template("login.html")

@view_route.route("/id-class")
def idclass():
    return render_template("id-class.html")

@view_route.route("/layout")
def layout():
    return render_template("layout.html")

@view_route.route("/front")
def front():
    return render_template("front.html")

@view_route.route("/js-basic")
def jsbasic():
    return render_template("js-basic.html")


@view_route.route("/save-user")
def saveUser():
    return render_template("save-user.html")


@view_route.route("/house")
def house():
    return render_template("house.html")







