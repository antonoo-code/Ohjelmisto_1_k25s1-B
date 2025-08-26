sukupuoli = input('Syötä sukupuolesi:')
if sukupuoli == 'nainen':
    hemoglobiiniarvonainen_str = input('Syötä hemoglobiiniarvo ilman g/l: ')
    hemoglobiiniarvonainen = float(hemoglobiiniarvonainen_str)

    if  117 <= hemoglobiiniarvonainen <= 175:
        print('Hemoglobiini arvosi on normaali.')
    elif 175 < hemoglobiiniarvonainen:
        print('Hemoglobiini arvosi on korkea.')
    elif 117 > hemoglobiiniarvonainen:
        print('Hemoglobiini arvosi on alhainen.')

if sukupuoli == 'mies':
    hemoglobiiniarvomies_str = input('Syötä hemoglobiiniarvo ilman g/l;')
    hemoglobiiniarvomies = float(hemoglobiiniarvomies_str)

    if 134 <= hemoglobiiniarvomies <= 195:
        print('Hemoglobiini arvosi on normaali.')
    elif 195 < hemoglobiiniarvomies:
        print('Hemoglobiini arvosi on korkea.')
    elif 134 > hemoglobiiniarvomies:
        print('Hemoglobiini arvosi on alhainen.')

