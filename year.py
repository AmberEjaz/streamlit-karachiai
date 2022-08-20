# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:37:00 2022

@author: HP
"""

import pandas as pd
import streamlit as st


def main():
    st.title('Air Passengers Report')
    data=pd.read_csv('AirPassengers.csv')
    data['Year']= data['Month'].apply(lambda x:x.split('-')[0])
    years=st.selectbox('Year',data['Month'].unique())
    button=st.button('Generate Info')
    if button:
        subset=data[data['Year']==years]
        st.table(subset)
    


if __name__=='__main__':
    main()
