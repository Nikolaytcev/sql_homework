import psycopg2
import random


def connect_db(name_db, password):
    conn = psycopg2.connect(database=name_db, user="postgres", password=password)
    cur = conn.cursor()
    return conn, cur


def main():
    password = 'Ybrjkfqwtd1990'
    name_db = 'clients'
    conn, cur = connect_db(name_db, password)
    db = DataBase(conn, cur)
    db.create_tables()
    names, lnames, emails, phones = map(lambda x: (f'name{x+1}',), range(10)), map(lambda x: (f'lastname{x+1}',), range(10)),\
                            map(lambda x: (f'mail{x+1}',), range(10)), [(random.randint(10000, 60000),) for _ in range(10)]
    phones[0] = ('12546',)
    for name, lname, email, phone in zip(names, lnames, emails, phones):
        db.add_client(name, lname, email, phone, info='Добавили нового клиента')
    db.add_phone_for_exists_client(('name1',), ('lastname1',), ('mail1',), (58697,))
    old_data = [('name1',), ('lastname1',), ('mail1',), (58697,)]
    db.update_client_info(old_data, name='new_name', lname='', email='', phone=89800)
    db.delete_clients_phone(('new_name',), ('lastname1',), ('mail1',), (89800,))
    db.delete_client(('new_name',), ('lastname1',), ('mail1',), (89800,))
    db.find_client_info(name='name2', lname='', email='', phone=None)
    db.find_client_info(name='', lname='lastname3', email='', phone=None)
    db.find_client_info(name='', lname='', email='mail5', phone=None)
    db.find_client_info(name='', lname='', email='', phone=phones[-1])
    conn.commit()
    cur.close()


class DataBase:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur

    def create_tables(self):
        self.cur.execute("DROP TABLE IF EXISTS phone_numbers, client_info;")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
                                    phone_numbers (number_id SERIAL PRIMARY KEY,
                                             phone_number INT);
                                    """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS
                            client_info (client_id SERIAL PRIMARY KEY,
                                     first_name VARCHAR(20) NOT NULL,
                                     last_name VARCHAR(30) NOT NULL,
                                     email VARCHAR(40) NOT NULL,
                                     phone INT REFERENCES phone_numbers(number_id));
                            """)
        print('Таблицы созданы!')

    def show_result(self, client_info):
        self.cur.execute("""SELECT first_name, last_name, email, phone_number FROM client_info ci
         LEFT JOIN phone_numbers pn ON ci.phone=pn.number_id WHERE
         first_name=%s AND last_name=%s AND email=%s;""", client_info[:-1])
        return self.cur.fetchall()

    def add_client(self, *args, info='Добавили нового клиента'):
        sql_phone = "INSERT INTO phone_numbers (phone_number) VALUES (%s);"
        sql_client = """INSERT INTO client_info (first_name, last_name, email, phone)
                        VALUES (%s, %s, %s, (SELECT number_id FROM phone_numbers WHERE phone_number=%s));"""
        if type(args[-1][0]) == int:
            self.cur.execute(sql_phone, args[-1])
        self.cur.execute(sql_client, args)
        print(f'{info}: {self.show_result(args)}')

    def add_phone_for_exists_client(self, *args):
        sql = """SELECT first_name, last_name, email, phone FROM client_info
                        WHERE first_name=%s AND last_name=%s AND email=%s;"""
        self.cur.execute(sql, args[:-1])
        data = self.cur.fetchall()
        if not data:
            self.add_client(*args)
        elif data[0][-1] is not None and data[0][-1] != args[-1][0]:
            self.add_client(*args, info='Добавили ещё один номер телефона слиенту')
        elif data[0][-1] != args[-1][0]:
            sql_phone = "INSERT INTO phone_numbers (phone_number) VALUES (%s);"
            self.cur.execute(sql_phone, args[-1])
            self.conn.commit()
            sql_client = """UPDATE client_info SET phone=(SELECT number_id FROM phone_numbers WHERE
            phone_number=%s) WHERE first_name=%s AND last_name=%s AND email=%s;"""
            self.cur.execute(sql_client, (args[-1], args[0], args[1], args[2]))
            print(f'Добавили номер телефона усуществующему клиенту {self.show_result(args)}')

    def update_client_info(self, old, name='', lname='', email='', phone=None):
        data = [name, lname, email]
        p = old.copy()
        info = ['first_name', 'last_name', 'email']
        for idx, i in enumerate(data):
            if i != '':
                p[idx] = (i,)
                sql = "UPDATE client_info SET " + info[idx] + "=%s WHERE first_name=%s AND last_name=%s AND email=%s;"
                self.cur.execute(sql, (i, old[0], old[1], old[2]))
        if phone is not None:
            p[-1] = (phone,)
            sql = "UPDATE phone_numbers SET phone_number=%s WHERE phone_number=%s;"
            self.cur.execute(sql, (phone, old[-1]))
        print(f'Данные клиента {old} изменены на: {self.show_result(p)}')

    def delete_clients_phone(self, *client_info):
        sql = """UPDATE client_info SET phone=%s WHERE phone=
                 (SELECT number_id FROM phone_numbers WHERE phone_number=%s);"""
        sql1 = "DELETE FROM phone_numbers WHERE phone_number=%s;"
        self.cur.execute(sql, [(None, ), client_info[-1]])
        self.cur.execute(sql1, client_info[-1])
        print(f'Телефон {client_info[-1][0]} клиента {client_info[:-1]} удалён. Новые данные {self.show_result(client_info)}')

    def delete_client(self, *client_info):
        sql_client = "DELETE FROM client_info WHERE first_name=%s AND last_name=%s AND email=%s;"
        sql_phone = """DELETE FROM phone_numbers WHERE number_id IN (SELECT phone_number FROM client_info WHERE
                    first_name=%s AND last_name=%s AND email=%s);"""
        self.cur.execute("SELECT * FROM client_info WHERE first_name=%s AND last_name=%s AND email=%s;", client_info[:-1])
        if not self.cur.fetchall():
            print('Клиента с такими данными нет в таблице!')
        else:
            self.cur.execute(sql_client, client_info[:-1])
            self.cur.execute(sql_phone, client_info[:-1])
            print(f'Клиент {client_info[:-1]} удалён. Результат поиска в таблице клиентов: {self.show_result(client_info)}')

    def find_client_info(self, name, lname, email, phone):
        sql = """SELECT first_name, last_name, email, phone_number FROM client_info ci LEFT JOIN
                    phone_numbers pn ON ci.phone=pn.number_id
                    WHERE first_name=%s OR last_name=%s OR email=%s OR pn.phone_number=%s;"""
        self.cur.execute(sql, ((name, ), (lname, ), (email, ), (phone, )))
        print(self.cur.fetchall())


if __name__ == '__main__':
    main()
