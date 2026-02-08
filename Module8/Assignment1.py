import mysql.connector

def get_town(code):
    connection = mysql.connector.connect(
    host="localhost",
    port ="3306",
    database="flight_game",
    user='roni',
    password='',
    autocommit=True,
    collation='utf8mb3_general_ci'
    )
    cursor = (connection.cursor())
    query = """
            SELECT name, municipality FROM airport WHERE ident = %s
            """

    cursor.execute(query, (code,))
    result = cursor.fetchall()
    if result == None or result == []:
        return ("","")
    else:
        return result[0]  # (Nimi, kaupunki)

def main():
    icao = input("Enter the ICAO code of an airport: ")
    (nimi, kaupunki) = get_town(icao.upper())
    if nimi != "":
        print(f"Airport name: {nimi}\n"
              f"Location: {kaupunki}")
    else:
        print("No airport found with ICAO code " + icao)

main()