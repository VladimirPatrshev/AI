import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
df = pd.DataFrame(data)
categories = df['whoAmI'].unique()
one_hot_df = pd.DataFrame()
for category in categories:
    one_hot_df[category] = (df['whoAmI'] == category).astype(int)
    
print(one_hot_df) 