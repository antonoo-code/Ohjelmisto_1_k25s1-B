#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
main_list = [1,2,3,4]


def list_calc(inp_list):
    result_list =sum(inp_list)
    return result_list

list_sum = list_calc (main_list)
print(f'Listan {main_list} summa on : {list_sum}')


