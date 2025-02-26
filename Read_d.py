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

def read1():
                tables = ["Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('',tables)
    
                if(table == "Continent"):
                        st.write(''' **Column Description** :''')
                        st.write('''**Continent Id** : Unique Id for all Continents''')
                        st.write('''**Continent Name** : Names of Continents''')
                        st.write('''\n''')
                        
                        try:
                                c.execute('SELECT * FROM CONTINENT ')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Continent ID','Continent Name'])
                                st.dataframe(df)
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")


                if(table == "Country"):
                        st.write(''' **Column Description** :''')
                        st.write('''**Country Id** : Unique Id for all Countries''')
                        st.write('''**Country Name** : Names of Countries''')
                        st.write('''**Status** : \n
                                Status = 0 : Developing Country  Status = 1 : Developed Country''')

                        st.write('''\n''')
                        
                        try:
                                c.execute('SELECT * FROM COUNTRY ')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Country ID','Country Name','Status','Continent Id'])
                                st.dataframe(df)
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")
    
                if(table == "Government Account"):
                        st.write(''' **Column Description** :''')
                        st.write('''**Country Id** : Unique Id for all Countries''')
                        st.write('''**Year** : Year''')
                        st.write('''**GDP Constant Price(National Currency In Billions)** : GDP at constant prices" (also known as "Real GDP" or "GDP in constant dollars")
                        is a measure of a country's economic output or Gross Domestic Product (GDP) that has been adjusted for inflation.''')
        
                        st.write('''**GDP Current Price(US Dollars In Billions)** : "GDP at current prices" or "Nominal GDP" refers to the Gross Domestic Product (GDP) of a 
                                country that is calculated using the current market prices for goods and services produced in a given year''')
        
                        st.write('''**GDP Deflator(Index)** :The GDP deflator, also known as the GDP price deflator or implicit price deflator, is a measure used to calculate 
                                the inflation-adjusted or real GDP by comparing the current market prices of goods and services to a base year ''')
        
                        st.write('''**GDP Per Capita(USD Units)** :Gross Domestic Product (GDP) per capita in USD (United States Dollars) is a measure that represents the 
                                average income or economic output of each individual in a country ''')
        
                        st.write('''**GDP Implied PPP(National Currency / International Dollars)** : GDP at implied purchasing power parity (GDP at implied PPP) is a measure of 
                                Gross Domestic Product (GDP) that has been adjusted for differences in price levels between countries using the concept of 
                                purchasing power parity (PPP)''')
        
                        st.write('''**Total Investments(percent GDP)** : Investment percent in GDP''')
                        st.write('''**Gross National Savings(percent GDP)**: Savings percent after investment''')
        
        # QUERY 
                        try:
                                c.execute('SELECT * FROM government_account')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Country Id','Year','GDP Constant Price','GDP Current Price','GDP Deflator','GDP Per Capita','Implied PPP','Total Investments','Gross National Savings'])
                                df['Year'] = df['Year'].astype(str)
                                df['Year'] = df['Year'].str.replace(',', '')
                                st.dataframe(df)
                                cols  = ['GDP Constant Price','GDP Current Price','GDP Deflator','GDP Per Capita','Implied PPP','Total Investments','Gross National Savings']
                                
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")

        
        
                if(table == "Government Finance"):
        
                        st.write(''' **Column Description** :''')
                        st.write('''**Country Id** : Unique Id for all Countries''')
                        st.write('''**Year** : Year''')
        
                        st.write('''**General Government Revenues(National Currency In Billions)** :General Government Revenues, often referred to as government 
                                revenues, represent the funds collected by a government from various sources to finance its operations and public services.''')
        
                        st.write('''**General Government Total Expenditure(National Currency In Billions)** : General Government Total Expenditure, 
                                often referred to as government expenditure or public expenditure, represents the total amount of money spent by a 
                                government during a specific time period, usually a fiscal year. ''')
        
                        st.write('''**General Government Gross Debt(National Currency In Billions)** : General Government Gross Debt, commonly referred to as 
                                government debt, is the total amount of money that a government owes to creditors, including domestic and foreign lenders, 
                                as a result of borrowing to cover budget deficits or finance various expenditures.''')
        
                        try:
                                c.execute('SELECT * FROM government_finance')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Country ID','Financial Year','General Government Revenues','General Government Total Expenditure','General Government Gross Debt'])
        
                                df['Financial Year'] = df['Financial Year'].astype(str)
                                df['Financial Year'] = df['Financial Year'].str.replace(',', '')
                                st.dataframe(df)
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")
    
                if(table == "Monetary"):
        
                        st.write(''' **Column Description** :''')
                        st.write('''**Country Id** : Unique Id for all Countries''')
                        st.write('''**Year** : Year''')
        
                        st.write('''**Inflation Average Consumer Price(Index)** : Inflation, often measured as the Consumer Price Index (CPI), 
                                is an economic indicator that tracks the average change in the prices of a basket of goods and services commonly 
                                purchased by a typical consumer over time. ''')
        
                        st.write('''**Inflation End Of Period Of Consumer(Index)** : "Inflation End of Period of Consumer" is a reference to a specific 
                                method of measuring inflation that tracks the change in consumer prices over time by considering price levels at the end of a 
                                specified period.''')
        
                        try:
                                c.execute('SELECT * FROM Monetary')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Country ID','Year','Inflation Average Consumer Price','Inflation End Of Period Of Consumer'])
                                df['Year'] = df['Year'].astype(str)
                                df['Year'] = df['Year'].str.replace(',', '')
                                st.dataframe(df)
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")
    
                if(table == "People"):
                        st.write(''' **Column Description** :''')
                        st.write('''**Country Id** : Unique Id for all Countries''')
                        st.write('''**Year** : Year''')
        
                        st.write('''**Unemployment Rate** : The unemployment rate is a key economic indicator that measures the percentage of 
                                the labor force that is unemployed and actively seeking employment.''')
        
                        st.write('''**Population(In Millions)** : Total Population in that year''')
        
                        try:
                                c.execute('SELECT * FROM people')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Country ID','Year','Unemployment Rate','Population'])
                                df['Year'] = df['Year'].astype(str)
                                df['Year'] = df['Year'].str.replace(',', '')
                                st.dataframe(df)
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")
    
                if(table == "Trade"):
        
                        st.write(''' **Column Description** :''')
                        st.write('''**Country Id** : Unique Id for all Countries''')
                        st.write('''**Year** : Year''')

                        st.write('''**Volume Of Import Goods Of And Services(percent change)** : The "Volume of Import Goods and Services (percent change)" 
                                is a measure that tracks the percentage change in the volume or Quantity of goods and services imported by a country over a 
                                specific period.''')
        
                        st.write('''**Volume Of Export Of Goods And Services(percent change)** : The "Volume of Import Goods and Services (percent change)" is 
                                a measure that tracks the percentage change in the volume or Quantity of goods and services imported by a country over a 
                                specific period. ''')
        
                        try:
                                c.execute('SELECT * FROM Trade')
                                data = c.fetchall()
                                df = pd.DataFrame(data,columns = ['Country ID','Year','Volume Of Import Of Goods And Services','Volumne Of Export Of Goods And Services'])
                                df['Year'] = df['Year'].astype(str)
                                df['Year'] = df['Year'].str.replace(',', '')
                                st.dataframe(df)
                        except mysql.connector.Error as err:
                                st.write(f"Error: {err}")

