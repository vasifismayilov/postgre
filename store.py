import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='vasif172',
    host='localhost',
    port='5432',
    database='store'
)


cursor = connection.cursor()


query = """
CREATE TABLE employee(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    stock_count INT DEFAULT 0,
    new_product BOOLEAN NOT NULL,
    worker_id SERIAL UNIQUE NOT NULL,
    entry_date DATE,
    entry_time DATE,
    expire_date DATE,
    price INT NOT NULL,
    sale_amount INT DEFAULT 0 NOT NULL,
    bar_code INT UNIQUE NOT NULL
)
"""

cursor.execute(query)

connection.commit()