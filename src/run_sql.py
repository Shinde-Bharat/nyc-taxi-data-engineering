
import duckdb
from pathlib import Path

SQL_FILE = Path("sql/01_basic_analytics.sql")

# Create an in-memory analytical database
connection = duckdb.connect()

# Read SQL queries
sql_content = SQL_FILE.read_text(encoding="utf-8")

# Execute each query separately
queries = [
    query.strip()
    for query in sql_content.split(";")
    if query.strip()
]

for index, query in enumerate(queries, start=1):
    print(f"\n========== QUERY {index} ==========")

    result = connection.execute(query).df()

    print(result.to_string(index=False))

connection.close()
