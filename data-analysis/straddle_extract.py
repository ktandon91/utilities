import pandas as pd

df = pd.read_excel('BN_I.xlsx')

def return_value(x):
    try:
        return x.split('(')[1].split('-')[0]
    except Exception as e:
        return 0

def return_time(x):
    try:
        temp = x.split(' ')[-1]
        if ":" in str(temp):
            return temp
        else:
            return " "
    except Exception as e:
        return " "

def return_day(x):
    try:
        temp = x.split('(')[-1]
        temp = temp[0:3]
        return temp
    except Exception as e:
        return " "

df['DAY'] = df['Date'].apply(return_day)
df['CE SELL VALUE'] = df['INVERTEDCE'].apply(return_value)
df["CE BUY TIME"] = df['INVERTEDCE'].apply(return_time)

df['PE SELL VALUE'] = df['INVERTEDPE'].apply(return_value)
df["PE BUY TIME"] = df['INVERTEDPE'].apply(return_time)

df.to_excel("BN_I_intermin.xlsx")


