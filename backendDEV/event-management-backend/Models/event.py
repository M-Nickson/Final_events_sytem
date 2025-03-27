from ..databaseDEV.db_configure import db
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    attendees = db.Column(db.JSON)  # Store attendees as a JSON array
    payment = db.Column(db.String(50))  # Store payment method


class Venue (db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)   
    location = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)


class Ticket (db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    ticket_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    available_quality = db.Column(db.Integer, nullable=False)  # Number of tickets available 


class Registration (db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)  # Date of registration


class payment (db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    registration_id = db.Column(db.Integer, db.ForeignKey('registrations.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)  # Date of payment
    payment_method = db.Column(db.String(50), nullable=False)  # Payment method (e.g., credit card, PayPal)


class Notification (db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.column(db.Integer, db.ForeignKey('events.id'))
    message = db.Column(db.Text, nullable=False)  # Notification message

class Feedback (db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating out of 5
    comment = db.Column(db.Text, nullable=True)  # Optional comment