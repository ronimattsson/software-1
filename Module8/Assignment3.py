import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="roni",
        password="",
        database="flight_game",
        collation='utf8mb3_general_ci',
        autocommit=True
    )
    cursor = connection.cursor()

    query = """
            SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s
            """
    cursor.execute(query, (icao_code,))
    return cursor.fetchone()

def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ")
    icao2 = input("Enter the ICAO code of the second airport: ")
    coords1 = get_airport_coordinates(icao1.upper())
    coords2 = get_airport_coordinates(icao2.upper())
    if coords1 == None:
        print(f"Airport with ICAO code {icao1} not found in the database.")
    elif coords2 == None:
        print(f"Airport with ICAO code {icao2} not found in the database.")
    else:
        distance = geodesic(coords1, coords2).kilometers
        print(f"\n\nDistance between {icao1} and {icao2}: {distance:.2f} kilometers")
    return

run_airport_distance()