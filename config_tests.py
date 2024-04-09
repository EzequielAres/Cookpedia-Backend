"""
App configuration
"""

###
# database configuration
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
SQLALCHEMY_TRACK_MODIFICATIONS = False

###
# praetorian configuration
SECRET_KEY = "latch"
JWT_ACCESS_LIFESPAN = {"hours": 24}
JWT_REFRESH_LIFESPAN = {"days": 30}
