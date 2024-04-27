def pipeline():
    import mysql.connector
    from sqlalchemy import create_engine
    import pandas as pd
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="dummy_database"
    )
    engine = create_engine("mysql+mysqlconnector://root:12345@localhost/dummy_database")
    # Create cursor object
    cursor = mydb.cursor()
    delete_query = "DELETE FROM dummy"

    # Execute the DELETE statement
    cursor.execute(delete_query)

    # Commit the changes to the database
    mydb.commit()
    # Execute SELECT query to fetch data from a table
    table_name = "dummy"
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows
    rows = cursor.fetchall()

    # Convert fetched data into a pandas DataFrame
    new_df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

    df = pd.read_excel('Dummy.xlsx',sheet_name='Dummy')
    df['add_column'] = df['a']+df['b']
    df['sub_column'] = df['b']-df['a']
    df.to_sql('dummy', con=engine, if_exists='append', index=False)

pipeline()