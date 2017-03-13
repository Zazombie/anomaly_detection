import pandas as pd


def data_import(path='big-data\\20130601_init.csv') -> pd.DataFrame:
    df = pd.read_csv(path, ';', parse_dates=[['date', 'time']], dayfirst=True)
    df.set_index(['date_time'], inplace=True, drop=False)

    df.direction1 = df.direction1 / df.direction1.max()
    df.speed1 = df.speed1 / df.speed1.max()
    df.speed2 = df.speed2 / df.speed2.max()
    df.speed3 = df.speed3 / df.speed3.max()
    df.temperature1 = df.temperature1 / df.temperature1.max()
    df.temperature2 = df.temperature2 / df.temperature2.max()
    df.unknown_param = df.unknown_param / df.unknown_param.max()
    df.pressure = df.pressure / df.pressure.max()
    df.voltage1 = df.voltage1 / df.voltage1.max()
    df.voltage2 = df.voltage2 / df.voltage2.max()

    return df


