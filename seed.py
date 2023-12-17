from models import User, db, Feedback
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# empty and reset database
db.drop_all()
db.create_all()
User.query.delete()

# add users
al = User.register(username="al", password="alpass", email="al@gmail.com", first_name="Al", last_name="La")
bo = User.register(username="bo", password="bopass", email="bo@gmail.com", first_name="Bo", last_name="Zark")
ed = User.register(username="ed", password="edpass", email="ed@gmail.com", first_name="Ed", last_name="Mond")

db.session.add(al)
db.session.add(bo)
db.session.add(ed)

db.session.commit()

# add feedback
good = Feedback(title="Good", content="This is good.", username="bo")
bad = Feedback(title="Bad", content="This is bad.", username="al")
meh = Feedback(title="meh", content="This is meh...", username="al")

db.session.add(good)
db.session.add(bad)
db.session.add(meh)

db.session.commit()