from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Date, DateTime, Time, Text, Boolean, ForeignKey, Float, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime


DATABASE_NAME = 'idergunoff:slon9124@localhost:5432/ipyforum_db'
# DATABASE_NAME = 'idergunoff:slon9124@ovz1.j56960636.m29on.vps.myjino.ru:49359/ipyforum_db'

engine = create_engine(f'postgresql+psycopg2://{DATABASE_NAME}', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    telegram_id = Column(BigInteger, primary_key=True)
    name = Column(String)
    admin = Column(Boolean, default=False)
    date_start = Column(DateTime)
    date_active = Column(DateTime)
    
    links = relationship('LinkPhoto', back_populates='admin')

    # photos = relationship('Photo', back_populates='user')
    support_questions = relationship('SupportQuestion', back_populates='user')
    support_answers = relationship('SupportAnswer', back_populates='admin')


# class Photo(Base):
#     __tablename__ = 'photo'

#     id = Column(Integer, primary_key=True)
#     user_id = Column(BigInteger, ForeignKey('user.telegram_id'))
#     file_id = Column(String)
#     file_path = Column(String)
#     date = Column(DateTime)
#     moderated = Column(Boolean, default=False)

#     user = relationship('User', back_populates='photos')


class LinkPhoto(Base):
    __tablename__ = 'link_photo'
    
    id = Column(Integer, primary_key=True)
    link = Column(String)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.datetime.now())
    admin_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    
    admin = relationship('User', back_populates='links')


class SupportQuestion(Base):
    __tablename__ = 'support_question'

    id =Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    text_question = Column(Text)
    date_question = Column(DateTime, default=datetime.datetime.now())
    answering = Column(Boolean, default=False)
    
    user = relationship('User', back_populates='support_questions')
    support_answers = relationship('SupportAnswer', back_populates='question')
    
    
class SupportAnswer(Base):
    __tablename__ = 'support_answer'
    
    id =Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('support_question.id'))
    admin_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    text_answer = Column(Text, nullable=True)
    date_anawer = Column(DateTime, default=datetime.datetime.now())

    admin = relationship('User', back_populates='support_answers')
    question = relationship('SupportQuestion', back_populates='support_answers')


class SummitQuestion(Base):
    __tablename__ = 'summit_question'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    user_name = Column(String)
    who_question = Column(String)
    text_question = Column(Text, default='')
    date_question = Column(DateTime, default=datetime.datetime.now())


Base.metadata.create_all(engine)