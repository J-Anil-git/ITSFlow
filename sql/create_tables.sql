-- ITS Flow (IT Service Flow) - database schema
-- PostgreSQL 18
-- Run against the itsflow database (initialise_db.py does this for you).

DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS it_user;
DROP TABLE IF EXISTS department;

CREATE TABLE department (
    department_id   SERIAL PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE it_user (
    it_user_id    SERIAL PRIMARY KEY,
    full_name     VARCHAR(50)  NOT NULL,
    username      VARCHAR(30)  NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE ticket (
    ticket_id     SERIAL PRIMARY KEY,
    staff_name    VARCHAR(50)   NOT NULL,
    department_id INTEGER       NOT NULL REFERENCES department (department_id),
    description   VARCHAR(1000) NOT NULL,
    status        VARCHAR(15)   NOT NULL DEFAULT 'Open'
                  CHECK (status IN ('Open', 'In Progress', 'Resolved')),
    created_at    TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assigned_to   INTEGER       REFERENCES it_user (it_user_id)
);

CREATE INDEX idx_ticket_department ON ticket (department_id);
CREATE INDEX idx_ticket_assigned_to ON ticket (assigned_to);
