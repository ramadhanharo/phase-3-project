from models import initialize_db, Match, Ticket
from datetime import datetime

def main():
    session = initialize_db()#Connects to the database and creates a session to interact with it.
    
    while True:
        print("\nStadium Ticket Booking System")
        print("1. Manage Matches")
        print("2. Manage Tickets")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manage_matches(session)
        elif choice == "2":
            manage_tickets(session)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_matches(session):
    while True:
        print("\nMatch Management")
        print("1. Create Match")
        print("2. View All Matches")
        print("3. Find Match by ID")
        print("4. Delete Match")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            home_team = input("Enter home team: ")
            away_team = input("Enter away team: ")
            date_str = input("Enter match date (YYYY-MM-DD HH:MM): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                match = Match.create(session, home_team, away_team, date)
                print(f"Match Created: {match}")
            except ValueError:
                print("Invalid date format.")
        elif choice == "2":
            matches = Match.get_all(session)
            for match in matches:
                print(match)
        elif choice == "3":
            match_id = input("Enter Match ID: ")
            match = Match.find_by_id(session, match_id)
            print(match if match else "Match not found.")
        elif choice == "4":
            match_id = input("Enter Match ID to delete: ")
            if Match.delete(session, match_id):
                print("Match deleted successfully.")
            else:
                print("Match not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_tickets(session):
    while True:
        print("\nTicket Management")
        print("1. Create Ticket")
        print("2. View All Tickets")
        print("3. Find Ticket by ID")
        print("4. Delete Ticket")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            match_id = input("Enter Match ID: ")
            seat_number = input("Enter Seat Number: ")
            price = input("Enter Price: ")
            try:
                price = float(price)
                ticket = Ticket.create(session, match_id, seat_number, price)
                print(f"Ticket Created: {ticket}")
            except ValueError:
                print("Invalid price format.")
        elif choice == "2":
            tickets = Ticket.get_all(session)
            for ticket in tickets:
                print(ticket)
        elif choice == "3":#Connects to the database and creates a session to interact with it.
            ticket_id = input("Enter Ticket ID: ")
            ticket = Ticket.find_by_id(session, ticket_id)
            print(ticket if ticket else "Ticket not found.")
        elif choice == "4":
            ticket_id = input("Enter Ticket ID to delete: ")
            if Ticket.delete(session, ticket_id):
                print("Ticket deleted successfully.")
            else:
                print("Ticket not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":#ensures the script runs only when executed directly,
    main()