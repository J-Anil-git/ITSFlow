from flask import Blueprint, render_template

from app import db
from app.models import Ticket

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


# Functionality 2: IT Desk views all tickets and opens one (SELECT with joins)
@bp.route("/dashboard")
def dashboard():
    tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()
    return render_template("dashboard.html", tickets=tickets)


@bp.route("/ticket/<int:ticket_id>")
def ticket_detail(ticket_id):
    ticket = db.get_or_404(Ticket, ticket_id)
    return render_template("ticket_detail.html", ticket=ticket)
