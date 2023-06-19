import streamlit
streamlit.title("My parents' new Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🍲Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚🍳Hard-Boiled free range egg')


streamlit.header('🍌🍊Build your own Smoothie...🍍🍏🥑')
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list= my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New sectionm to display the fruits selected
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
# streamlit.text(fruityvice_response.json())

# normalising the json version 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# shwoing it as a dataframe
streamlit.dataframe(fruityvice_normalized)


