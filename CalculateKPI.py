import pandas as pd

def calculate():
    dataframe1 = pd.read_excel('KPI.xlsx')
    dataframe1 = pd.DataFrame(dataframe1)

    f =dataframe1.mean(axis='columns', numeric_only=True)
    print(f)
    col = ['Q1', 'Q2','Q3','Q4']
    dataframe1['total'] = dataframe1[col].sum(axis=1)
    dataframe1['average'] = dataframe1[col].mean(numeric_only=True, axis=1)
    print(dataframe1)
    dataframe1.to_excel('output.xlsx', index=False)
    return None



if __name__ == '__main__':
    calculate()