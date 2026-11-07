
import duckdb
from pathlib import Path

sql_file = Path("sql/02_daily_analytics.sql")

con = duckdb.connect()

query = sql_file.read_text(encoding="utf-8")

result = con.execute(query).df()

print(result.to_string(index=False))

con.close()
