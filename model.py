from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Date, DateTime, Time, Text, Boolean, ForeignKey, Float, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# DATABASE_NAME = 'idergunoff:slon9124@localhost:5432/ipyforum_db'
DATABASE_NAME = 'idergunoff:slon9124@ovz1.j56960636.m29on.vps.myjino.ru:49359/ipyforum_db'

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

    photos = relationship('Photo', back_populates='user')
    #supports = relationship('Support', back_populates='user')
    #support_admin = relationship('Support', back_populates='admin')


class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    file_id = Column(String)
    file_path = Column(String)
    date = Column(DateTime)
    moderated = Column(Boolean, default=False)

    user = relationship('User', back_populates='photos')


class Support(Base):
    __tablename__ = 'support'

    id =Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    admin_id = Column(BigInteger, ForeignKey('user.telegram_id'))
    question = Column(Text)
    answer = Column(Text, nullable=True)
    answering = Column(Boolean, default=False)
    date_question = Column(DateTime)
    date_anawer = Column(DateTime)

    #user = relationship('User', back_populates='supports')
    #admin = relationship('User', back_populates='supports_admin')


Base.metadata.create_all(engine)