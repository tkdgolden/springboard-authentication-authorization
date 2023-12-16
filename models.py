from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True)
    password_hash = db.Column(db.String)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    feedback = db.relationship('Feedback')

    @classmethod
    def register(self, username, password, email, first_name, last_name):

        password_hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = password_hashed.decode("utf8")

        return self(username=username, password_hash=hashed_utf8, email=email, first_name=first_name, last_name=last_name)
    
    @classmethod
    def authenticate(self, username, password):

        user = User.query.get_or_404(username)

        if bcrypt.check_password_hash(user.password_hash, password):
            return user
        else:
            return False
        
class Feedback(db.Model):
    __tablename__ = "feedbacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('users.username'))

    user = db.relationship('User')