import streamlit
from urllib.error import URLError

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
    streamlint.error("Please select a fruit to show info")
  else:
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      # Normalization 
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlint.error()



streamlit.stop()
import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# Gather the information from the user 
fruit_second_choice = streamlit.text_input('what fruit whould you like to add?', 'orange')
streamlit.write('the user entered',fruit_second_choice)


my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlint')")
