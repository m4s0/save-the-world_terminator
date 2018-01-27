import pandas as pd

sensor_ids = [
    '10352',
    '10273',
    '6907',
    '6909',
    '10320',
    '6908',
    '6956',
    '10354',
    '6912',
    '6905',
    '20428',
    '9963',
]

df = pd.read_csv('_data/2017.csv')

for index, row in df.iterrows():
    if str(row['IdSensore']) not in sensor_ids:
        df.drop(index, inplace=True)
    # if index == 100:
    #     break

# mask = df['IdSensore'].isin(sensor_ids)
# df = df[~mask]

df.to_csv('_data/milan_2017_sensor.csv')
