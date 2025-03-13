# phase-3-project

# Stadium Ticket Booking System

# Developed by Ramadhan
# Project Overview

The Stadium Ticket Booking System is a Python CLI application that allows users to manage football matches and tickets using a database powered by SQLAlchemy ORM. Users can create, view, search, and delete matches and tickets through an interactive command-line interface.

# Features

# Match Management:

Create a new football match

View all matches

Find a match by ID

Delete a match

# Ticket Management:

Create a ticket for a specific match

View all tickets

Find a ticket by ID

Delete a ticket

Data Persistence: Uses SQLAlchemy ORM for efficient database interactions.

# Technologies Used

Python

SQLAlchemy (ORM)

SQLite (or any preferred database)

Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/stadium-ticket-booking.git
cd stadium-ticket-booking

# Set up a virtual environment (recommended):

pipenv install
pipenv shell

Ensure dependencies are installed:


# Initialize the database:

python models.py

Run the application:

python cli.py

Usage

After running python cli.py, the menu options will be displayed:

Stadium Ticket Booking System
1. Manage Matches
2. Manage Tickets
3. Exit

Follow the prompts to create, view, and manage matches and tickets.

Database Models

# Match

id: Primary key

home_team: Name of the home team

away_team: Name of the away team

date: Date and time of the match


# Ticket

id: Primary key

match_id: Foreign key referencing Match

seat_number: Assigned seat

price: Ticket price

Relationship: Belongs to Match

# Future Improvements

Implement a GUI version

Add user authentication

Integrate payment processing

# License

This project is licensed under the MIT License.



