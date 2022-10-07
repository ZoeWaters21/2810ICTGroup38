import pandas as pd

df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)

def dateRange(beginDate, endDate):
    df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
    df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]
    return df2

def customSearch(searchWord):

    df2 = df[df["OFFENCE_DESC"].str.lower().str.contains(searchWord)]
    return df2["OFFENCE_DESC"]

def offenceCodeDistribution():
    columns = df.values.tolist()
    offences = []
    for i in columns:
        tuple = [i[2], i[23]]
        offences.append(tuple)

    count = {}
    runtime = 0
    for list in offences:
        runtime += 1
        print(runtime)
        if runtime > 10:
            break
        for elements in offences:
            if elements[0] in count:
                count[elements[0]] += elements[1]
                print(count)
                runtime += 1
                print(runtime)
                if runtime > 10:
                    break
            else:
                count[elements[0]] = elements[1]
                print(count)
                runtime += 1
                print(runtime)
                if runtime > 10:
                    break

    return count

#print(dateRange('01-01-11', '01-01-13'))
#print(customSearch('nude'))
print(offenceCodeDistribution())