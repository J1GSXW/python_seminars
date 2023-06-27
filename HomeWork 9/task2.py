#  Работа в Google Colab. Файл california_housing_train.csv, который находится в папке sample_data
# Узнать какая максимальная households в зоне минимального значения population
import pandas as pd

df = pd.read_csv('/content/sample_data/california_housing_train.csv')

min_population = df['population'].min()
min_population_data = df[df['population'] == min_population]
max_households = min_population_data['households'].max()

print("Максимальное количество households в зоне с минимальным значением population:", max_households)
