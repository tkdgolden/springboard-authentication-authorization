from flask import Flask, redirect, render_template, session
from models import db, connect_db, User
from forms import RegisterUserForm, LoginUserForm
from secret import MY_SECRET

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///authentication'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = MY_SECRET

connect_db(app)

app.app_context().push()
db.create_all()

def check_user():
    if 'user' in session:
        user = User.query.get_or_404(session['user'])

        return user
    else:
        return False

@app.route("/")
def index():
    user = check_user()
    if user:
        return redirect(f"/users/{user.username}")
    else:
        return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)

        db.session.add(user)
        db.session.commit()

        session['user'] = user.username

        return redirect(f"/users/{user.username}")
    
    else:
        return render_template("register_user_form.html", form=form)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session['user'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            return redirect("/login")
    
    else:
        return render_template("login_user_form.html", form=form)
    
@app.route("/users/<username>")
def secret(username):
    user = check_user()
    if user.username == username:
        return render_template("user_info.html", user=user)
    
    else:
        return redirect("/")
    
@app.route("/logout")
def logout():
    session.pop('user')

    return redirect("/")