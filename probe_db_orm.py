# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:33:54 2023

@author: nikolaicev_na
"""

import os
import json
from sqlalchemy.orm import sessionmaker
import datetime as dt
from probe_db_classes import Publisher, Book, Sale, Shop, Stock, engine, Base


def get_book_info(author_name):
    if not session.query(Publisher).filter(Publisher.name.ilike(f'%{author_name}%')).all():
        return 'Автора с таким именем нет в базе!'
    else:
        sub = session.query(Publisher.id).filter(Publisher.name.ilike(f'%{author_name}%')).subquery()
        q = session.query(Book.title, Book.id_publisher, Stock.id_shop, Stock.id).\
            join(Stock).subquery()
        q1 = session.query(q.c.title, q.c.id, q.c.id_publisher, Shop.name).join(Shop).subquery()
        q2 = session.query(q1.c.title, q1.c.name, q1.c.id_publisher, Sale.price, Sale.date_sale).\
            join(Sale).subquery()
        q3 = session.query(q2.c.title, q2.c.name, q2.c.price, q2.c.date_sale, q2.c.id_publisher).\
            filter(q2.c.id_publisher == sub.c.id).order_by(q2.c.date_sale)
        title, name = list(map(lambda x: len(x.title), q3.all())), list(map(lambda x: len(x.name), q3.all()))
        price = list(map(lambda x: len(str(x.price)), q3.all()))
        st = f"\n{'Book'.ljust(max(title))} | {'Shop'.ljust(max(name))} | {'Price'.ljust(max(price))} | Date sale"
        st += '\n'+(9 + len(st))*'-' + '\n'
        for s in q3:
            st += f'{s.title.ljust(max(title))} | {s.name.ljust(max(name))} |' \
                      f' {str(s.price).ljust(max(price))} | {s.date_sale} \n'
        return st


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_date_sale(s):
    date = list(map(lambda x: int(x), s.split('T')[0].split('-'))) + list(map(lambda x: int(x) if x[-1] != 'Z' else int(x[:2]), s.split('T')[1].split(':')))
    return dt.datetime(*date)


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
    sale = [Sale(price=float(i['fields']['price']),
                 date_sale=get_date_sale(i['fields']['date_sale']),
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


    
    

    
    