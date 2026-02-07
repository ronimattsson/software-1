import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port ="3306",
    user="roni",
    password="salasana",
    database="flight_game",
    autocommit=True
    )

cursor = yhteys.cursor()

def get_town(town):
    sql = f"SELECT name, municipality from airport where ident = '{town}'"
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if tulos == []:
        return ("","")
    else:
        return tulos[0] #(Nimi, kaupunki)

icao = input("Enter the ICAO code of an airport: ")
(nimi, kaupunki) = get_town(icao.upper())
if nimi != "":
    print(f"Airport name: {nimi}\n"
          f"Location: {kaupunki}")
else:
    print("No airport found with ICAO code " + icao + ".")