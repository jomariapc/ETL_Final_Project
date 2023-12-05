from sys import displayhook
import pylab as plt 
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
from fuzzywuzzy import fuzz
from itertools import combinations


# DATA CLEANING


def check_nan(df: pd.DataFrame, show = True) -> None:
    
    """
    Receives a dataframe and returns the % of nulls
     
    It plots it dependent on the show variable which has a default value of True.
    """
    
    nan_cols = df.isna().mean() * 100  # % of null values
    
    nan_cols = nan_cols[nan_cols>0]
    
    displayhook(f'N nan cols: {len(nan_cols)}')
    displayhook(nan_cols)



    # Muestro el gráfico dependiendo de la variable show
    if(show):

        plt.figure(figsize=(10, 6))  # 100X60  pixeles


        sns.heatmap(df.isna(),       
                    yticklabels=False,  
                    cmap='viridis',      
                    cbar=False           
                )

        plt.show();


def column_unification(df):

    """
    Function that remove spaces from rows
    and
    lowercase and replace spaces with _
    in the columns names
    
    """

    #Remove spaces from rows
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    #Lowercase and spaces with _
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]

    return df


def rename_columns(df, dictio):
    """
    Function to change the name of the columns specified in the dictio param
    
    """    
    return df.rename(columns=dictio)


def replace_to(string, change, change_to):

    """
    Function that replace 'change_for' for 'change_to' in string

    It is usefull for the comma character in a  spanish float number, for the dot in an english one

    return the string with the replace function
    
    """

    return string.replace(change, change_to)


def column_counts(df):

    """
    Collects the number of unique values for each column in a DataFrame.

    Iterates through each column, counts unique values, and groups columns by these counts.
    Returns a sorted dictionary mapping the count of unique values to the corresponding column names.

    Parameters:
    df (pandas.DataFrame): DataFrame to evaluate.

    Returns:
    dict: Sorted dictionary with unique value counts as keys and lists of column names as values.
    """

    dictio = {}
    columns = df.columns.tolist()

    for c in columns:
        counts = df[c].value_counts()
        
        dictio[len(counts)] = dictio.get(len(counts), []) + [c]

    return dict(sorted(dictio.items()))


def drop_columns(df, columns):
    """
    Drops specified columns from a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame from which to drop columns.
    columns (list of str): List of column names to be dropped.

    Returns:
    pandas.DataFrame: DataFrame with specified columns removed.
    """
    return df.drop(columns=columns)



def change_type(df, column, type_from, type_to):

    """
    Converts the data type of a specified column in a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the column to convert.
    column (str): The name of the column to convert.
    type_from (str): The original data type of the column.
    type_to (str): The target data type to convert the column to.

    Returns:
    pandas.DataFrame: DataFrame with the column data type changed.
    """

    #If the type from is object
    if type_from == 'object':

        if df[column].dtype == 'object':

            df[column]= pd.to_numeric(df[column]) 

            #If the type to is float
            if type_to=='float':
                df[column] = df[column].astype(float)

            #If the type to is int                
            elif type_to=='int':
                df[column] = df[column].astype(int)

    
    #If the type from is float
    elif type_from == 'float':

        if df[column].dtype == 'float':

            df[column]= pd.to_numeric(df[column]) 

            #If the type to is object
            if type_to=='float':
                df[column] = df[column].astype(float)

            #If the type to is int    
            elif type_to=='int':
                df[column] = df[column].astype(int)

    
    #If the type from is int
    elif type_from == 'int64':

        if df[column].dtype == 'int64':

            df[column]= pd.to_numeric(df[column]) 

            #If the type to is object
            if type_to=='float':
                df[column] = df[column].astype(float)

            #If the type to is int    
            elif type_to=='object':
                df[column] = df[column].astype(object)

    return df



# PROCESSING DATAFRAMES

def group_and_drop_duplicates(df):
    """
    Groups the DataFrame by relevant columns, counts duplicates, and consolidates them.

    For each duplicate found based on 'artículos_ordenados', it combines the 'cantidad'
    into the row with the maximum 'cantidad' and drops the remaining duplicates.

    Parameters:
    df (pandas.DataFrame): The DataFrame to process.

    Returns:
    pandas.DataFrame: The DataFrame with duplicates consolidated and removed.
    """
    # Group by relevant columns and count the number of duplicates
    duplicates = df[df.duplicated(subset=['artículos_ordenados'], keep=False)]

    # Iterate over the duplicates
    for index, row in duplicates.iterrows():
        # Find rows with the same entry in 'artículos_ordenados'
        similar_rows = df[df['artículos_ordenados'] == row['artículos_ordenados']]

        # Find the row with the maximum 'cantidad' (last in order of appearance)
        max_qty_row = similar_rows.loc[similar_rows['cantidad'].idxmax()]

        # Increase the 'cantidad' in that row
        df.at[max_qty_row.name, 'cantidad'] += 1

        # Drop the current duplicate row
        df.drop(index, inplace=True)

    # Reset the indices after the operations
    df.reset_index(drop=True, inplace=True)
    return df


