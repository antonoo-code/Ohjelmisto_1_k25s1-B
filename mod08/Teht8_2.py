import mysql.connector

connection = mysql.connector.connect(
    port=3306, #oletusarvo ei pakollinen.
    host="127.0.0.1", #oletusarvo ei pakollinen.
    database = 'flight_game', 
    user='root',
    password='Rekolammas123',
    autocommit=True)



Input_code = input('Syötä maakoodi: ')

cursor = connection.cursor()
result =cursor.execute(f'SELECT type, count(*) FROM airport WHere iso_country like "{Input_code}"group by type')
result2 = cursor.fetchall()
print(result2)