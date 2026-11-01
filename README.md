# ITS Flow (IT Service Flow)

ITS Flow is a ticket tracking system for a company IT desk, built with Flask and PostgreSQL.

- **Staff** log an IT issue with their name, department and a description, and are told "Your ticket has been sent to the IT Desk".
- **IT Desk** staff see every ticket on one dashboard and can open a ticket to read its details.

This is the INFO8021 DevOps Strategy and Automation project by Jeon Anil.

## Branches

| Branch | What it holds |
| --- | --- |
| `main` | The initial website: Home and About us pages, no functionality yet. Also the database scripts. |
| `feature/log-ticket` | Functionality 1: Staff log a ticket. The form saves a new row in the `ticket` table. |
| `feature/it-dashboard` | Functionality 2: IT Desk dashboard. Lists every ticket from the database and opens a ticket's detail page. |

The feature branches are kept separate and are not merged into `main`.

## Technologies

Python 3.11, Flask 3.1.3, Flask-SQLAlchemy 3.1.1, Flask-WTF 1.3.0, psycopg2-binary 2.9.13 and PostgreSQL 18. Exact package versions are in `requirements.txt`.

## Project structure

```
ITSFlow/
├── itsflow.py            # starts the app
├── config.py             # settings, read from .env
├── initialise_db.py      # creates the database and tables
├── populate_db.py        # fills the tables with sample data
├── requirements.txt
├── .env.example
├── sql/
│   └── create_tables.sql
├── data/
│   ├── departments.csv
│   ├── it_users.csv
│   └── tickets.csv
└── app/
    ├── __init__.py
    ├── models.py
    ├── forms.py          # feature/log-ticket
    ├── routes.py
    ├── static/
    │   └── style.css
    └── templates/
        ├── base.html
        ├── index.html
        ├── about.html
        ├── log_ticket.html      # feature/log-ticket
        ├── ticket_sent.html     # feature/log-ticket
        ├── dashboard.html       # feature/it-dashboard
        └── ticket_detail.html   # feature/it-dashboard
```

## Getting started

You need Python 3 and PostgreSQL running on your machine.

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# 2. Install the packages
pip install -r requirements.txt

# 3. Copy the settings file and change the database password if yours is different
copy .env.example .env         # Windows
cp .env.example .env           # macOS / Linux

# 4. Create the database and tables, then add the sample data
python initialise_db.py
python populate_db.py

# 5. Run the app
flask --app itsflow run
```

Open http://127.0.0.1:5000 in your browser.

## Database

Three tables, created by `sql/create_tables.sql`:

- `department`: the company's departments.
- `it_user`: IT Desk staff who tickets can be assigned to.
- `ticket`: each logged issue, with its department, status (Open, In Progress or Resolved), the time it was logged and who it is assigned to.

`populate_db.py` loads 8 departments, 5 IT Desk users and 25 tickets from the CSV files in `data/`. The sample data was written for this project and does not describe real people.
