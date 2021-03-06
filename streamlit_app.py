import streamlit
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   # Normalization 
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized


streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fuityvice fruit advice')
import requests

# Gather the information from the user 
try:
  fruit_choice = streamlit.text_input('what fruit whould you like info about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to show info")
  else:
     fruityvice_normalized = get_fruityvice_data(fruit_choice)
     streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlint.error()




import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])


streamlit.header("The fruit load list contains:")
if streamlit.button('show the list'):
   my_cur = my_cnx.cursor()
   my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
   my_data_rows = my_cur.fetchall()
   streamlit.dataframe(my_data_rows)


def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('"+ new_fruit +"')")
      
      
# Gather the information from the user 
fruit_second_choice = streamlit.text_input('what fruit whould you like to add?')
if streamlit.button('Add a fruit to the list'):
   return_from_function = insert_row_snowflake(fruit_second_choice)
   streamlit.text(return_from_function)



