# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:58:40 2023

@author: nikolaicev_na
"""

import sqlalchemy as sq
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime as dt


password_ = 'Ybrjkfqwtd1990'
database = 'netology_db'

DSN = f"postgresql://postgres:{password_}@localhost:5432/{database}"
engine = sq.create_engine(DSN)
Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(40), nullable=False, unique=True)


class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

    pub = relationship('Publisher', backref='book')


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(40), nullable=False)


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer, nullable=True)

    book = relationship('Book', backref='stock')
    shop = relationship('Shop', backref='stock')


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL(10, 2), nullable=False)
    date_sale = sq.Column(sq.DateTime, default=dt.datetime.now())
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer, nullable=True)

    stock = relationship('Stock', backref='sqle')
 
    
