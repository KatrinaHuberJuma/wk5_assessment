"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    def __repr__(self):
        """Representation of a brand"""

        return "\n< BRAND Name: %s, Id: %s >\n" % (self.name, self.brand_id)

    brand_id = db.Column(db.String(5),
                        primary_key = True,
                        autoincremnt = True)
    name = db.Column(db.String(50),
                        nullable = False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))



class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    def __repr__(self):
        """Representation of a model"""

        return "\n< MODEL Name: %s, Id: %s >\n" % (self.name, self.model_id)

    model_id = db.Column(db.Integer,
                        primary_key = True, 
                        autoincremnt = True)
    name = db.Column(db.String(50),
                        nullable = False)
    year = db.Column(db.Integer, 
                        nullable=False)
    brand_id = db.Column(db.String(5), 
                        db.ForeignKey(brand.brand_id),
                        nullable=False)

    brand = db.relationship("Brand", backref="models")



class Award(db.Model):
    """Car model."""

    __tablename__ = "awards"

    def __repr__(self):
        """Representation of an award"""

        return "\n<AWARD Name: %s, Id: %s, Winner_id: %s >\n" % (self.name, self.award_id, self.winner_id)

    award_id = db.Column(db.Integer,
                        nullable=False)
    year = db.Column(db.Integer,
                        nullable=False)
    winner_id = db.Column(db.Integer,
                        db.ForeignKey(model.model_id))
    name = db.Column(db.String(50),
                        nullable=False)

    model = db.relationship("Model", backref="awards")


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
