import streamlit
import pandas as pd 
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Eggs')
streamlit.text('Pancakes')
streamlit.text('Hash browns')

streamlit.header('🍌Banana Smoothies Available + Your Choice of Additional Fruit 🫐🍓')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.fruit))


streamlit.dataframe(my_fruit_list)
