import streamlit
import pandas as pd 
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Eggs')
streamlit.text('Pancakes')
streamlit.text('Hash browns')

streamlit.header('🍌Banana Smoothies Available + Your Choice of Additional Fruit 🫐🍓')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Lemon', 'Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]


streamlit.dataframe(my_fruit_list)
