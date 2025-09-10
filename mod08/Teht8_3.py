from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
    port=3306, #oletusarvo ei pakollinen.
    host="127.0.0.1", #oletusarvo ei pakollinen.
    database = 'flight_game', 
    user='root',
    password='Rekolammas123',
    autocommit=True)




Code_input1 = input('Syötä ensimmäisen kentän ICAO koodi: ')
Code_input2 = input('Syötä toisen kentän ICAO koodi: ')
def airport_distance_calc(code1, code2):
    airport_cordi1 = (f'SELECT latitude_deg, longitude_deg  FROM airport WHERE ident = "{code1}"')
    cursor = connection.cursor()
    cursor.execute(airport_cordi1)
    port_cordi1 = cursor.fetchall()
    
    airport_cordi2 = (f'SELECT latitude_deg, longitude_deg  FROM airport WHERE ident = "{code2}"')
    cursor = connection.cursor()
    cursor.execute(airport_cordi2)
    port_cordi2 = cursor.fetchall()

    final_distance = distance.distance(port_cordi1, port_cordi2).kilometers
    return final_distance

print(f'Lentokenttien etäisyys on : {airport_distance_calc(Code_input1, Code_input2)} kilometriä.')



