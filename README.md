<p width="80%" align="center">
  <img src="img/head_readme.png" alt="Tepuy Logo">
</p>

# Final Project - ETL for Tepuy Burger

## **About Tepuy Burger**
Founded in 2017, Tepuy Burger is a gourmet burger chain. Known for their quality offerings, they have experienced organic growth, currently boasting three locations in Alicante & Benidorm, with plans for further expansion in the upcoming months.

## **Software Challenges**
Due to their unexpected growth, the company now operates using a myriad of unrelated software solutions.

The ones pertinent to this project include:

- Otter – Manages delivery services across three delivery apps.
- Deliverect – Manages delivery services for an additional delivery app, overlapping some data with Otter.
- Gloria Food - Manages delivery orders from the company's own website.

## **Primary Objective of the Project**
With significant short-term growth anticipated, the company aims to consolidate and comprehend data across software platforms. This project seeks to unify delivery information from various applications (Glovo, Uber Eats, Just Eat, and the company's own website) into a single database. This initiative is a component of a broader project to integrate all of their products and systems.

## **Project Development**
### STEP 1: ETL
#### *EXTRACTION*
***Data Extraction***
- **Data Source 1** – Extracts data from Glovo, Uber Eats, and Tepuy's web delivery service from CSV files.
  - Related document: [I.Data_Extraction.ipynb](https://github.com/jomariapc/ETL_Project/blob/main/src/Jupyter_Notebook/I.Data_Extraction.ipynb)
- **Data Source 2** – Extracts data from Just Eat from CSV files.
- **Data Source 3** – Retrieves data from GloriaFood via API.

#### *TRANSFORM*
***Data Cleaning***
  Cleaning each data source separately.
- Related documents:  
    - [II-S1_Cleaning.Ipynb]() 
    - [I-S2_Cleaning.Ipynb]()
    - [I-S3_Cleaning.Ipynb]()

***EDA (Exploratory Data Analysis)***
- Related documents: 
  - [II-S1_EDA.ipynb]()
  - [II-S2_EDA.ipynb]()

***Data Unification***
Unifying data related to orders.
- Related document: 
  - [III-Data_Unification_Orders.ipynb]()
Unifying data related to order items (products).
- Related document: 
  - [III-Data_Unification_Items.ipynb]()

**Data Cleaning and DataFrame Processing Functions**
- Related document: [PySql.py]()

#### *LOAD*
***Database Structure***
- Analysis, separation, and creation of related tables for database design and loading.
- Related document: [IV-Database_structure.ipynb]()

***Database Population***
- Related document: [V-Database_fill.ipynb]()

**Database Loading Functions**
- Related document: [PySql.py]()

***ERD***
![ERD Image](/img/ERD.png)

### ***STEP 2: VISUALIZATION***

Development of an interactive dashboard divided into three key segments to visualize sales trends, top-selling products, and performance by region. The dashboard allows for date filtering, peak demand identification, and adjustments to operational and marketing strategies.

#### Orders
![Orders](/img/Dashboard/ordenes.png)

#### Top 5 Products
![Products](/img/Dashboard/productos.png)

#### Channels
![Channels](/img/Dashboard/canales.png)

## NEXT STEPS

1. Integration of additional company systems via APIs:
- Tipsi – POS system for order management.
- Cover manager – Software for managing table reservations.
- Mapal reputation – For managing delivery and dine-in reviews.
2. Data upload to a cloud service.
3. With all data loaded and centralized, train machine learning models for sales predictions, product performance, reservation trends, customer behavior analysis, etc.

## Interested in previous work?
- ***First ETL.***
  - Related Document: [link]
- ***Initial Dashboard.***
  - Related Document: [link]
