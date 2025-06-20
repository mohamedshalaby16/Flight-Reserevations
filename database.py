import sqlite3

conn = sqlite3.connect('flights.db')

def create_table():
    """Create the flights_table if it does not exist."""
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute("""
      CREATE TABLE IF NOT EXISTS flights_table(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              flight_number TEXT,
              departure TEXT,
              destination TEXT,
              date TEXT,
              seat_number TEXT
            )
    """)
    conn.commit()
    conn.close()


def insert_flight(full_name, flight_number, departure, destination, date, seat_number):
    conn= sqlite3.connect('flights.db')
    c=conn.cursor()
    c.execute(""" 
        INSERT INTO flights_table (name, flight_number, departure, destination, date, seat_number)
              VALUES(?,?,?,?,?,?)
              
""",(full_name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()


def view_reservations():
    
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute("SELECT * FROM flights_table")
    rows = c.fetchall()
    conn.close()
    return rows

def update_reservation(fid, full_name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect('flights.db')
    c=conn.cursor()
    c.execute("""
        UPDATE flights_table
        SET name = ?, flight_number = ?, departure = ?, destination =?, date = ?, seat_number = ?
        WHERE id= ?
""",(full_name, flight_number, departure, destination, date, seat_number,fid))
    conn.commit()
    conn.close()


def delete_reservation(fid):
    conn = sqlite3.connect('flights.db')
    c=conn.cursor()
    c.execute("""
        DELETE FROM flights_table 
        WHERE id=?  
  """,(fid,))   
    conn.commit()
    conn.close()