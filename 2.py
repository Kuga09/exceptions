import pandas as pd

try:
    f = open('my_file.txt')
except FileNotFoundError:
    print('Файл не найден.')

try:
    df = pd.read_csv('my_file.csv')
except FileNotFoundError:
    print('Файл не найден.')
else:
    try:
        if 'A' not in df.columns:
            raise ValueError("Столбец А в датафрейме не найден")
        if 'B' not in df.columns:
            raise ValueError("Столбец B в датафрейме не найден")
        if 'C' not in df.columns:
            raise ValueError("Столбец C в датафрейме не найден")
        if 'D' not in df.columns:
            raise ValueError("Столбец D в датафрейме не найден")
    except Exception as e: 
        print(f'{e}')

