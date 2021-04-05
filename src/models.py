import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(50))
    profile = Column(String())    
 
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    photo = Column(String()) 
    effects = Column(String())
    description = Column(String())
    username_id = Column(Integer, ForeignKey('user.id'))
    username = relationship(User) 

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments = Column(String())
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    like = Column(String())
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')