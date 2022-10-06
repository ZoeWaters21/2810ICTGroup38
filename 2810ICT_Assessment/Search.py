import pandas as pd

df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)

def dateRange(beginDate, endDate):
    df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
    df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]
    return df2

def customSearch(searchWord):

    df2 = df[df["OFFENCE_DESC"].str.lower().str.contains(searchWord)]
    return df2["OFFENCE_DESC"]

#print(dateRange('01-01-11', '01-01-13'))
print(customSearch('nude'))