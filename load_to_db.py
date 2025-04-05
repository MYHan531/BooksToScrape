# load_to_db.py

import pandas as pd
from sqlalchemy import create_engine

# 1. Load the CSV scraped earlier
df = pd.read_csv('books_raw.csv')

# 2. Define PostgreSQL connection string
db_user = 'postgres' # might be 'root'
db_password = 'root'   # 🔐 replace with your actual password
db_host = 'localhost'
db_port = '5432'
db_name = 'books_db'

# 3. Create SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# code to test connection
# with engine.connect() as conn:
#     result = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
#     print("Tables in DB:", [row[0] for row in result])

# 4. Load the data into a table called 'books_raw'
df.to_sql(
    'books_raw',
    engine,
    if_exists='replace',
    index=False,
    method='multi'  # sends rows in batches
)

print("[SUCCESS] Data loaded into PostgreSQL!")

