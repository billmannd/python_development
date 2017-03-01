
#run the following commands in an ipython console. 
import lxml
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
from sqlalchemy import create_engine
pd.read_csv('example')
df = pd.read_csv('example')
df.to_csv('example')
df.to_csv('My_output')
pd.read_csv('My_output')
pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
df.to_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

pd.read_csv('My_output')
df.to_csv('My_output',index=False)
pd.read_csv('My_output')
data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
type(data)
data[0]
data[0].head()

df
engine = create_engine('sqlite:///:memory:')
df
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)
sqldf

