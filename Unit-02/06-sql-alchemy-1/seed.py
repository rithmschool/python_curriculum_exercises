from app import db, Snack

db.create_all()

snack1 = Snack("Hershey", "Chocolate")
snack2 = Snack("Skittles", "Candy")
snack3 = Snack("Chips Ahoy", "Cookie")

db.session.add_all([snack1, snack2, snack3])
db.session.commit()