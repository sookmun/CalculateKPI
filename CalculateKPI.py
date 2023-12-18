import pandas as pd

def calculate():
    dataframe1 = pd.read_excel('KPI.xlsx')
    dataframe1 = pd.DataFrame(dataframe1)

    col = ['Q1', 'Q2', 'Q3', 'Q4']
    dataframe1['Total'] = dataframe1[col].sum(axis=1)
    dataframe1['Average'] = dataframe1[col].mean(axis=1)
    print(dataframe1)
    dataframe1.to_excel('calculatedKPI.xlsx', index=False)



if __name__ == '__main__':
    calculate()