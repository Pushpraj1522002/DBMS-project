import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password = '#######',
    database = 'economy'
)

c = mydb.cursor()

def  create():

                continent,country,govta,govtf,mono,peop,trad =st.tabs(["Continent","Country","Government Account","Government Finance","Monetary","People","Trade"])
                
                with continent:
                        cont = st.text_input('Continent Name')
                        Id = st.text_input('Continent ID')
                        if st.button('Insert Into Continent'):
                                
                                try:
                                        insert_query = ('INSERT INTO CONTINENT (Continent_Name, Continent_ID) VALUES (%s, %s)')
                                        data = (cont,Id)
                                        c.execute(insert_query, data)
                                        mydb.commit()
                                        st.success(f'Inserted: {cont}, {Id}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                
                with country:
                        Id = st.text_input("Country Id (Country Table)")
                        Name = st.text_input("Country Name")
                        Status = st.text_input("Country Status")
                        Cont_Id = st.text_input("Continent Id (From Continent Table)")
                        if(st.button('Insert Into Country')):
                                
                                try:
                                        insert_query = ('INSERT INTO COUNTRY (Country_Id,Country_Name,Status,Continent_Id) VALUES(%s,%s,%s,%s)')
                                        data = (Id,Name,int(Status),Cont_Id) 
                                        c.execute(insert_query,data)
                                        mydb.commit()
                                        st.success(f'Inserted: {Id},{Name},{Status},{Cont_Id}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                with govta:
                        Id = st.text_input("Country Id For Govt.Account")
                        Year = st.text_input("Year") 
                        Gdp_Constant_Price = st.text_input("GDP Constant Price")
                        Gdp_Current_Price = st.text_input("GDP Current Price")
                        GDP_Deflator = st.text_input("GDP Deflator")
                        GDP_Per_Captita = st.text_input("GDP Per Capita")
                        Implied_PPP = st.text_input("Implied_PPP")
                        Total_Investments = st.text_input("Total Investments")
                        Gross_National_Savings = st.text_input("Gross National Savings")
                        if(st.button('Insert Into Government Account')):
                                
                                try:
                                        insert_query = ('INSERT INTO government_account (Country_Id,Year,GDP_Constant_Price,GDP_Current_Price,GDP_Deflator,GDP_Per_Capita,Implied_PPP,Total_Investments,Gross_National_Savings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(Gdp_Constant_Price),float(Gdp_Current_Price),float(GDP_Deflator),float(GDP_Per_Captita),float(Implied_PPP),float(Total_Investments),float(Gross_National_Savings))
                                        c.execute(insert_query,data)
                                        mydb.commit()
                                        st.success(f'Inserted: {Id},{Year},{Gdp_Constant_Price},{Gdp_Current_Price},{GDP_Deflator},{GDP_Per_Captita},{Implied_PPP},{Total_Investments},{Gross_National_Savings}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                with govtf:
                        Id = st.text_input("Country Id For Govt.Finance")
                        Year = st.text_input("Financial Year")
                        Revenue = st.text_input("General Government Revenue")
                        Expenditure = st.text_input('General Government Total Expenditure')
                        GDept = st.text_input('General Government Gross Debt')
                        if(st.button('Insert Into Government Finance')):
                                
                                try:
                                        insert_query = ('INSERT INTO government_finance(Country_Id,Financial_Year,General_Government_Revenue,General_Government_Total_Expenditure,General_Government_Gross_Debt) VALUES(%s,%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(Revenue),float(Expenditure),float(GDept))
                                        c.execute(insert_query,data)
                                        mydb.commit()
                                        st.success(f'Inserted: {Id},{Year},{Revenue},{Expenditure},{GDept}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                        
                with mono:
                        Id = st.text_input('Country Id For Monetary')
                        Year = st.text_input('Monetary Year')
                        AvgCP = st.text_input('Inflation Average Consumer Price')
                        EoPC = st.text_input('Inflation End Of Period Of Consumer')
                        if(st.button('Insert Into Monetary')):
                                
                                try:
                                        insert_query = ('INSERT INTO Monetary(Country_Id,Year,Inflation_Average_Consumer_Price,Inflation_End_Of_Period_Of_Consumer) VALUES(%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(AvgCP),float(EoPC))
                                        c.execute(insert_query,data)
                                        mydb.commit()
                                        st.success(f'Inserted: {Id},{Year},{AvgCP},{EoPC}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                
                with peop:
                        Id = st.text_input('Country Id For People')
                        Year = st.text_input('Population Year')
                        Unemployment_rate = st.text_input('Unemployment Rate')
                        Population_rate = st.text_input('Population Rate')
                        if(st.button('Insert Into People')):
                                
                                try:
                                        insert_query = ('INSERT INTO People(Country_Id,Year,Unemployment_rate,Population_rate) VALUES(%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(Unemployment_rate),float(Population_rate))
                                        c.execute(insert_query,data)
                                        mydb.commit()
                                        st.success(f'Inserted: {Id},{Year},{Unemployment_rate},{Population_rate}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                
                with trad:
                        Id = st.text_input('Country Id For Trade')
                        Year = st.text_input('Trade Year')
                        VOIGS = st.text_input('Volume Of Import Goods And Services')
                        VOEGS = st.text_input('Volume Of Export Goods And Services')
                        if(st.button('Insert Into Trade')):
                                
                                try:
                                        insert_query = ('INSERT INTO TRADE (Country_ID,Year,Volume_Of_Import_Goods_And_Services,Volume_Of_Export_Goods_And_Services) VALUES(%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(VOIGS),float(VOEGS))
                                        c.execute(insert_query,data)
                                        mydb.commit()
                                        st.success(f'Inserted: {Id},{Year},{VOIGS},{VOEGS} ')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
        

    