def new_table(df_from, column_to_check, id_column_name, column_name, id_list=[], create_id=True):

    """
    Creates a new DataFrame with unique values from a specified column of an existing DataFrame.
    Optionally generates a list of consecutive IDs or uses a provided list of IDs.

    Parameters:
    df_from (pandas.DataFrame): Source DataFrame.
    column_to_check (str): Column name in df_from to extract unique values from.
    id_column_name (str): Column name for the ID in the new DataFrame.
    column_name (str): Column name for the unique values in the new DataFrame.
    id_list (list, optional): List of IDs to use if create_id is False. Default is an empty list.
    create_id (bool, optional): Flag to generate consecutive IDs. Default is True.

    Returns:
    pandas.DataFrame: A new DataFrame with two columns: IDs and unique values from the specified column.
    """
    # Read the unique values from the specified column
    data = list(df_from[column_to_check].unique())

    # Generate consecutive IDs if create_id is True
    if create_id:
        ids = [str(e + 1) for e in range(len(data))]
    else:
        ids = id_list

    # Create a dictionary with IDs and unique data
    dict_temp = {id_column_name: ids, column_name: data}

    return pd.DataFrame(dict_temp)



#So proud of this function :D
def fill_column(row, df_to_compare, column_to_compare, column_to_change):
    
    """
    Updates a column value in a row based on matching values in another DataFrame.

    This function checks if the value in the specified 'column_to_compare' of the row
    exists in the same column of 'df_to_compare'. If a match is found, it updates the
    value of 'column_to_change' in the row with the corresponding value from 'df_to_compare'.

    Parameters:
    row (pandas.Series): A row of a DataFrame where the update is to be performed.
    df_to_compare (pandas.DataFrame): DataFrame to compare with for matching values.
    column_to_compare (str): Column name to compare for matching values.
    column_to_change (str): Column name in the row to be updated based on the match.

    Returns:
    pandas.Series: The updated row with the modified value in 'column_to_change'.
    """
    # Check if the value exists in the comparison DataFrame
    if row[column_to_compare] in df_to_compare[column_to_compare].values:
        # Find the matching row in the comparison DataFrame
        matching_row = df_to_compare[df_to_compare[column_to_compare] == row[column_to_compare]]
        
        # Update the value of the specified column in the row
        row[column_to_change] = matching_row[column_to_change].values[0]

    return row


def fill_random(len, seed, choice, proportion):

    """
    Generates a random array of specified length using given choices and proportions.

    This function uses a seed for reproducibility and allows specifying the probability
    distribution for the selection of elements.

    Parameters:
    len (int): Length of the array to be generated.
    seed (int): Seed value for the random number generator for reproducibility.
    choice (list): A list of elements from which the random selection will be made.
    proportion (list): A list of probabilities associated with each element in 'choice'.

    Returns:
    numpy.ndarray: An array of randomly selected elements with the specified distribution.
    """

    np.random.seed(seed)

    return np.random.choice(choice, size=len, p=proportion)



def compare_fuzzywuzzy(lst, umbral=90):

    """
    Compares pairs of items in a list for similarity above a defined threshold.

    This function utilizes the FuzzyWuzzy library to compute the similarity ratio
    between each pair of items in the list. Pairs with a similarity ratio exceeding
    the threshold are recorded.

    Parameters:
    lst (list): A list of items to be compared for similarity.
    umbral (int, optional): The threshold for similarity ratio. Default is 90.

    Returns:
    list of tuples: A list containing tuples of the format (item1, item2, similarity_ratio)
    for each pair where the similarity ratio exceeds the threshold.
    """

    coincidencias = []

    for producto1, producto2 in combinations(lst, 2):

        similitud = fuzz.ratio(producto1, producto2)

        if similitud > umbral:

            coincidencias.append((producto1, producto2, similitud))

    return coincidencias


def update_item(cadena, lst, umbral=90):

    """
    Compares a given string against each item in a list using a similarity threshold. 

    If the similarity ratio between the string and an item in the list exceeds the threshold,
    the function returns the matching item from the list. If no matches are found above the
    threshold, the original string is returned.

    Parameters:
    cadena (str): The string to be compared against the list.
    lst (list): A list of strings to compare with.
    umbral (int, optional): The threshold for the similarity ratio. Default is 90.

    Returns:
    str: The matching item from the list if similarity exceeds the threshold, otherwise the original string.
    """

    for i in lst:

        if fuzz.ratio(cadena, i) > umbral:

            return i
        
    return cadena

