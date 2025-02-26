import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='#########',
    database = 'economy'
)

c = mydb.cursor()

def delete():
                continent,country,govta,govtf,mono,peop,trad = st.tabs(["Continent","Country","Government Account","Government Finance","Monetary","People","Trade"])
                
                with continent:
                        Cont_Id = st.text_input("Enter the Continent Id You Want To Delete",key='Cont_Y')
                        if(st.button(f'Del(Continent Id) : {Cont_Id}',key='Continent')):
                                
                                try:
                                        c.execute(f"DELETE FROM Continent WHERE Continent_Id = '{Cont_Id}'")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                with country:
                        Count_Id = st.text_input("Enter the Country Id You Want To Delete",key='Count_I')
                        if(st.button(f'Del(Country Id) : {Count_Id}',key='Country')):
                                
                                try:
                                        c.execute(f"DELETE FROM Country WHERE Country_Id = '{Count_Id}'")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                with govta:
                        Count_Id = st.text_input("Enter the Country Id",key='govta_C')
                        Year = st.text_input("Enter the Year",key='govta_Y')

                        if(st.button(f'Del(Country Id) : {Count_Id} Year : {Year}',key='govta')):
                                
                                try:
                                        c.execute(f"DELETE FROM government_account WHERE Country_Id = '{Count_Id}' AND Year = {Year}")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                with govtf:
                        Count_Id = st.text_input("Enter the Country Id ",key='govtf_C')
                        Year = st.text_input("Enter the Year",key='govtf_Y')

                        if(st.button(f'Del (Country Id) : {Count_Id} Year : {Year}',key='govtf')):
                                
                                try:
                                        c.execute(f"DELETE FROM government_finance WHERE Country_Id = '{Count_Id}' AND Year = '{Year}")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                
                with mono:
                        Count_Id = st.text_input("Enter the Country Id ",key='mono_C')
                        Year = st.text_input("Enter the Year",key='mono_Y')

                        if(st.button(f'Del(Country Id) : {Count_Id} Year : {Year}',key='mono')):
                                
                                try:
                                        c.execute(f"DELETE FROM Monetary WHERE Country_Id = '{Count_Id}' AND Year = '{Year}")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                
                with peop:
                        Count_Id = st.text_input("Enter the Country Id ",key='peop_C')
                        Year = st.text_input("Enter the Year",key='peop_Y')

                        if(st.button(f'Del(Country Id) : {Count_Id} Year : {Year}',key='peop')):
                                
                                try:
                                        c.execute(f"DELETE FROM people WHERE Country_Id = '{Count_Id}' AND Year = '{Year}")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                
                with trad:
                        Count_Id = st.text_input("Enter the Country Id ",key='trad_C')
                        Year = st.text_input("Enter the Year",key='trad_Y')

                        if(st.button(f'Del(Country Id) : {Count_Id} Year : {Year}',key='trad')):
                                
                                try:
                                        c.execute(f"DELETE FROM trade WHERE Country_Id = '{Count_Id}' AND Year = '{Year}")
                                        mydb.commit()
                                        st.success(f'Deleted Successfully')                        
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                

 
