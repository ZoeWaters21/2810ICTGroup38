import pandas as pd

df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)

def dateRange(beginDate, endDate):
    df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
    df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]
    return df2

def customSearch(searchWord):

    df2 = df[df["OFFENCE_DESC"].str.lower().str.contains(searchWord)]
    return df2["OFFENCE_DESC"]


def dateRangeOffenceCode(beginDate, endDate):
    df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
    df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]
    df3 = df2["OFFENCE_CODE"].value_counts()
    offenceCode = df3.head(19)
    return offenceCode

def mobiletrendSearch():
    distributionDic = {}
    df2 = df[df["OFFENCE_DESC"].str.lower().str.contains("mobile phone")]

    df2['OFFENCE_MONTH'] = pd.to_datetime(df2['OFFENCE_MONTH']).dt.year
    df3 = df2["OFFENCE_CODE"].value_counts()
    print(df3)
    years = df2['OFFENCE_MONTH'].unique()
    years.sort()

    topCases = df3.index.tolist()
    caseList = []
    i = 0
    for year in years:
        ydf = df2[df2['OFFENCE_MONTH'].astype('str').str.contains(str(year))]
        for case in topCases:
            cdf = ydf[ydf["OFFENCE_CODE"].astype('str').str.contains(str(case))]
            ldf = cdf["OFFENCE_CODE"].value_counts()
            if ldf.empty:
                tldf = 0
            else:
                tldf = ldf.tolist()
                tldf = tldf[0]
            caseList.append([case, tldf])
        distributionDic[year] = caseList[i*9: + (9+(9*i))]
        i += 1

    return distributionDic


#print(dateRange('01-01-11', '01-01-13'))
#print(customSearch('nude'))
#print(dateRangeOffenceCode("01-01-2012", '01-01-2013'))

print(mobiletrendSearch())