import pandas as pd

#CREATE DICTIONARY WITH THE COLUMN NAMES AND THE COLUMN TYPES
def create_dictio(df):

    """
    Creates a dictionary mapping column names to their respective data types.

    Iterates over each column in the provided DataFrame and categorizes its data type as 'FLOAT',
    'INT', or 'VARCHAR(50)', based on the actual data type of the column.

    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze for column data types.

    Returns:
    dict: A dictionary with column names as keys and their categorized data types as values.
    """

    column_types = {}

    for e in df:
        if 'float' in str(df[e].dtype):
            column_types[e] = 'FLOAT'
        elif 'int' in str(df[e].dtype):
            column_types[e] = 'INT'
        else:
            column_types[e] = 'VARCHAR(50)'

    return column_types

        

#CREATE TABLES
def create_table(table_name, column_names_types, cursor):
    
    """
    Constructs and executes a SQL query to create a table with specified columns and types.

    This function first drops the table if it already exists, then creates a new table with the
    given name and columns as specified in the 'column_names_types' dictionary.

    Parameters:
    table_name (str): Name of the table to be created.
    column_names_types (dict): Dictionary with column names as keys and their data types as values.
    cursor (database cursor): Cursor object used to interact with the database.

    Returns:
    None: The function executes the SQL query but does not return any value.
    """
    # Drop the table if it exists
    cursor.execute(f'DROP TABLE IF EXISTS `{table_name}`;\n')
    
    # Start the CREATE TABLE statement
    query = f'CREATE TABLE `{table_name}`('

    # Add columns and their types to the query
    for key, value in column_names_types.items():

        query += f'{key} {value}, '

    # Execute the final CREATE TABLE query
    cursor.execute(query[:-2] + ');')


def create_tables(db_structure, cursor):

    """
    Creates tables in a database based on a defined structure and populates them with data.

    For each table in the 'db_structure' dictionary, the function reads data from a CSV file,
    creates the table in the database, and sets up primary and foreign keys as specified.
    It then populates the table with data from the CSV file.

    Parameters:
    db_structure (dict): A dictionary defining the structure of the database. Each key is a table name,
                         and the value is a dictionary specifying primary and foreign keys.
    cursor (database cursor): Cursor object used to interact with the database.

    Returns:
    None: The function executes SQL queries but does not return any value.
    """

    for table, keys in db_structure.items():
        # Read dataframe from CSV
        df = pd.read_csv(f'../../data/4-fill_db/{table}.csv')
        # Create table in the database
        create_table(table, create_dictio(df), cursor)
        
        # Add primary keys if defined
        if 'primary_keys' in keys:
            primary_keys_str = ', '.join([f'`{pk}`' for pk in keys['primary_keys']])
            primary_key_query = f'ALTER TABLE `{table}` ADD PRIMARY KEY ({primary_keys_str});'
            cursor.execute(primary_key_query)

        # Add foreign keys if defined
        if 'foreign_keys' in keys:
            for fk_info in keys['foreign_keys']:
                foreign_key_str = ', '.join([f'`{fk}`' for fk in fk_info['fk']])
                reference_str = f"`{fk_info['reference_table']}` (`{fk_info['reference_column']}`)"
                foreign_key_query = f'ALTER TABLE `{table}` ADD FOREIGN KEY ({foreign_key_str}) REFERENCES {reference_str};'
                cursor.execute(foreign_key_query)

        # Insert values into the table
        insert_values(table, df, cursor)



#INSERT VALUES
def insert_values(table_name, df, cursor):

    """
    Inserts data from a DataFrame into a specified table in the database.

    For each row in the DataFrame, the function constructs and executes an SQL insert query
    to add the row to the specified table.

    Parameters:
    table_name (str): Name of the table in the database where data will be inserted.
    df (pandas.DataFrame): DataFrame containing data to be inserted into the table.
    cursor (database cursor): Cursor object used to interact with the database.

    Returns:
    None: The function executes SQL insert queries but does not return any value.
    """
    
    # Prepare column names for the SQL query
    column_names = ','.join([f'`{col}`' for col in df.columns])

    # Iterate over each row in the DataFrame
    for i in range(df.shape[0]):
        # Get values from the row as a tuple
        values = tuple(df.iloc[i].values)
        
        # Construct and execute the insert query
        cursor.execute(f'INSERT INTO `{table_name}` ({column_names}) VALUES {values};')



