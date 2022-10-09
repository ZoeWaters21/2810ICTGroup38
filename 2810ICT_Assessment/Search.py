import pandas as pd
from collections import OrderedDict

df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)

def mobiletrendSearch():
    distributionDic = OrderedDict()
    df2 = df[df["OFFENCE_DESC"].str.lower().str.contains("mobile phone")]

    df2['OFFENCE_MONTH'] = pd.to_datetime(df2['OFFENCE_MONTH']).dt.year
    df3 = df2["OFFENCE_CODE"].value_counts()
    print(df3)
    years = df2['OFFENCE_MONTH'].unique()
    years.sort()

    topCases = df3.index.tolist()
    print(topCases, type(topCases))
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

        print(caseList)
        distributionDic[year] = caseList
        caseList = []
        i += 1

        analysisList1 = []
        analysisList2 = []
        analysisList3 = []

    for key, value in distributionDic.items():
        print(key, '->', value[0][0], value[1][0], value[2][0])

print(mobiletrendSearch())
