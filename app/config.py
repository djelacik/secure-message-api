import os

""" class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/messages')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 """

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
