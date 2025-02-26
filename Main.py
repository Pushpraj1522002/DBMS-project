import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import itertools

import Read_d
import Create_d
import Delete_d
import Update_d
import Query_d


import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='##########',
    database = 'economy'
)

c = mydb.cursor()

def main():

        Queries,Create,Read,Update,Delete = st.tabs(["Queries","Create","Read","Update","Delete"])        

        with Read:
                Read_d.read1()
                       
        with Update:
                Update_d.update()
                
        with Delete:
                Delete_d.delete()
                
        with Create:
                Create_d.create()
                
        with Queries:
                Query_d.query()
                    
                        
if __name__ == "__main__":
    main()
    
c.close()
mydb.close()
