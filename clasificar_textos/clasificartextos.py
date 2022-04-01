import pandas as pd
import matplotlib.pyplot as plt

def get_xlsx_df(table):
    df = pd.read_excel(table, engine='openpyxl', na_filter = False)
    return df

homo1 = get_xlsx_df('homo1.xlsx')
print (f'homo1: {homo1}') 

homo2 = get_xlsx_df('homo2.xlsx')
print (f'homo2: {homo2}') 

training, test = homo1, homo2
RETAILER = sorted(training['RETAILER'].unique())
print (f'sorted: {RETAILER}')

print(f'training shape: {training.shape}')
print(f'test shape: {test.shape}')
print ('value counts: ')
print (training['RETAILER'].value_counts())
print (test['RETAILER'].value_counts())
#############visualizacion##############
fig, axes = plt.subplots (1, 2, sharey=True)
training['RETAILER'].value_counts().plot.bar(ax=axes[0])
test['RETAILER'].value_counts().plot.bar(ax=axes[1])
plt.show()



