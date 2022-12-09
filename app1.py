import calendar  
from datetime import datetime  

import plotly.graph_objects as go  
import streamlit as st 
from streamlit_option_menu import option_menu 

#import database as db  # local import

# -------------- SETTINGS --------------
incomes = ["Input Income"]
currency = "Rp"
page_title = "PDAM KOTA SEMARANG"
page_icon = ":sweat_drops:"  
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " )


years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


st.header(f"Cari Tagihan ({currency})" ":money_with_wings:")
page_icon = ":money_with_wings:"
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Bulan :", months, key="month")
    col2.selectbox("Tahun :", years, key="year")
    
    no = st.text_input("No Pelanggan : ")
    name = st.text_input("Nama Pelanggan : ")
    "---"
    st.text("PENGGUNAAN AIR")
    income1 = st.number_input("Meter Awal (m3) :", min_value=0, format="%i", step=1)
    income2 = st.number_input("Meter Akhir (m3) :", min_value=0, format="%i", step=1)
    income = income2-income1
    

    "---"

    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter a comment here ...")
        
    "---"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        i = income
        
        st.write(f"Periode : {period}")
        st.write(f"Nomor Pelanggan : {no}")
        st.write(f"Nama Pelanggan : {name}")
        st.write(f"Pemakaian Air /m3 : {income}")
        if (i<10):
            st.write(f"Jumlah Tagihan : {i*2500}")                # Pemakaian 0 - 10 m3 sebesar Rp. 2.500/meter kubik
        elif (i<20):
            st.write(f"Jumlah Tagihan : {(i-10)*5000+25000}")    # Pemakaian 11 - 20 m3 sebesar Rp. 5.000/meter kubik
        elif (i<30):
            st.write(f"Jumlah Tagihan : {(i-20)*7000+75000}")     # Pemakaian 21 - 30 m3 sebesar Rp. 7.000/meter kubik
        else :
            st.write(f"Jumlah Tagihan : {(i-30)*10000+145000}")  # Pemakaian >31 m3 sebesar Rp. 10.000/meter kubik
        st.write(f"Comment : {comment}")
        st.success("Data saved!")
    
    
