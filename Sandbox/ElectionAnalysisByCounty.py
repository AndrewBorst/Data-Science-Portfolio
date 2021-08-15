# Election anaylsis by county to test hypothesis that college educated voters
# made a significant switch in 2020. 
# 
# Author: Andrew Borst
# Date: 08/08/2021

import numpy as np
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pandas
import pandas as pd

# print(pd.read_csv('.\Public_Datasets\countypres_2000-2020.csv'))
df = pd.read_csv('.\Public_Datasets\countypres_2000-2020.csv')
dfhead = df.head()

