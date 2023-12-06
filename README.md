<p width="80%" >
  <img src="img/head_readme.png" alt="Tepuy Logo">
</p>

# Final Project - ETL - Tepuy Burger

## **About Tepuy Burger**
Tepuy Burger is a hamburger chain created in 2017. After an organic and constant growth based on the quality of their burgers, today it has 3 restaurants in Alicante & Benidorm, and expects to extend their business in the next months.

## **Software Issues**
Based in their not expected growth, this enterprise today manages its business with several softwares that have nothing to do with each other.

The ones that are relevant to the current project are the following:

- Otter – To manage delivery services for three of the delivery apps.
- Deliverect – To manage delivery services for one of the delivery apps. It came after Otter, so they repeat some of the information.
- Gloria Food - To manage delivery services from the own website. 

## **Project Main Objective**
As a strong growth is expected in the short term, the enterprise is trying to join and understand all the information from the SW platforms, and this project aims to integrate in one single database the delivery information from different applications (Glovo, Uber eats, Just Eat, and own web). This is a small part of the total integration project of all their products and systems.

## **Project Development**

### *EXTRACTION*
#### ***Data Extraction***
- **Step 1** – Data extraction (Glovo, Uber Eats, and Tepuy web delivery information from a CSV file)
  - Related document: [I.Data_Extraction.ipynb](https://github.com/jomariapc/ETL_Project/blob/main/src/Jupyter_Notebook/I.Data_Extraction.ipynb)
- **Step 2** – Data extraction (Just Eat information extraction from a CSV files)
- **Step 3** – Data extraction (GloriaFood information extraction from API)

### *TRANSFORM*
#### ***Data Cleaning***
Limpieza de cada una de las fuentes de datos por separado.
- Related documents:  
    - [I-S1_Cleaning.Ipynb]() 
    - [I-S2_Cleaning.Ipynb]()
    - [I-S3_Cleaning.Ipynb]()

#### ***EDA (Exploratory Data Analysis) ***
- Related documents: [III.Data_Unification.ipynb]()

#### ***Database Analysis***
- Related document: [IV.Database.ipynb](https://github.com/jomariapc/ETL_Project/blob/main/src/Jupyter_Notebook/IV.Database.ipynb)

### *LOADING*
#### ***Database Filling***
- Related document: [V.Database_filling.ipynb](https://github.com/jomariapc/ETL_Project/blob/main/src/Jupyter_Notebook/V.Database_filling.ipynb)

#### ***ERD***
![ERD Image](/img/ERD.png)


#### ***Extra information***

##### ***Python files***
Data Cleaning and Processing DataFrames functions
- Related document: [PyPower.py](https://github.com/jomariapc/ETL_Project/blob/main/src/Python/PyPower.py)

Database loading functions
- Related document: [PySql.py](https://github.com/jomariapc/ETL_Project/blob/main/src/Python/PySql.py)


#### *** Next steps ***

1. Visualization of the information obtained through an interactive dashboard.
- Related repo: [Viz_Project](https://github.com/jomariapc/Viz_Project)

2. Integration through API of the other systems used by the company:

- Gloria foods – Restaurant order system
- Tipsi – TPV system to manage orders
- Cover manager – Software to manage table reservations
- Mapal reputation – To manage delivery and eat in reviews.