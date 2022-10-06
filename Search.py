import pandas as pd

dataFrame = pd.read_csv('penalty_data_set_2.csv')

def dateRange(beginDate, endDate):
    dateRangeFrame = pd.dataFrame.period_range(column = "OFFENCE_MONTH", start=beginDate, end=endDate)
    dateRangeFrame = pd.loc[dateRangeFrame]
    return dateRangeFrame

print('01/01/12', '01/01/2013')