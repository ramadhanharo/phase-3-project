from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Updated import for SQLAlchemy 2.0 compatibility
Base = declarative_base()
engine = create_engine('sqlite:///tickets.db')
Session = sessionmaker(bind=engine)

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    home_team = Column(String)
    away_team = Column(String)
    date = Column(DateTime)

    tickets = relationship('Ticket', back_populates='match', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Match(id={self.id}, home_team='{self.home_team}', away_team='{self.away_team}', date='{self.date}')"

    @classmethod
    def create(cls, session, home_team, away_team, date):
        match = cls(home_team=home_team, away_team=away_team, date=date)
        session.add(match)
        session.commit()
        return match

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, match_id):
        return session.query(cls).filter_by(id=match_id).first()

    @classmethod
    def delete(cls, session, match_id):
        match = cls.find_by_id(session, match_id)
        if match:
            session.delete(match)
            session.commit()
            return True
        return False

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    seat_number = Column(String)
    price = Column(Float)

    match = relationship('Match', back_populates='tickets')

    def __repr__(self):
        return f"Ticket(id={self.id}, match_id={self.match_id}, seat_number='{self.seat_number}', price={self.price})"

    @classmethod
    def create(cls, session, match_id, seat_number, price):
        ticket = cls(match_id=match_id, seat_number=seat_number, price=price)
        session.add(ticket)
        session.commit()
        return ticket

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, ticket_id):
        return session.query(cls).filter_by(id=ticket_id).first()

    @classmethod
    def delete(cls, session, ticket_id):
        ticket = cls.find_by_id(session, ticket_id)
        if ticket:
            session.delete(ticket)
            session.commit()
            return True
        return False

def initialize_db():
    Base.metadata.create_all(engine)
    return Session()

# Only runs when you execute models.py directly
if __name__ == "__main__":
    initialize_db()
    print("Database initialized!")
