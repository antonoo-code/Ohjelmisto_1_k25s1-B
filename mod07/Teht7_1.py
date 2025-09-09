month = int(input('Syötä haalutun kuukauden järjestysnumero: '))


seasons = ('talvi', 'talvi', 'kevät', 'kevät', 'kevät', 'kesä', 'kesä', 'kesä', 'syksy', 'syksy' , 'syksy' ,'talvi')
month_order = seasons[month-1]
print(f'Halutun kuukaudenn vuodenaika on: {month_order}')




