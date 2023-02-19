import sqlite3

def add_msg(data: list):

    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    # Вставка записей
    c.execute(f'''INSERT INTO {data['table_name']}
                (message_id, 
                    timestamp, 
                    telegram_user_id, 
                    type, 
                    text, 
                    reply_to
                    )
                    VALUES(?, ?, ?, ?, ?, ?);''',
                  (data['message_id'],
                  data['timestamp'],
                  data['telegram_user_id'],
                  data['type'],
                  data['text'],
                  data['reply_to']
                )
              )


    c.execute(f"SELECT * FROM {data['table_name']};")
    conn.commit()
    conn.close()

def create_table(table_name: str):

    conn = sqlite3.connect('messages.db')# Создание/вход в бд
    c = conn.cursor()
    c.execute(f'''CREATE TABLE {table_name}
                (message_id integer primary key, 
                timestamp text, 
                telegram_user_id integer, 
                type text, 
                text text, 
                reply_to integer);''')