import pandas as pd

dataFrame = pd.read_csv('penalty_data_set_2.csv')

def dateRange(beginDate, endDate):
    dateRangeFrame = pd.period_range(start= beginDate, end= endDate)
    df = pd.DataFrame(dataFrame, index=dateRangeFrame)
    return df

print(dateRange("01/01/2012", "01/01/2013"))