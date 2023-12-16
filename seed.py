from models import User, db

db.drop_all()
db.create_all()

User.query.delete()

al = User(username="al", email="al@gmail.com", first_name="Al", last_name="La")
bo = User(username="bo", email="bo@gmail.com", first_name="Bo", last_name="Zark")
ed = User(username="ed", email="ed@gmail.com", first_name="Ed", last_name="Mond")

db.session.add(al)
db.session.add(bo)
db.session.add(ed)

db.session.commit()