""" import mysql.connector


connection = mysql.connector.connect(
    port=3306, #oletusarvo ei pakollinen.
    host="127.0.0.1", #oletusarvo ei pakollinen.
    database = 'flight_game', 
    user='root',
    password='Rekolammas123',
    autocommit=True
    )

#luodaan osoitin ja sijoitetaan viittaus siihen muuttujaan
cursor = connection.cursor()

#käytetään osoitinta tietokantahakuun
cursor.execute('SELECT municipality FROM airport')
#heataan rivikerrallaan
result = cursor.fetchone()
print(result)

result = cursor.fetchone()
print(result)
#haetaan useampi rivi kerrallaan
result = cursor.fetchmany()
print(result) """
import mysql.connector

connection = mysql.connector.connect(
    port=3306, #oletusarvo ei pakollinen.
    host="127.0.0.1", #oletusarvo ei pakollinen.
    database = 'flight_game', 
    user='root',
    password='Rekolammas123',
    autocommit=True
    )

def get_country_name_by_code(code):
    sql = (f'SELECT name FROM country WHERE iso_country = "{code}"')
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        return "Ei löydy"
    return result

print(get_country_name_by_code('YE'))

country_code = input('Anna maakoodi: ')
country = get_country_name_by_code(country_code)
print(f'Maakoodi: {country_code}, hakutulos: {country}')