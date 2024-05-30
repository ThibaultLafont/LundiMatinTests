class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/lundi_matin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# import os

# class Config:
#     DEBUG = True
#     SECRET_KEY = 'your_secret_key'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost/lundi_matin')
