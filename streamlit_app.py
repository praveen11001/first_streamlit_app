import streamlit

streamlit.title("My Mom's new Healthy Diner")
  
streamlit.header(' Breakdown Header')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Ranged Egg')
streamlit.text('🥑🍞 Avocardo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


#new section to display fruitvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# show json response of fruityvice api
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())

# take the data into json format and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# make the unstructured data of json into table like data using dataframe function of pandas of python
streamlit.dataframe(fruityvice_normalized)

