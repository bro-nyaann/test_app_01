import streamlit as st

import utils

def fn_menu_option_0(df):
    col1, col2, col3 = st.columns(3)
    
    col2.image('images/sentra-herbal-logo.png', use_container_width=True)

    st.write("---")

    col1, col2 = st.columns(2)
    
    utils.fn_markdown_text_1(
        "Laporan Kerja - Januari 2025",
        "Center",
        size=25,
        color= "#FF0000",
        header="h3"
        )
    
    st.divider()
    st.dataframe(df)