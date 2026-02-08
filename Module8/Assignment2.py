import mysql.connector

def get_airports_by_country(country_code):
    yhteys = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="roni",
        password="",
        database="flight_game",
        autocommit=True,
        collation='utf8mb3_general_ci'
    )
    cursor = yhteys.cursor()

    sql = f"SELECT count(*), type FROM airport WHERE iso_country = '{country_code}' GROUP BY type ORDER BY type desc"
    cursor.execute(sql)
    return cursor.fetchall()

def run_country_program():
    code = input("Enter the country code (e.g., FI for Finland): ")
    result = get_airports_by_country(code.upper())
    if result == None or len(result) == 0:
        print(f"No airports found for country code '{code}'.")
    else:
        print("\nAirports in " + code.upper() + ": ")
        for pair in result:
            print(str(pair[0]) + " " + pair[1] + " airports")

run_country_program()