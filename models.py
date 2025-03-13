from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    home_team = Column(String, nullable=False)
    away_team = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    tickets = relationship('Ticket', back_populates='match', cascade='all, delete-orphan')# ensures that if a match is deleted, all related tickets are also deleted.

    
    def __repr__(self):#string representation of the Match object
        return f"Match(id={self.id}, home_team='{self.home_team}', away_team='{self.away_team}', date='{self.date}')"

    @classmethod
    def create(cls, session, home_team, away_team, date):#class method to insert a new match into the database.
        match = cls(home_team=home_team, away_team=away_team, date=date)#Creates a new Match object with the provided details.
        session.add(match)#adds match to the database
        session.commit()#Saves  the match to the database.
        return match#Returns the newly created match object.
    

    #Retrieve All Matches
    @classmethod
    def get_all(cls, session):#retrieves all match records
        return session.query(cls).all()#Fetches all records from the matches table.
    

    #Find Match by ID
    @classmethod
    def find_by_id(cls, session, match_id):
        return session.query(cls).filter_by(id=match_id).first()#Searches for the match with the given match_id.
    
    #Delete a Match
    @classmethod
    def delete(cls, session, match_id):
        match = cls.find_by_id(session, match_id)
        if match:#If the match exists:
            session.delete(match)#delete match from session
            session.commit()#save the changes
            return True# if deletion was successful.
        return False# if deletion was unsuccessful.

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    seat_number = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default='Available')
    
    match = relationship('Match', back_populates='tickets')#Each ticket belongs to one match.
    
    def __repr__(self):#string representation of ticket object
        return f"Ticket(id={self.id}, match_id={self.match_id}, seat='{self.seat_number}', price={self.price}, status='{self.status}')"

    @classmethod
    def create(cls, session, match_id, seat_number, price, status='Available'):#Inserts a new ticket into the database.
        ticket = cls(match_id=match_id, seat_number=seat_number, price=price, status=status)#Creates a new Ticket object.
        session.add(ticket)#Adds the ticket to the session.
        session.commit()#saves the changes to database
        return ticket#Returns the created ticket.
    
    #Retrieve All Tickets
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()#Fetches all records from tickets table.

    @classmethod
    def find_by_id(cls, session, ticket_id):
        return session.query(cls).filter_by(id=ticket_id).first()#Searches for the ticket with the given ticket_id

    @classmethod
    def delete(cls, session, ticket_id):
        ticket = cls.find_by_id(session, ticket_id)#Finds the ticket by ID.
        if ticket:
            session.delete(ticket)
            session.commit()
            return True
        return False

# Database setup
def initialize_db():
    engine = create_engine('sqlite:///match_ticket_booking.db')
    Base.metadata.create_all(engine)#Creates tables if they don’t exist.
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    session = initialize_db()
    print("Database initialized!")
