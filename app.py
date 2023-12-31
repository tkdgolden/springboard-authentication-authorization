from flask import Flask, redirect, render_template, session
from models import db, connect_db, User, Feedback
from forms import RegisterUserForm, LoginUserForm, FeedbackForm
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
    """ Check session for user info. """

    if 'user' in session:
        user = User.query.get_or_404(session['user'])
        return user
    else:
        return False

@app.route("/")
def index():
    """ Display login page if not logged in, user info page if logged in. """

    user = check_user()

    if user:
        return redirect("/users")
    else:
        return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register a new user with a form, form submission. """

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

        return redirect("/users")
    
    return render_template("register_user_form.html", form=form)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log in a user with a form, form submission. """

    form = LoginUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session['user'] = user.username

            return redirect("/users")
        
        else:

            return redirect("/login")
    
    return render_template("login_user_form.html", form=form)
    
@app.route("/users")
def user_info():
    """ Show current user info and all of their feedback. """

    user = check_user()

    if user:

        return render_template("user_info.html", user=user)
    
    return redirect("/")
    
@app.route("/logout")
def logout():
    """ Remove user from session. """

    session.pop('user')

    return redirect("/")

@app.route("/users/delete")
def delete_user():
    """ Delete the selected user. """

    user = check_user()

    if user != False:
        db.session.delete(user)
        db.session.commit()
        session.pop('user')
    
    return redirect("/")

@app.route("/feedback/add", methods=["GET", "POST"])
def add_feedback():
    """ Add new user feedback with form, form submission. """

    user = check_user()

    if user == False:

        return redirect("/")
    
    form = FeedbackForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        feedback = Feedback(title=title, content=content, username=user.username)
        db.session.add(feedback)
        db.session.commit()

        return redirect("/users")
    
    return render_template("feedback_form.html", form=form)

@app.route("/feedback/<int:feedback_id>/update", methods=["GET", "POST"])
def update_feedback(feedback_id):
    """ Update the selected feedback with form, form submission. """

    user = check_user()
    feedback = Feedback.query.get_or_404(feedback_id)

    if (user == False) or (feedback.user.username != user.username):

        return redirect("/")
    
    form = FeedbackForm(obj=feedback)

    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()

        return redirect("/users")
    
    else:
        return render_template("feedback_form.html", form=form)
    
@app.route("/feedback/<int:feedback_id>/delete")
def delete_feedback(feedback_id):
    """ Delete the selected feedback. """

    user = check_user()

    if user == False:

        return redirect("/")
    
    feedback = Feedback.query.get_or_404(feedback_id)

    if feedback.user.username != user.username:

        return redirect("/")
    
    db.session.delete(feedback)
    db.session.commit()

    return redirect("/")