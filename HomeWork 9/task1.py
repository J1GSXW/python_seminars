# Работа в Google Colab. Файл california_housing_train.csv, который находится в папке sample_data
# Для домов, где кол-во людей от 0 до 500 (population) вывести информацию о цене дома(median_house_value):

# максимальное значение
# минимальное значение
# среднее
# медиану

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')

print(df.loc[df['population'] < 501, ['median_house_value']].max())
print(df.loc[df['population'] < 501, ['median_house_value']].min())
print(df.loc[df['population'] < 501, ['median_house_value']].mean())
print(df.loc[df['population'] < 501, ['median_house_value']].median())
