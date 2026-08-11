# Expected: 1 finding (SQL Injection / CWE-89)

import sqlite3

def run(user_input: str) -> None:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (name TEXT)")
    # Intentionally insecure: string concatenation into SQL
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cur.execute(query)

if __name__ == "__main__":
    run("test")