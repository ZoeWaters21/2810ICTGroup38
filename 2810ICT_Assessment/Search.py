import pandas as pd

df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)

def dateRangeOffenceCode(beginDate, endDate):
    df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
    df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]
    df3 = df2["OFFENCE_CODE"].value_counts()
    offenceCode = df3.head(19)
    return offenceCode



print(dateRangeOffenceCode("01/02/2002","01/02/2022"))

#print(customSearch('nude'))
