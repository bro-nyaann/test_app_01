import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas

from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

import utils
from menu_option_1 import fn_menu_option_1
from menu_option_0 import fn_menu_option_0

def main():
	## inital page config
	st.set_page_config(
		page_title="Sentra Herbal | Menjaga Arti Sehat Kita",
		page_icon=":leaves:",
		layout="wide",
		initial_sidebar_state="expanded"
	)

	## hide streamlit header & footer styles
	utils.fn_hide_streamlit_styles()

	password = st.text_input("Enter your password:", type="password")
	if password == 'SentraHerbal':

		## load the raw data into pandas dataframe
		df_raw = utils.csv_to_df("raw_data/sales_data.csv")
		
		df_raw_2 = utils.fn_split_datetime_column(df_raw, "Order Lines/Created on")
		df_raw_2 = utils.fn_rename_columns(df_raw_2)
		df_raw_2 = utils.fn_add_week_index(df_raw_2)

		## horizontal nav menu ##
		menu_options = (
			"Home",
			"Penjualan",
			"Target",
			"Kendala",
			"Ringkasan",
			'---',
		)

		with st.sidebar:
			picked_option = option_menu(
				"Index",
				menu_options,
				icons=None,
				menu_icon="cast",
				default_index=0,
				orientation="vertical")
			st.write('---')

		# col1, col2 = st.columns()
		# with col1:
		# 	st.write('hello world')

		# with col2:
		# 	st.dataframe(df_raw_2)

		if picked_option == menu_options[0]:
			fn_menu_option_0(df_raw_2)

		elif picked_option == menu_options[1]:
			fn_menu_option_1(df_raw_2)

		elif picked_option == menu_options[2]:
			pass

		elif picked_option == menu_options[3]:
			pass

		elif picked_option == menu_options[4]:
			pass
		
if __name__ == '__main__':
	main()
