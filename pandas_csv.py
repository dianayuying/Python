import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
#        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
#        'age': [42, 52, 36, 24, 73], 
#        'preTestScore': [4, 24, 31, ".", "."],
#        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
#df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
#print(df)

#df.to_csv('c:\learning\python\example.csv')

df2 = pd.read_csv('c:\learning\python\example.csv')

print(df2.head())

df2.plot(x='first_name',y='age',style='0')

plt.show()