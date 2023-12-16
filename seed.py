from models import User, db
from flask_bcrypt import Bcrypt

db.drop_all()
db.create_all()

User.query.delete()

bcrypt = Bcrypt()

al = User.register(username="al", password="alpass", email="al@gmail.com", first_name="Al", last_name="La")
bo = User.register(username="bo", password="bopass", email="bo@gmail.com", first_name="Bo", last_name="Zark")
ed = User.register(username="ed", password="edpass", email="ed@gmail.com", first_name="Ed", last_name="Mond")

db.session.add(al)
db.session.add(bo)
db.session.add(ed)

db.session.commit()