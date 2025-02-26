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

def query():
    
    NestQ,JoinQ,AggregateQ,Procedure,Trigger,Preval = st.tabs(["Nested Queries","Join Queries","Aggregate Queries","Procedures","Triggers","Privilages"])
                
                #  *************  NESTED QUERIES  ***************
                
    with NestQ:
        Q1,Q2,Q3 = st.tabs(['Query-1','Query-2','Query-3'])
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#########',
            database = 'economy'
        ) 
        c = mydb.cursor()   
                            
        with Q1:
                                
            query_text = '''Syntax : SELECT Country_Id, Population_rate, 2020 AS Year
                                    FROM people
                                    WHERE Country_Id IN (
                                    SELECT Country_Id
                                    FROM Country
                                    WHERE Continent_Id = 'AF')
                                    AND Year = 2020 
                                    UNION
                                    SELECT Country_Id, Population_rate, 2021 AS Year
                                    FROM people
                                    WHERE Country_Id IN (
                                    SELECT Country_Id
                                    FROM Country
                                    WHERE Continent_Id = 'AF')
                                    AND Year = 2021;'''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                        5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                        unsafe_allow_html=True)
                                
            if(st.button('Retrieve The Total Population Rate For Countries In Africa For The Years 2020 And 2021.')):
                
                try:
                    c.execute('''SELECT Country_Id, Population_rate, 2020 AS Year
                                    FROM people
                                    WHERE Country_Id IN (
                                    SELECT Country_Id
                                    FROM Country
                                    WHERE Continent_Id = 'AF')
                                    AND Year = 2020 
                                    UNION
                                    SELECT Country_Id, Population_rate, 2021 AS Year
                                    FROM people
                                    WHERE Country_Id IN (
                                    SELECT Country_Id
                                    FROM Country
                                    WHERE Continent_Id = 'AF')
                                    AND Year = 2021;''')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    df['Year'] = df['Year'].astype(str)
                    df['Year'] = df['Year'].str.replace(',', '')
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                        
        with Q2:
                                        
            query_text = '''Syntax : SELECT Country_Id, General_Government_Revenue
                                FROM government_finance
                                WHERE Country_Id IN (
                                SELECT Country_Id
                                FROM Country
                                WHERE Continent_Id = 'EU'
                                )
                                AND Financial_Year BETWEEN 2018 AND 2022
                                UNION
                                SELECT Country_Id, General_Government_Revenue
                                FROM government_finance
                                WHERE Country_Id IN (
                                SELECT Country_Id
                                FROM Country
                                WHERE Continent_Id = 'EU'
                                )
                                AND Financial_Year BETWEEN 2018 AND 2022;'''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                        5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                        unsafe_allow_html=True)
                                
            if(st.button('Find The Total Government Revenue For Countries In Europe For The Years 2018 To 2022.')):
                
                try:
                    c.execute('''SELECT Country_Id, General_Government_Revenue
                                FROM government_finance
                                WHERE Country_Id IN (
                                SELECT Country_Id
                                FROM Country
                                WHERE Continent_Id = 'EU'
                                )
                                AND Financial_Year BETWEEN 2018 AND 2022
                                UNION
                                SELECT Country_Id, General_Government_Revenue
                                FROM government_finance
                                WHERE Country_Id IN (
                                SELECT Country_Id
                                FROM Country
                                WHERE Continent_Id = 'EU'
                                )
                                AND Financial_Year BETWEEN 2018 AND 2022;''')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                                        
                        
        with Q3:
                                
            query_text = '''Syntax : SELECT c.Country_Name, m.Inflation_End_Of_Period_Of_Consumer
                                    FROM Monetary m
                                    JOIN Country c ON m.Country_Id = c.Country_Id
                                    WHERE c.Continent_Id = 'AS' AND m.Year IN (2019, 2020)
                                    INTERSECT
                                    SELECT c.Country_Name, m.Inflation_End_Of_Period_Of_Consumer
                                    FROM Monetary m
                                    JOIN Country c ON m.Country_Id = c.Country_Id
                                    WHERE c.Continent_Id = 'AS' AND m.Year IN (2019, 2020);'''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                        5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                        unsafe_allow_html=True)
                                
            if(st.button('Inflation In Asian Countries For The Year 2019,2020')):
                
                try:
                    c.execute('''SELECT c.Country_Name, m.Inflation_End_Of_Period_Of_Consumer
                                    FROM Monetary m
                                    JOIN Country c ON m.Country_Id = c.Country_Id
                                    WHERE c.Continent_Id = 'AS' AND m.Year IN (2019, 2020)
                                    INTERSECT
                                    SELECT c.Country_Name, m.Inflation_End_Of_Period_Of_Consumer
                                    FROM Monetary m
                                    JOIN Country c ON m.Country_Id = c.Country_Id
                                    WHERE c.Continent_Id = 'AS' AND m.Year IN (2019, 2020);''')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                        
                #  *************  JOIN QUERIES  ***************
                   
    with JoinQ:
        
        Q1,Q2,Q3 = st.tabs(['Query-1','Query-2','Query-3'])
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#########',
            database = 'economy'
        ) 
        c = mydb.cursor()
                        
        with Q1:
            
            query_text = '''Syntax : SELECT c.Country_Name, p.Population_rate FROM Country c 
                        INNER JOIN people p ON c.Country_Id = p.Country_Id WHERE p.Year = 2019;'''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                            5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                            unsafe_allow_html=True)
                                
            if(st.button('Countries With Their Population Rate For Year 2019')):
                try:
                    c.execute('SELECT c.Country_Name, p.Population_rate FROM Country c INNER JOIN people p ON c.Country_Id = p.Country_Id WHERE p.Year = 2019; ')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")        
                        
                                
                                
                        
        with Q2:

            query_text = '''Syntax : SELECT c.Country_Name, g.GDP_Current_Price FROM Country c 
                                INNER JOIN government_account g ON c.Country_Id = g.Country_Id WHERE g.YEAR = 2022; '''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                            5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                            unsafe_allow_html=True)
                                
            if(st.button('GDP Current Price Of Countries For Year 2022')):
                
                try:
                    c.execute('SELECT c.Country_Name, g.GDP_Current_Price FROM Country c INNER JOIN government_account g ON c.Country_Id = g.Country_Id WHERE g.YEAR = 2022; ')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                        
        with Q3:
                                
            query_text = '''Syntax : SELECT c.Country_Name, cnt.Continent_Name FROM Country c 
                        INNER JOIN Continent cnt ON c.Continent_Id = cnt.Continent_Id;'''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                                        5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                                        unsafe_allow_html=True)
                                
            if(st.button('Country Name With Continent Name')):
                
                try:
                    c.execute('SELECT c.Country_Name, cnt.Continent_Name FROM Country c INNER JOIN Continent cnt ON c.Continent_Id = cnt.Continent_Id;')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                                        
                #  *************  AGGREGATE QUERIES  ***************

                
    with AggregateQ:
        
        Q1,Q2,Q3 = st.tabs(['Query-1','Query-2','Query-3'])
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#########',
            database = 'economy'
        ) 
        c = mydb.cursor()
                        
        with Q1:
                                
            query_text = '''Syntax : SELECT cnt.Continent_Name, AVG(p.Unemployment_rate) AS Avg_Unemployment_Rate 
                                FROM Continent cnt INNER JOIN Country c ON cnt.Continent_Id = c.Continent_Id 
                                INNER JOIN people p ON c.Country_Id = p.Country_Id WHERE p.Year = 2018 
                                GROUP BY cnt.Continent_Name; '''
                                                                
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                            5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                            unsafe_allow_html=True)
                                
            if(st.button('Average Unemployement Rate Per Continent In 2018')):
                
                try:
                    c.execute('SELECT cnt.Continent_Name, AVG(p.Unemployment_rate) AS Avg_Unemployment_Rate FROM Continent cnt INNER JOIN Country c ON cnt.Continent_Id = c.Continent_Id INNER JOIN people p ON c.Country_Id = p.Country_Id WHERE p.Year = 2018 GROUP BY cnt.Continent_Name; ')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                        
        with Q2:
                                
            query_text = '''Syntax : SELECT cnt.Continent_Name, MAX(g.GDP_Current_Price) AS Max_GDP_2021 FROM Continent cnt 
                            INNER JOIN Country c ON cnt.Continent_Id = c.Continent_Id INNER JOIN government_account g 
                            ON c.Country_Id = g.Country_Id WHERE g.YEAR = 2021 GROUP BY cnt.Continent_Name; '''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                            5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                            unsafe_allow_html=True)
                                
            if(st.button('Maximum GDP Of A Continent In 2021')):
                
                try:
                    c.execute('SELECT cnt.Continent_Name, MAX(g.GDP_Current_Price) AS Max_GDP_2021 FROM Continent cnt INNER JOIN Country c ON cnt.Continent_Id = c.Continent_Id INNER JOIN government_account g ON c.Country_Id = g.Country_Id WHERE g.YEAR = 2021 GROUP BY cnt.Continent_Name; ')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]
                    df.columns = columns
                    st.dataframe(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                
                        
        with Q3:
                                
            query_text = '''Syntax : SELECT cnt.Continent_Name, SUM(p.Population_rate) AS Total_Population_2020 
                                    FROM Continent cnt INNER JOIN Country c ON cnt.Continent_Id = c.Continent_Id 
                                    INNER JOIN people p ON c.Country_Id = p.Country_Id WHERE p.Year = 2020 GROUP BY 
                                    cnt.Continent_Name; '''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                        5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                        unsafe_allow_html=True)
                                
            if(st.button('Total Population For Each Continent For Year 2020')):
                
                try:
                    c.execute('SELECT cnt.Continent_Name, SUM(p.Population_rate) AS Total_Population_2020   FROM Continent cnt INNER JOIN Country c ON cnt.Continent_Id = c.Continent_Id INNER JOIN people p ON c.Country_Id = p.Country_Id WHERE p.Year = 2020 GROUP BY cnt.Continent_Name; ')
                    data = c.fetchall()
                    df = pd.DataFrame(data)
                    columns = [i[0] for i in c.description]                      
                    df.columns = columns                     
                    st.dataframe(df)  
                except mysql.connector.Error as err:
                        st.write(f"Error: {err}")                   
                                        
                #  *************  PRIVILAGE QUERIES  ***************                                        
                        
    with Preval:
        
                    
        choice = st.selectbox('Select',['None','Create New User','Remove User','Display User'])
        if choice == 'None':
            pass
            
        if choice == 'Create New User':
            name = st.text_input('Enter new user name')
            passwd = st.text_input('Enter new Password',type='password')
            if(st.button('Create')):
                
                try:
                    c.execute('create user %s@"localhost" identified by %s',(name,passwd))
                    st.write('Created successfully')
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                    
        if choice == 'Remove User':
            name = st.text_input('Enter new user name')
            # passwd = st.text_input('Enter new Password',type='password')
            if(st.button('Remove')):
                
                try:
                    c.execute('DROP USER %s@localhost', (name,))
                    st.write('User removed successfully')
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                        
        if choice == 'Display User':
            
                try:
                    c.execute('SELECT user, host FROM mysql.user;')
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = ['User','Host'])
                    st.write(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                    
        Grant,Revoke = st.tabs(['Grant','Revoke'])
        
        with Grant:
            
            name = st.text_input('Enter the user name for grant')
            choice = st.selectbox('Select For Grant',['None','Display Grants','Insert','Update','Delete','All Privileges'])
            
            if(choice == 'None'):
                pass
            
            if(choice == 'Display Grants'):
                
                try:
                    c.execute("SHOW GRANTS FOR %s@'localhost';",(name,))
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = [f'Grants for {name}@localhost'])
                    st.write(df)
                except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                        
            # ********************   INSERT **************************
            
            if(choice == 'Insert'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.continent TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.country TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.government_account TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.government_finance TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.Monetary TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.people TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"GRANT INSERT ON economy.trade TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")

            # ********************   UPDATE **************************

                        
            if(choice == 'Update'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.continent TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.country TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.government_account TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.government_finance TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.Monetary TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.people TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"GRANT UPDATE ON economy.trade TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
            # ********************   DELETE **************************
                        
                        
            if(choice == 'Delete'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.continent TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.country TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.government_account TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.government_finance TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.Monetary TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.people TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"GRANT DELETE ON economy.trade TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
            # ********************   ALL PRIVILEGES **************************                        
                        
            if(choice == 'All Privileges'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.continent TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.country TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.government_account TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.government_finance TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.Monetary TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.people TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"GRANT ALL PRIVILEGES ON economy.trade TO '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
        with Revoke:
            
            name = st.text_input('Enter the user name for Revoke')
            choice = st.selectbox('Select For Revoke',['None','Display Grants','Insert','Update','Delete','All Privileges'])
            
            if(choice == 'None'):
                pass
            
            if(choice == 'Display Grants'):
                
                try:
                    c.execute("SHOW GRANTS FOR %s@'localhost';",(name,))
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = [f'Grants for {name}@localhost'])
                    st.write(df)
                except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                        
            # ********************   INSERT **************************
            
            if(choice == 'Insert'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.continent FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.country FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.government_account FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.government_finance FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.Monetary FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.people FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"REVOKE INSERT ON economy.trade FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")

            # ********************   UPDATE **************************

                        
            if(choice == 'Update'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.continent FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.country FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.government_account FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.government_finance FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.Monetary FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.people FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"REVOKE UPDATE ON economy.trade FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
            # ********************   DELETE **************************
                        
                        
            if(choice == 'Delete'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.continent FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.country FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.government_account FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.government_finance FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.Monetary FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.people FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"REVOKE DELETE ON economy.trade FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
            # ********************   ALL PRIVILEGES **************************                        
                        
            if(choice == 'All Privileges'):
                
                tables = ["None","Continent","Country","Government Account","Government Finance","Monetary","People","Trade"]
                table = st.selectbox('Select the table',tables)
                
                if table == 'None':
                    pass
                
                if table == 'Continent':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.continent FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Country':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.country FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Account':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.government_account FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Government Finance':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.government_finance FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Monetary':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.Monetary FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'People':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.people FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                if table == 'Trade':
                    
                    try:
                        grant_query = f"REVOKE ALL PRIVILEGES ON economy.trade FROM '{name}'@'localhost';"
                        c.execute(grant_query)
                        st.write('Success')
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")

                                                                                              
                #  *************  PROCEDURE QUERIES  ***************                        
                        
    with Procedure:
        
        Q1,Q2,Q3 = st.tabs(['Procedure-1','Procedure-2','Procedure-3'])
                                
        with Q1:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='#########',
                database = 'economy'
            )
            c = mydb.cursor()
                                
            query_text = '''Syntax : 
                                    CREATE PROCEDURE TopPopulationGrowth(IN analysis_year INT)
                                    BEGIN
                                    SELECT Country_Id, Population_rate
                                    FROM PEOPLE
                                    WHERE Year = analysis_year
                                    ORDER BY Population_rate DESC
                                    LIMIT 5;
                                    END  ;
                                '''
                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                                        5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                                        unsafe_allow_html=True)
                                                                
            procedure_name = 'TopPopulationGrowth'
            check_query = f"SELECT COUNT(*) FROM information_schema.ROUTINES WHERE ROUTINE_NAME = '{procedure_name}' AND ROUTINE_TYPE = 'PROCEDURE';"
            c.execute(check_query)
            procedure_exists = c.fetchone()[0]

            if procedure_exists:
                pass
            else:
                create_query = '''
                                CREATE PROCEDURE TopPopulationGrowth(IN analysis_year INT)
                                BEGIN
                                SELECT Country_Id, Population_rate
                                FROM PEOPLE
                                WHERE Year = analysis_year
                                ORDER BY Population_rate DESC
                                LIMIT 5;
                                END ;'''
                                                
                if(st.button('Retrieve the top 5 countries with the highest population growth rate in a specified year.')):
                    c.execute(create_query)
                    print("Procedure created successfully.")
                                
            Year = st.text_input("Enter Year")
                                
            if st.button('Call TopPopulationGrowth '):
                
                try:
                    c.execute(" CALL TopPopulationGrowth(%s)",[Year])  
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = ['Country ID','Population Rate'])
                    st.write(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
            
            c.close()
                               
                                
                        
        with Q2:
                           
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='#########',
                database = 'economy'
            )
            c = mydb.cursor()

            query_text = '''Syntax : 
                        CREATE PROCEDURE GovernmentRevenueExpenditureRatio(IN country_code VARCHAR(10), IN analysis_year INT)
                        BEGIN
                        SELECT Country_Id, Financial_Year, General_Government_Revenue, General_Government_Total_Expenditure,
                        (General_Government_Revenue / General_Government_Total_Expenditure) AS Revenue_Expenditure_Ratio
                        FROM GOVERNMENT_FINANCE
                        WHERE Country_Id = country_code AND Financial_Year = analysis_year;
                        END  ;'''

                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                                5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                                unsafe_allow_html=True)
                                                                
            procedure_name = 'GovernmentRevenueExpenditureRatio'
            check_query = f"SELECT COUNT(*) FROM information_schema.ROUTINES WHERE ROUTINE_NAME = '{procedure_name}' AND ROUTINE_TYPE = 'PROCEDURE';"
            c.execute(check_query)
            procedure_exists = c.fetchone()[0]

            if procedure_exists:
                pass
            else:
                create_query = '''
                            CREATE PROCEDURE GovernmentRevenueExpenditureRatio(IN country_code VARCHAR(10), IN analysis_year INT)
                        BEGIN
                        SELECT Country_Id, Financial_Year, General_Government_Revenue, General_Government_Total_Expenditure,
                        (General_Government_Revenue / General_Government_Total_Expenditure) AS Revenue_Expenditure_Ratio
                        FROM GOVERNMENT_FINANCE
                        WHERE Country_Id = country_code AND Financial_Year = analysis_year;
                        END  ;'''
                                                
                if(st.button('Get the general government revenue and expenditure ratio for a specific country in a given year.')):
                    c.execute(create_query)
                    print("Procedure created successfully.")
                                
            Country_Id = st.text_input('Enter Country Id')
            Year = st.text_input("Enter The Year")
                                
                                
            if st.button('Call GovernmentRevenueExpenditureRatio '):
                
                try:
                    c.execute(" CALL GovernmentRevenueExpenditureRatio(%s,%s)",[Country_Id,Year])  # Call the stored procedure
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = ['Country Id','Revenue Expenditure Ratio'])
                    st.write(df)
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
                        
            c.close() 
                        
                                
        with Q3:
                         
                mydb = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='#########',
                        database = 'economy'
                    )
                c = mydb.cursor()

                query_text = '''Syntax :
                            CREATE PROCEDURE CalculateAvgUnemploymentRate(IN country_code VARCHAR(10))
                            BEGIN
                            SELECT Country_Id, AVG(Unemployment_rate) AS Avg_Unemployment_Rate
                            FROM PEOPLE
                            WHERE Country_Id = country_code
                            AND Year BETWEEN 2018 AND 2022
                            GROUP BY Country_Id;
                            END ;'''

                                                        
                st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                            5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                            unsafe_allow_html=True)
                                                                
                procedure_name = 'CalculateAvgUnemploymentRate'
                check_query = f"SELECT COUNT(*) FROM information_schema.ROUTINES WHERE ROUTINE_NAME = '{procedure_name}' AND ROUTINE_TYPE = 'PROCEDURE';"
                c.execute(check_query)
                procedure_exists = c.fetchone()[0]

                if procedure_exists:
                    pass
                else:
                    create_query = '''
                                    CREATE PROCEDURE CalculateAvgUnemploymentRate(IN country_code VARCHAR(10))
                            BEGIN
                            SELECT Country_Id, AVG(Unemployment_rate) AS Avg_Unemployment_Rate
                            FROM PEOPLE
                            WHERE Country_Id = country_code
                            AND Year BETWEEN 2018 AND 2022
                            GROUP BY Country_Id;
                            END ;'''
                                                
                    if(st.button('Calculate average unemployment rate for a specific country between 2018 and 2022.')):
                        c.execute(create_query)
                        print("Procedure created successfully.")
                                
                Country_Id = st.text_input('Enter The Country Id')                         
                        
                if st.button('Call CalculateAvgUnemploymentRate '):
                    
                    try:
                        c.execute(" CALL CalculateAvgUnemploymentRate(%s)",[Country_Id]) 
                        data = c.fetchall()
                        df = pd.DataFrame(data,columns=['Country Id','Average Unemployment Rate'])
                        st.write(df)
                        
                    except mysql.connector.Error as err:
                        st.write(f"Error: {err}")
                        
                c.close() 
    
    with Trigger:
        
        Q1,Q2 = st.tabs(['Trigger-1','Trigger-2'])
        
        with Q1:
            
            mydb = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='#########',
                        database = 'economy'
            )
            
            c = mydb.cursor()

            query_text = '''Syntax :
                                CREATE TRIGGER audit_government_account_insert_trigger
                                AFTER INSERT ON GOVERNMENT_ACCOUNT
                                FOR EACH ROW
                                BEGIN
                                    INSERT INTO audit_trail_government (action_type, action_time, country_id, year)
                                    VALUES ('INSERT', NOW(), NEW.Country_Id, NEW.YEAR);
                                END;'''

                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                unsafe_allow_html=True)
                                                                
            if(st.button('Insert Into Government Account Trigger')):
                
                try:
                    create_query = 'SELECT * FROM audit_trail_government'
                    c.execute(create_query) 
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = ['Column Number','Type','Date&Time','Country Id','Year'])
                    df['Year'] = df['Year'].astype(str)
                    df['Year'] = df['Year'].str.replace(',', '')
                    st.write(df)
                
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
            
            c.close()
                
        with Q2:
            
            mydb = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='#########',
                        database = 'economy'
            )
            
            c = mydb.cursor()

            query_text = '''Syntax :
                            DELIMITER //
                                CREATE TRIGGER audit_continent_delete_trigger
                                AFTER DELETE ON CONTINENT
                                FOR EACH ROW
                                BEGIN
                                    INSERT INTO audit_trail_continent (action_type, action_time, continent_id, continent_name)
                                    VALUES ('DELETE', NOW(), OLD.Continent_Id, OLD.Continent_Name);
                                END;
                                //DELIMITER ;'''

                                                        
            st.markdown(f'<div style="background-color: #ffffff; padding: 10px; border-radius: \
                5px; margin-bottom : 10px"><span style="color: black;">{query_text}</span></div>', \
                unsafe_allow_html=True)
                                                                
            if(st.button('Delete From Continent Trigger')):
                
                try:
                    create_query = 'SELECT * FROM audit_trail_Continent'
                    c.execute(create_query)        
                    data = c.fetchall()
                    df = pd.DataFrame(data,columns = ['Type','Date&Time','Continent Id','Content Name'])
                    st.write(df)
                    
                except mysql.connector.Error as err:
                    st.write(f"Error: {err}")
            
            c.close()
                
                
        
        
                    
    
