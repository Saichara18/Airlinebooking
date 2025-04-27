import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="",  # replace with your MySQL password
        database="flight_db"  # replace with your database name
    )

# Check Database Connection
def test_database_connection():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Run a simple query to check the connection
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result:
            print("Database connection successful!")
        else:
            print("Database connection failed!")
        
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
# Test the connection
test_database_connection()
