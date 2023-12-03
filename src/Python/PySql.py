import pandas as pd

#CREATE DICTIONARY WITH THE COLUMN NAMES AND THE COLUMN TYPES
def create_dictio(df):

    column_types= {}

    for e in df:

        if ('float' in str(df[e].dtype)):
            column_types[e]='FLOAT'

        elif ('int' in str(df[e].dtype)):
            column_types[e]='INT'

        else:
            column_types[e]='VARCHAR(50)'
        

    return column_types
        

#CREATE TABLES
def create_table(table_name, column_names_types, cursor):
    """
    Function that receives the name of the table "table_name", 
    a dictionary "column_names_types" with the format 
    key (column name): value(column type)  

    Returns the string with the query for create table

    """

    cursor.execute(f'DROP TABLE IF EXISTS `{table_name}`;\n')
    
    # Add CREATE TABLE statement
    query = f'CREATE TABLE `{table_name}`('

    # Add all the columns to the string from the dictionary
    for key, value in column_names_types.items():

        query += f'{key} {value}, '

    cursor.execute(query[:-2] + ');')

def create_tables(db_structure, cursor):
        
    for table, keys in db_structure.items():
        #Read dataframe
        df = pd.read_csv(f'../../data/4-fill_db/{table}.csv')
        #Create table with dataframe
        create_table(table, create_dictio(df), cursor)
        
        # Check and add primary keys
        if 'primary_keys' in keys:
            primary_keys_str = ', '.join([f'`{pk}`' for pk in keys['primary_keys']])
            primary_key_query = f'ALTER TABLE `{table}` ADD PRIMARY KEY ({primary_keys_str});'
            cursor.execute(primary_key_query)

        if 'foreign_keys' in keys:
            for fk_info in keys['foreign_keys']:
                foreign_key_str = ', '.join([f'`{fk}`' for fk in fk_info['fk']])
                reference_str = f"`{fk_info['reference_table']}` (`{fk_info['reference_column']}`)"
                foreign_key_query = f'ALTER TABLE `{table}` ADD FOREIGN KEY ({foreign_key_str}) REFERENCES {reference_str};'
                cursor.execute(foreign_key_query)

        #Insert values
        insert_values(table, df, cursor)


#INSERT VALUES
def insert_values(table_name, df, cursor):

    column_names = ','.join(df.columns)

    # For each row

    for i in range(df.shape[0]):   
        
        values = tuple(df.iloc[i].values)   
        
        cursor.execute(f'insert into `{table_name}` ({column_names}) values {values};')


