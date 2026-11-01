from flask import Blueprint, redirect, render_template, url_for

from app import db
from app.forms import TicketForm
from app.models import Department, Ticket

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


# Functionality 1: Staff log a ticket (INSERT into ticket)
@bp.route("/log", methods=["GET", "POST"])
def log_ticket():
    form = TicketForm()
    form.department.choices = [(0, "Choose your department")] + [
        (d.department_id, d.department_name)
        for d in Department.query.order_by(Department.department_name)
    ]
    if form.validate_on_submit():
        ticket = Ticket(staff_name=form.staff_name.data.strip(),
                        department_id=form.department.data,
                        description=form.description.data.strip())
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for("main.ticket_sent", ticket_id=ticket.ticket_id))
    return render_template("log_ticket.html", form=form)


@bp.route("/sent/<int:ticket_id>")
def ticket_sent(ticket_id):
    ticket = db.get_or_404(Ticket, ticket_id)
    return render_template("ticket_sent.html", ticket=ticket)
