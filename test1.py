import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


# Read raw data from the file
# Supress unnecessary warnings so that presentation looks clean
#import warnings
#warnings.filterwarnings('ignore')

import pandas #provides data structures to quickly analyze data
#Since this code runs on Kaggle server, data can be accessed directly in the 'input' folder
#Read the train dataset
dataset = pandas.read_csv("Data/train.csv")

#Read test dataset
dataset_test = pandas.read_csv("Data/test.csv")
#Save the id's for submission file
ID = dataset_test['id']
#Drop unnecessary columns
dataset_test.drop('id',axis=1,inplace=True)

#Print all rows and columns. Dont hide any
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

#Display the first five rows to get a feel of the data
print(dataset.head(5))

#Learning : cat1 to cat116 contain alphabets


# Size of the dataframe

print(dataset.shape)

# We can see that there are 188318 instances having 132 attributes

#Drop the first column 'id' since it just has serial numbers. Not useful in the prediction process.
dataset = dataset.iloc[:,1:]

#Learning : Data is loaded successfully as dimensions match the data description