# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:33:54 2023

@author: nikolaicev_na
"""

import random
import json
import os
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime as dt
from decimal import Decimal


password_ = ''
database = ''

DSN = f"postgresql://postgres:{password_}@localhost:5432/{database}"
engine = sq.create_engine(DSN)
Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(40), nullable=False)


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
    date_sale = sq.Column(sq.DATE, default=dt.datetime.now())
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer, nullable=True)

    stock = relationship('Stock', backref='sqle')


def get_book_info(author_name):
    if not session.query(Publisher).filter(Publisher.name.like(f'%{author_name}%')).all():
        return 'Автора с таким именем нет в базе!'
    else:
        sub = session.query(Publisher.id).filter(Publisher.name.like(f'%{author_name}%')).subquery()
        q = session.query(Book.title, Book.id_publisher, Stock.id_shop, Stock.id).\
            join(Stock).subquery()
        q1 = session.query(q.c.title, q.c.id, q.c.id_publisher, Shop.name).join(Shop).subquery()
        q2 = session.query(q1.c.title, q1.c.name, q1.c.id_publisher, Sale.price, Sale.date_sale).\
            join(Sale).subquery()
        q3 = session.query(q2.c.title, q2.c.name, q2.c.price, q2.c.date_sale, q2.c.id_publisher).\
            filter(q2.c.id_publisher == sub.c.id).all()
        title, name = list(map(lambda x: len(x.title), q3)), list(map(lambda x: len(x.name), q3))
        price = list(map(lambda x: len(str(x.price)), q3))
        st = ''
        for s in q3:
            st += f'{s.title.ljust(max(title))} | {s.name.ljust(max(name))} |' \
                      f' {str(s.price).ljust(max(price))} | {s.date_sale} \n'
        return st


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def filling_tables(data):
    file = json.load(open(data, 'r'))
    publisher = [Publisher(name=i['fields']['name']) for i in file if i['model'] == 'publisher']
    print('Авторы, которые есть в базе: ', end='')
    print(*[i['fields']['name'] for i in file if i['model'] == 'publisher'], sep=', ')
    book = [Book(title=i['fields']['title'], id_publisher=i['fields']['id_publisher']) for i in file if
            i['model'] == 'book']
    shop = [Shop(name=i['fields']['name']) for i in file if i['model'] == 'shop']
    stock = [Stock(id_book=i['fields']['id_book'], id_shop=i['fields']['id_shop'], count=i['fields']['count']) for i in
             file if i['model'] == 'stock']
    sale = [Sale(price=Decimal(i['fields']['price']),
                 date_sale=dt.datetime.now() + dt.timedelta(days=random.randint(1, 20), hours=random.randint(2, 5)),
                 id_stock=i['fields']['id_stock'], count=i['fields']['count']) for i in file if i['model'] == 'sale']
    l = [publisher, book, shop, stock, sale]
    for i in l:
        session.add_all(i)
        session.commit()


data = os.listdir(os.getcwd())[os.listdir(os.getcwd()).index('tests_data.json')]
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

filling_tables(data)

print(get_book_info(input('Введите имя автора: ')))

