# Use pandas to convert csv to db
import pandas as pd
from sql import SQLConnection
#TODO find classes for these functions

# dbName = 'global_sea_levels_nosignals'
# Converts a csv to a db file and prints the db as an output
def csv_to_db(dbName):
  
  # Create db object
  db = open(f'data/{dbName}.db', 'w')
  # Close file
  db.close()

  # Connect to created database
  conn = SQLConnection(f'data/{dbName}.db')

  # Get data from CSV using pandas
  sea_level_data = pd.read_csv(f'data/{dbName}.csv')

  # if_exists can be 'replace', 'append' or 'error' and defines behaviour when chosen table name already exists
  # conn defines the db this table is being added to
  sea_level_data.to_sql(dbName, conn, if_exists = 'replace', index = False)

  # Define a queue
  q = f'SELECT * FROM {dbName}'

  # Iterate through connection printing each row
  for r in conn.queue(q):
    print(r)

# Takes name and two fields of database and returns two lists containing the data from those fields
# param is optional and defines a parameter for grabbing data, leave blank string if not using
def generate_xy_lists(dbName, field1, field2, param):
  # Predefined queries
  q1 = f'SELECT {field1} FROM {dbName} {param}'
  q2 = f'SELECT {field2} FROM {dbName} {param}'
  
  # Lists for holding x and y values
  x_list = []
  y_list = []
  
  # Connect to database
  conn = SQLConnection(f'data/{dbName}.db')
  
  # Get data from specified fields
  for r in conn.query(q1):
    x_list.append(r)
  for r in conn.query(q2):
    x_list.append(r)

  # return lists
  return x_list, y_list