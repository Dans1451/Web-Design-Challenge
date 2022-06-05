
  
# importing pandas module
import pandas as pd
  

  
  
# reading the data in the csv file
cities_df = pd.read_csv('Resources/cities.csv')
cities_df.to_html('cities.html')
  
  
