
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app. connect_db(app) is used in app.py """
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """create a pet who is up for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default= True)


    def __repr__(self):
        """Show info about user"""

        return f'<User {self.id} {self.name} {self.species}>'

