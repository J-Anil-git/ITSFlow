"""Fill the ITS Flow tables with the sample data in the data/ folder.

Usage:  python populate_db.py   (run initialise_db.py first)

Existing rows are removed first, so the script can be run again safely.
"""
import csv
from pathlib import Path

import psycopg2
from werkzeug.security import generate_password_hash

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

DATA = Path(__file__).parent / "data"
# Every sample IT Desk account gets this password until real accounts exist.
DEFAULT_PASSWORD = "ChangeMe123!"


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    with conn, conn.cursor() as cur:
        cur.execute("TRUNCATE ticket, it_user, department RESTART IDENTITY")

        departments = {}
        for row in read_csv("departments.csv"):
            cur.execute(
                "INSERT INTO department (department_name) VALUES (%s) RETURNING department_id",
                (row["department_name"],))
            departments[row["department_name"]] = cur.fetchone()[0]

        users = {}
        for row in read_csv("it_users.csv"):
            cur.execute(
                "INSERT INTO it_user (full_name, username, password_hash) "
                "VALUES (%s, %s, %s) RETURNING it_user_id",
                (row["full_name"], row["username"], generate_password_hash(DEFAULT_PASSWORD)))
            users[row["username"]] = cur.fetchone()[0]

        tickets = read_csv("tickets.csv")
        for row in tickets:
            cur.execute(
                "INSERT INTO ticket (staff_name, department_id, description, status, created_at, assigned_to) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (row["staff_name"], departments[row["department"]], row["description"],
                 row["status"], row["created_at"], users.get(row["assigned_to"])))
    conn.close()
    print(f"Inserted {len(departments)} departments, {len(users)} IT Desk users and {len(tickets)} tickets.")


if __name__ == "__main__":
    main()
