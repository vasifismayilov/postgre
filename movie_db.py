import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='vasif172',
    host='localhost',
    port='5432',
    database='movie_db'
)


cursor = connection.cursor()

query = """
CREATE TABLE hmw(
    id SERIAL PRIMARY KEY,
    film_name VARCHAR(50) NOT NULL,
    description TEXT,
    rating INT NOT NULL DEFAULT 0,
    movie_genre SERIAL UNIQUE NOT NULL,
    release_date DATE NOT NULL,
    trailer BOOLEAN DEFAULT false
)   
"""


cursor.execute(query)

connection.commit()