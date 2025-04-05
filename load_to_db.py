# load_to_db.py

import pandas as pd
from sqlalchemy import create_engine
import getpass

# 1. Load the CSV scraped earlier
df = pd.read_csv('books_raw.csv')

# 2. Prompt for sensitive or customizable values
db_user = input("Enter PostgreSQL username (default: postgres): ") or 'postgres'
db_password = getpass.getpass("Enter PostgreSQL password: ")
db_host = input("Enter host (default: localhost): ") or 'localhost'
db_port = input("Enter port (default: 5432): ") or '5432'
db_name = input("Enter database name (default: books_db): ") or 'books_db'

# 3. Create SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# 4. Load the data into a table called 'books_raw'
df.to_sql(
    'books_raw',
    engine,
    if_exists='replace',
    index=False,
    method='multi'  # sends rows in batches
)

print("[SUCCESS] Data loaded into PostgreSQL!")


# code to test connection
# with engine.connect() as conn:
#     result = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
#     print("Tables in DB:", [row[0] for row in result])
