import psycopg2

conn = psycopg2.connect(
    database  = 'db_games',
    user = 'postgres',
    password = 'Ben10ehFera',
    host = 'localhost',
    port = '5432'
)