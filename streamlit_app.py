import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("My Mom's new Healthy Diner")
  
streamlit.header(' Breakdown Header')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Ranged Egg')
streamlit.text('🥑🍞 Avocardo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# adding pandas import functionality here--
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)





#create a repeatable code block (called function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#new section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get the information about the fruit.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

# # show json response of fruityvice api
# streamlit.text(fruityvice_response.json())

# take the data into json format and normalize it 
# make the unstructured data of json into table like data using dataframe function of pandas of python

# dont run anything from here while we are facing troubleshoot
streamlit.stop()


#snowflake connector import start works from here
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

#add another input from user for fruit
add_my_fruit = streamlit.text_input("What fruit would you like to add: ", "Gauva")
streamlit.write('Thanks for adding fruit ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit') ")
