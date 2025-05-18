
import pandas as pd
import numpy as np
empdf = {
    'Ename':["Sukesh","Vineetha","Chandra","Sindhu"],
    'Eno':[101,102,103,104],
    'Salary':[10000,20000,30000,40000]
}

Employee = pd.DataFrame(empdf)
print("Display the Employee DataFrame")
print(Employee)
#checking pandas version
print(pd.__version__)