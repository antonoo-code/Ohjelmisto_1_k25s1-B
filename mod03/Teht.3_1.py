Kuhan_pituus_str = input('Anna kuhan pituus senttimetreinä:')
Kuhan_pituus = float(Kuhan_pituus_str)
if Kuhan_pituus < 37 :
    print(f'Laita takaisin järveen! {37-Kuhan_pituus} cm puuttuu.')
else:
    print('Onnittelut vonkaleesta!')
