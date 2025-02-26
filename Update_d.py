import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='########',
    database = 'economy'
)

c = mydb.cursor()

def update():
                continent,country,govta,govtf,mono,peop,trad = st.tabs(["Continent","Country","Government Account","Government Finance","Monetary","People","Trade"])
                
                with continent:
                        cont = st.text_input('Updated Continent Name','')
                        Id = st.text_input('Updated Continent ID','')
                        
                        if st.button('Update Continent Id'):
                                
                                try:
                                        update_query = 'UPDATE CONTINENT SET Continent_Id = %s WHERE Continent_Name = %s'
                                        data = (Id,cont)
                                        c.execute(update_query, data)
                                        mydb.commit()
                                        st.success(f'Updated Continent: {cont}, {Id}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")

                        if st.button('Update Continent Name'):
                                
                                try:
                                        update_query = 'UPDATE CONTINENT SET Continent_Name = %s WHERE Continent_Id = %s'
                                        data = (cont, Id)
                                        c.execute(update_query, data)
                                        mydb.commit()
                                        st.success(f'Updated Continent: {cont}, {Id}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                        
                with country:
                        Id = st.text_input("Updated Country Id (Country Table)",'')
                        Name = st.text_input("Updated Country Name",'')
                        Status = st.text_input("Updated Country Status",'')
                        Cont_Id = st.text_input("Updated Continent Id (From Continent Table)",'')
                        
                        if(st.button('Update Country Id')):
                                
                                try:
                                        Update_query = ('Update COUNTRY SET COUNTRY COUNTRY_Id = %s WHERE Country_Name = %s')
                                        data = (Id,Name) 
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Name}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                        
                        if(st.button('Update Country Name')):

                                try:
                                        Update_query = ('Update COUNTRY SET COUNTRY COUNTRY_Name = %s WHERE Country_Id = %s')
                                        data = (Name,Id) 
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Name}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                        if(st.button('Update Country Status')):
                                
                                try:
                                        Update_query = ('Update COUNTRY SET COUNTRY status = %s WHERE Country_Id = %s')
                                        data = (int(Status),Id) 
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Status}')  
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                                                      
                                
                with govta:
                        st.write('If you want to update just one column then keep other values same as before')
                        Id = st.text_input("Updated Country Id For Govt.Account",'')
                        Year = st.text_input("Updated Year",'') 
                        Gdp_Constant_Price = st.text_input("Updated GDP Constant Price",'')
                        Gdp_Current_Price = st.text_input("Updated GDP Current Price",'')
                        GDP_Deflator = st.text_input("Updated GDP Deflator",'')
                        GDP_Per_Captita = st.text_input("Updated GDP Per Capita")
                        Implied_PPP = st.text_input("Updated Implied_PPP")
                        Total_Investments = st.text_input("Updated Total Investments")
                        Gross_National_Savings = st.text_input("Updated Gross National Savings")
                        
                        if(st.button('Update Into Government Account')):
                               
                                try:
                                        Update_query = ('UPDATE government_account SET Country_Id = %s, Year = %s, GDP_Constant_Price = %s, GDP_Current_Price = %s, GDP_Deflator = %s, GDP_Per_Capita = %s, Implied_PPP = %s, Total_Investments = %s, Gross_National_Savings = %s WHERE some_condition = some_value')
                                        data = (Id, int(Year), float(Gdp_Constant_Price), float(Gdp_Current_Price), float(GDP_Deflator), float(GDP_Per_Capita), float(Implied_PPP), float(Total_Investments), float(Gross_National_Savings))
                                        c.execute(Update_query, data)
                                        st.success(f'Updated: {Id}, {Year}, {Gdp_Constant_Price}, {Gdp_Current_Price}, {GDP_Deflator}, {GDP_Per_Capita}, {Implied_PPP}, {Total_Investments}, {Gross_National_Savings}')
                                        
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")

                                        
                with govtf:
                        st.write('If you want to update just one column then keep other values same as before')
                        Id = st.text_input("Updated Country Id For Govt.Finance")
                        Year = st.text_input("Updated Financial Year")
                        Revenue = st.text_input("Updated General Government Revenue")
                        Expediture = st.text_input('Updated General Government Total Expenditure ')
                        GDept = st.text_input('Updated General Government Gross Debt')
                        
                        
                        if(st.button('Update Into Government Finance')):
                                
                                try:
                                        Update_query = ('Update INTO government_finance(Country_Id,Financial_Year,General_Government_Revenue,General_Government_Total_Expenditure,General_Government_Gross_Debt) VALUES(%s,%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(Revenue),float(Expediture),float(GDept))
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Year},{Revenue},{Expenditure},{GDept}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                        
                with mono:
                        st.write('If you want to update just one column then keep other values same as before')
                        Id = st.text_input('Updated Country Id For Monetary')
                        Year = st.text_input('Updated Monetary Year')
                        AvgCP = st.text_input('Updated Inflation Average Consumer Price')
                        EoPC = st.text_input('Updated Inflation End Of Period Of Consumer')
                        
                        if(st.button('Update Monetary')):
                                
                                try:
                                        Update_query = ('Update INTO Monetary(Country_Id,Year,Inflation_Average_Consumer_Price,Inflation_End_Of_Period_Of_Consumer) VALUES(%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(AvgCP),float(EoPC))
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Year},{AvgCP},{EoPC}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                
                with peop:
                        st.write('If you want to update just one column then keep other values same as before')
                        Id = st.text_input('Updated Country Id For People')
                        Year = st.text_input('Updated Population Year')
                        Unemployment_rate = st.text_input('Updated Unemployemnt Rate')
                        Population_rate = st.text_input('Updated Population Rate')
                        
                        if(st.button('Update People')):
                                
                                try:
                                        Update_query = ('Update INTO People(Country_Id,Year,Unemployment_rate,Population_rate) VALUES(%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(Unemployment_rate),float(Population_rate))
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Year},{Unemployment_rate},{Population_rate}')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
                                
                
                with trad:
                        st.write('If you want to update just one column then keep other values same as before')                        
                        Id = st.text_input('Updated Country Id For Trade')
                        Year = st.text_input('Updated Trade Year')
                        VOIGS = st.text_input('Updated Volume Of Import Goods And Services')
                        VOEGS = st.text_input('Updated Volume Of Export Goods And Services')
                        
                        if(st.button('Update Into Trade')):
                                
                                try:
                                        Update_query = ('Update INTO TRADE (Country_ID,Year,Volume_Of_Import_Goods_And_Services,Volume_Of_Export_Goods_And_Services) VALUES(%s,%s,%s,%s)')
                                        data = (Id,int(Year),float(VOIGS),float(VOEGS))
                                        c.execute(Update_query,data)
                                        mydb.commit()
                                        st.success(f'Updated: {Id},{Year},{VOIGS},{VOEGS} ')
                                except mysql.connector.Error as err:
                                        st.write(f"Error: {err}")
        
        
         
                
    
