"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
        # ``Brand.query.filter_by(name='Ford')`` would return a query object.
        # in order to get an instance of Brand (corresponding to a row in the brands
        # database), you would have to tack .first() or .one() on the end


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
        # An association table is a kind of "middle table" between two tables
        # that have a "many to many" relationship (which is not directly possible).
        # Each row in an association table bears a foreign key to two other tables.
        # The "many to many"-ness is created by having multiple rows for containing
        # a certain foreign key (allowing it to be related to multple other fks)




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter(Brand.brand_id == 'ram').first()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(db.or_(Brand.discontinued != None, Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Brand.query.filter(Brand.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models_of_year = db.session.query(Model).join(Brand).filter(Model.year==year).all()
    for a_model in models_of_year:
        print a_model.name, a_model.brand.name, a_model.brand.headquarters


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    all_models = db.session.query(Model).join(Brand).all()

    brand_models = {}

    for this_model in all_models:
        brand_models[this_model.brand.name] = brand_models\
                                             .get(this_model.brand.name, [])
        brand_models[this_model.brand.name].append(tuple([this_model.name, this_model.year]))

    print brand_models

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return db.session.query(Brand).filter(Brand.name.like('%{}%'.format(mystr))).all()
    


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return db.session.query(Model).filter(Model.year >= start_year, Model.year < end_year).all()

