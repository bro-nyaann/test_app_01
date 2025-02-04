import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas

# Load the CSV data
# @st.cache_data
def csv_to_df(csv_source='invoice_price_history.csv'):
	data = pd.read_csv(csv_source)
	return data

def fn_split_datetime_column(df, datetime_column):
    # Split the datetime string into components
    df['Tahun'] = pd.to_datetime(df[datetime_column]).dt.year
    df['Bulan'] = pd.to_datetime(df[datetime_column]).dt.month
    df['Tanggal'] = pd.to_datetime(df[datetime_column]).dt.day
    # df['Jam'] = pd.to_datetime(df[datetime_column]).dt.strftime('%H:%M:%S')
    
    # Drop the original datetime column
    df.drop(columns=[datetime_column], inplace=True)

    # # add week index to the df
    # df['Index Pekan'] = (df['Tanggal'] - 1) // 7 + 1
    
    return df

def fn_rename_columns(df):
    df.rename(columns=
              {'Order Lines/Order Reference': 'No SO', 
               'Order Lines/Salesperson': 'Salesperson',
               'Order Lines/Customer': 'Nama MP',
               'Order Lines/Product/Product Category': 'Kategori Produk',
               'Order Lines/Product': 'Nama Produk',
               'Order Lines/Product Qty': 'Qty Order',
               'Order Lines/Delivered Quantity': 'Qty Terkirim',
               'Order Lines/Product/Cost': 'Cost Produk',
               'Order Lines/Unit Price': 'Harga Jual',
               'Order Lines/Discount (%)': 'Discount (%)',
               'Order Lines/Subtotal': 'Subtotal',
               'Order Lines/Invoice Status': 'Status Invoice',
               'Order Lines/Order Status': 'Order Status'},
               inplace=True)

    return df

def fn_add_week_index(df):
    # add week index
    df['Index Pekan'] = (df['Tanggal'] - 1) // 7 + 1

    # remove any row that contain 'To Invoice'
    df = df[~df['Status Invoice'].str.contains('To Invoice', na=False)]

    return df


def fn_hide_streamlit_styles():
    hide_streamlit_style = """
        <style>
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stStatusWidget"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        #MainMenu {
        visibility: hidden;
        height: 0%;
        }
        header {
        visibility: hidden;
        height: 0%;
        }
        footer {
        visibility: hidden;
        height: 0%;
        }
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def fn_markdown_text_1(text, align='center', size=19, color='#ff0000', header='h1'):
    st.markdown(
    	f"<{header} style='text-align: {align}; color:{color};'> {text} </{header}>",
    	unsafe_allow_html=True
    )

def fn_calculate_discount(value, discount):
     return value - (discount/100 * value)