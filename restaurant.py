import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.hellodisneyland.com/restaurants-disneyland-paris")

def main(page):
    SRC = page.content
    Soup = BeautifulSoup(SRC, "lxml")
    table = Soup.find("figure", {"class": 'wp-block-table'})
    title = table.find_all("strong")
    word_title = [i.text.strip() for i in title]
    df = pd.DataFrame(columns=word_title)

    columns_data = table.find_all("tr")

    for row in columns_data[1:]:
        row_data = row.find_all("td")
        individual_row_data = [data.text.strip() for data in row_data ] 
        length =len(df)
        df.loc[length] =individual_row_data
      

    df.to_csv(r'C:\Users\messaoudi\OneDrive\Bureau\POWER BI\PI_4BI3\restaurants.csv', index=False)


    
main(page)      
      
   
    
    

  

     
        

  
    





