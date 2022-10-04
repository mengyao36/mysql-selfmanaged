# sudo apt-get install python3-dev default-libmysqlclient-dev
# pip install pymysql # Successfully installed pymysql-1.0.2
# pip install python-decouple
# pip3 install Flask-SQLAlchemy

# import needed paclages
from sqlalchemy import create_engine
import pandas as pd
import os
from decouple import config

# get info from GCP created vm
MYSQL_HOSTNAME = config('HOST')

MYSQL_USER = config('USER')

MYSQL_PASSWORD = config('KEY')

MYSQL_DATABASE = config('DATABASE')

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'

db = create_engine(connection_string)

# need to use GCP terminal (vm) to create a database, then a table with some columns first, finally run the commands below
# get data from mysql
query = 'select * from hmy.table1;'
query

# return this query as dataframe from mysql
df = pd.read_sql(query, con=db) # need to change settings in GCP terminal (0.0.0.0) AND give firewall rule for this vm
df
# Output as below: 
# Empty DataFrame
# Columns: [var1, var2]
# Index: []

####################################################################
# find some data from one git repo use the link for raw data display
# load dataset called "small.csv" *
real_df = pd.read_csv('https://raw.githubusercontent.com/mengyao36/mysql-selfmanaged/main/Data/small.csv')
real_df
# Output as below: 
#     ID  Age  Gender  Health
# 0  100   78  Female       1
# 1  101   56    Male       4
# 2  102   49    Male       5
# 3  103   23  Female       5
# 4  104   50  Female       3
# 5  105   66    Male       2

# uplode this dataset into mysql
real_df.to_sql('new_table', con=db, if_exists='replace')

sql_query = """select * from new_table where Age = '50';"""

age_50 = pd.read_sql(sql_query, con=db)
age_50
# Output as below:
#    index   ID  Age  Gender  Health
# 0      4  104   50  Female       3