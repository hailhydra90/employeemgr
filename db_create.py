from app import db
from models import BlogPost

#create DB
db.create_all()

#Insert
db.session.add(BlogPost("Hello", "Hello to you"))
db.session.add(BlogPost("Goodbye", "Goodbye to you"))

#Commit Changes
db.session.commit()