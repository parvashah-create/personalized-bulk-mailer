import sqlite3
import os
import pandas as pd




def get_db(db):
    # eastablish connection with db
    db_path = os.getcwd() + "/database/{}".format(db)
    conn = sqlite3.connect(db_path,check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor


def get_roles(roles):
    conn, cur = get_db("neu_info.db") 


    # Build the SQL query with a placeholder for the list of values
    sql_query = "SELECT * FROM mail_info WHERE role IN ({})".format(','.join(['?']*len(roles)))

    # Execute the query with the list of values as parameters
    roles_df = pd.read_sql_query(sql_query, conn, params=roles)

    # Close the database connection
    conn.close()
    
    return roles_df


