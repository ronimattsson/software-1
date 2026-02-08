import mysql.connector

def get_town(town):
    sql = f"SELECT name, municipality from airport where ident = '{town}'"
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if tulos == []:
        return ("","")
    else:
        return tulos[0] #(Nimi, kaupunki)

yhteys = mysql.connector.connect(
    host="localhost",
    port ="3306",
    user="roni",
    password="",
    database="flight_game",
    autocommit=True,
    collation='utf8mb3_general_ci'
    )
cursor = yhteys.cursor()

icao = input("Enter the ICAO code of an airport: ")
(nimi, kaupunki) = get_town(icao.upper())
if nimi != "":
    print(f"Airport name: {nimi}\n"
          f"Location: {kaupunki}")
else:
    print("No airport found with ICAO code " + icao + ".")