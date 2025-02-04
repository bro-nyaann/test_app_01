import streamlit as st

import utils

def fn_menu_option_1(df):
    # title / header
    utils.fn_markdown_text_1(
        "Data Penjualan",
        "Center",
        size=25,
        color= "#ff0000",
        header="h2"
        )
    st.write('---')

    # Filter options
    filtered_df = df

    # buat opsi tamilan tabel: by marketplace: omzet (subtotal); by product: qty terjual; by salesperson: omzet

    radio_options = ['Rinci', 'By Product', 'By Marketplace']
    radio_option = st.sidebar.radio('Tampilan', radio_options)
    st.sidebar.write('---')

    # filter options

    col1, col2, col3 = st.columns([4.75, 0.5, 4.75])
    
    with col1:
        filter_week_index = st.multiselect('Pekan Ke:', df['Index Pekan'].unique())
        if filter_week_index:
            filtered_df = filtered_df[df['Index Pekan'].isin(filter_week_index)]

        filter_product_category = st.multiselect('Kategori Produk', df['Kategori Produk'].unique())
        if filter_product_category:
            filtered_df = filtered_df[df['Kategori Produk'].isin(filter_product_category)]

    with col3:    
        filter_inv_status = st.multiselect('Status Invoice', df['Status Invoice'].unique())
        if filter_inv_status:
            filtered_df = filtered_df[df['Status Invoice'].isin(filter_inv_status)]
        
        filter_mp_name = st.multiselect('Marketplace', df['Nama MP'].unique())
        if filter_mp_name:
            filtered_df = filtered_df[df['Nama MP'].isin(filter_mp_name)]

    if radio_option == radio_options[0]:
        if filter_inv_status == ['Nothing to Invoice']:
            display_df = filtered_df[[
                'No SO',
                'Order Status',
                'Nama MP',
                'Nama Produk',
                'Qty Order',
                'Tanggal',
            ]]

        else:
            display_df = filtered_df[[
                'No SO',
                'Nama MP',
                'Nama Produk',
                'Qty Order',
                'Harga Jual',
                'Discount (%)',
                'Subtotal',
                'Tanggal',
                ]]
        
        display_df = display_df.set_index('No SO')
    
    elif radio_option == radio_options[1]:
        display_df = filtered_df.groupby('Nama Produk', as_index=True)['Qty Terkirim'].sum()
    
    elif radio_option == radio_options[2]:
        display_df = filtered_df.groupby('Nama MP', as_index=True)['Subtotal'].sum()

    st.write('---')

    # Select specific column to display
    # columns_to_display = st.multiselect('Select columns to display', filtered_df.columns, default=filtered_df.columns.tolist())

    # if filter_inv_status == ['Nothing to Invoice']:
    #     display_df = filtered_df[[
    #         'No SO',
    #         'Order Status',
    #         'Nama MP',
    #         'Nama Produk',
    #         'Qty Order',
    #         'Tanggal',
    #     ]]

    # else:
    #     display_df = filtered_df[[
    #         'No SO',
    #         'Nama MP',
    #         'Nama Produk',
    #         'Qty Order',
    #         'Harga Jual',
    #         'Discount (%)',
    #         'Subtotal',
    #         'Tanggal',
    #         ]]

    # Visualise the data
    st.dataframe(display_df, use_container_width=True)

    # show the total omzet
    with st.sidebar:
        total_values = filtered_df['Subtotal'].sum()
        total_non_premium = filtered_df.loc[filtered_df['Kategori Produk'] == 'Produk Non Premium', 'Subtotal'].sum()
        total_premium = filtered_df.loc[filtered_df['Kategori Produk'] == 'Produk Premium', 'Subtotal'].sum()
        st.write('Omset')
        st.write(f'`Premium: Rp. {int(total_premium):,}`')
        st.write(f'`Non Premium: Rp. {int(total_non_premium):,}`')
        st.write(f'`Total: Rp. {int(total_values):,}`')

        # st.write('Omset')
        # total_values = display_df['Subtotal'].sum()
        # st.write(f'`Total: Rp. {int(total_values):,}`')
    
    # tampilkan data penjualan
    ## row: marketplace name; value sum of subtotal revenue

    """
    # chart perbandingan omset dari masing2 mp
        - produk premium &  non premium dari masing2 mp

    # rincian chart | mengguankan expand to view
    fiter: nama mp | default: none; kategori produk | default: any; tahun,bulan,tanggal; invoice status: fully invoiced
    view by: qty produk (total pcs terjual; kategori produk (omset)
    - mp1
        - table: row: nama produk; value: sum of qty nama produk
    
    - mp2
        - table: row: nama produk; value: sum of qty nama produk
    
    - mp3
        - table: row: nama produk; value: sum of qty nama produk
    """