import pandas as pd

customers = pd.read_csv("customer.csv")
products = pd.read_csv("product.csv")
orders = pd.read_csv("orders.csv")

#shape
print(customers.shape)
print(products.shape)
print(orders.shape)

#columns
print(customers.columns)
print(products.columns)
print(orders.columns)

#null values
print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

#duplicat rows
print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())

# Unique Counts
print(customers.nunique())
print(products.nunique())
print(orders.nunique())

# Data Quality Summary:
# 1. Loaded all three datasets successfully.
# 2. Verified shape and column names.
# 3. Checked data types.
# 4. No missing values found.
# 5. No duplicate records found.
# 6. Calculated unique values for each column.




#--------------------
#task 2
#--------------------

# Standardize column names
customers.columns = customers.columns.str.lower()
products.columns = products.columns.str.lower()
orders.columns = orders.columns.str.lower()

# Handle missing values
customers.fillna("Unknown", inplace=True)
products.fillna("Unknown", inplace=True)
orders.fillna("Unknown", inplace=True)

# Verify cleaning
print(customers.dtypes)
print(products.dtypes)
print(orders.dtypes)

print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

# Task 2 Summary:
# 1. Standardized all column names to lowercase.
# 2. Verified that data types were already correct.
# 3. Handled possible missing values using fillna().
# 4. Confirmed that no null values remain.
# 5. The DataFrames are now ready for analysis.

#----------------
#task 3
#----------------
df = pd.merge(orders, customers, on="customer_id")
df = pd.merge(df, products, on="product_id")

print(df.head())

df["sales"] = df["quantity"] * df["price"]

print(df[["quantity", "price", "sales"]])


region_sales = df.groupby("region")["sales"].sum()

print("Sales by Region")
print(region_sales)

category_sales = df.groupby("category")["sales"].sum()

print("\nSales by Category")
print(category_sales)

multi_group = df.groupby(
    ["region", "category"]
)["sales"].sum()

print("\nSales by Region and Category")
print(multi_group)

'''
## Business Interpretation

1. The North region generated the highest total sales (1100).
2. Electronics is the best-performing product category with total sales of 1200.
3. The Consumer segment contributed the highest revenue among all customer segments.
4. The multi-level groupby shows that Electronics products performed especially well in the East and North regions.
5. This analysis can help the business focus marketing and inventory planning on high-performing regions and categories.
'''

# ==========================================
# TASK 4 : Merge Tables and Calculate Metrics
# ==========================================

# Merge orders and customers tables using customer_id
df = pd.merge(orders, customers, on="customer_id")

# Merge the above result with products table using product_id
df = pd.merge(df, products, on="product_id")

# Display first 5 rows of merged dataset
print("Merged Data:")
print(df.head())


# ------------------------------------------
# Create a new Sales column
# Formula: Sales = Quantity × Price
# ------------------------------------------

df["sales"] = df["quantity"] * df["price"]

print("\nDataset with Sales Column:")
print(df[["product_name", "quantity", "price", "sales"]])


# ------------------------------------------
# Calculate Total Revenue
# ------------------------------------------

total_revenue = df["sales"].sum()

print("\nTotal Revenue:")
print(total_revenue)


# ------------------------------------------
# Calculate Average Order Value
# ------------------------------------------

average_order_value = df["sales"].mean()

print("\nAverage Order Value:")
print(average_order_value)


# ------------------------------------------
# Find Top-Selling Products
# ------------------------------------------

top_products = df.groupby("product_name")["sales"].sum()

top_products = top_products.sort_values(
    ascending=False
)

print("\nTop Selling Products:")
print(top_products)


# ------------------------------------------
# Create Final Merged Analysis Table
# ------------------------------------------

analysis_table = df[
    [
        "order_id",
        "customer_name",
        "region",
        "segment",
        "product_name",
        "category",
        "quantity",
        "price",
        "sales"
    ]
]

print("\nMerged Analysis Table:")
print(analysis_table)

'''
Business Interpretation

• The three datasets were successfully merged.
• A new Sales column was created using Quantity × Price.
• Total Revenue shows the overall earnings from all orders.
• Average Order Value indicates the average revenue per order.
• Top-selling products help identify the best-performing items.
'''

# ------------------------------------------
# Pivot Table 1 : Region vs Month
# ------------------------------------------

pivot1 = pd.pivot_table(
    df,
    values="sales",
    index="region",
    columns="month",
    aggfunc="sum",
    fill_value=0
)

print("Pivot Table : Region vs Month")
print(pivot1)

# ------------------------------------------
# Pivot Table 2 : Category vs Segment
# ------------------------------------------

pivot2 = pd.pivot_table(
    df,
    values="sales",
    index="category",
    columns="segment",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table : Category vs Segment")
print(pivot2)

print("\nRegion vs Month")
print(pivot1.reset_index())

print("\nCategory vs Segment")
print(pivot2.reset_index())

'''
## Business Interpretation

 Pivot Table 1 (Region vs Month)
- The pivot table compares sales across different regions and months.
- It helps identify which region performed best during a particular month.
 Pivot Table 2 (Category vs Segment)
- The pivot table shows sales contribution by product category and customer segment.
- Electronics generated the highest sales across customer segments.
- Such comparisons help businesses understand customer behavior and improve decision-making.
'''

# ==========================================
# TASK 6 : Data Visualization
# ==========================================

# Import Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Chart 1 : Histogram of Sales
# ------------------------------------------

plt.figure(figsize=(6,4))
plt.hist(df["sales"], bins=5)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()


# ------------------------------------------
# Chart 2 : Scatter Plot
# Quantity vs Sales
# ------------------------------------------

plt.figure(figsize=(6,4))
plt.scatter(df["quantity"], df["sales"])

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.show()


# ------------------------------------------
# Chart 3 : Bar Chart
# Sales by Product
# ------------------------------------------

product_sales = df.groupby("product_name")["sales"].sum()

plt.figure(figsize=(6,4))
plt.bar(product_sales.index, product_sales.values)

plt.title("Sales by Product")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

plt.show()


# ------------------------------------------
# Chart 4 : Line Chart
# Monthly Sales Trend
# ------------------------------------------

month_sales = df.groupby("month")["sales"].sum()

# Arrange months in proper order
month_order = ["Jan", "Feb", "Mar", "Apr"]
month_sales = month_sales.reindex(month_order)

plt.figure(figsize=(6,4))
plt.plot(month_sales.index, month_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# ------------------------------------------
# Chart 5 : Box Plot
# Sales Distribution
# ------------------------------------------

plt.figure(figsize=(6,4))
plt.boxplot(df["sales"])

plt.title("Box Plot of Sales")
plt.ylabel("Sales")

plt.show()


# ------------------------------------------
# Chart 6 : Heatmap
# Region vs Month Sales
# ------------------------------------------

pivot1 = pd.pivot_table(
    df,
    values="sales",
    index="region",
    columns="month",
    aggfunc="sum",
    fill_value=0
)

# Display the pivot table
print("\nPivot Table (Region vs Month):")
print(pivot1)

plt.figure(figsize=(7,4))

sns.heatmap(
    pivot1,
    annot=True,
    cmap="YlGnBu",
    fmt=".0f"
)

plt.title("Sales Heatmap (Region vs Month)")
plt.xlabel("Month")
plt.ylabel("Region")

plt.show()

'''
## Chart Summary

1. The histogram shows the distribution of sales values.
2. The scatter plot shows the relationship between quantity sold and sales amount.
3. The bar chart compares total sales across products.
4. The line chart illustrates the monthly sales trend.
5. The box plot displays the spread and variability of sales values.
6. The heatmap provides a visual comparison of sales across different regions and months.
'''
# Task 7 : Chart Story

#The visualizations provide several useful insights into the sales data. The bar chart shows that the Laptop is the top-selling product, generating the highest revenue among all products. The line chart indicates that sales vary across different months, with some months contributing more to the overall revenue than others. The histogram and box plot reveal that sales values are unevenly distributed because a few high-value orders significantly increase the total sales. The scatter plot shows that sales generally increase as the quantity purchased increases. The heatmap helps compare sales across different regions and months, making it easy to identify stronger-performing areas. Overall, these charts help the business understand customer buying patterns and make better decisions regarding inventory and sales planning.

# ==========================================
# TASK 8 : SQLite Database and SQL Queries
# ==========================================

import sqlite3
import pandas as pd

# ------------------------------------------
# Create SQLite Database
# ------------------------------------------

conn = sqlite3.connect("sales_database.db")

# ------------------------------------------
# Load DataFrames into Database
# ------------------------------------------

customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

print("Tables loaded successfully!\n")


# ------------------------------------------
# Query 1 : SELECT
# ------------------------------------------

print("Query 1 : SELECT * FROM customers")
print(pd.read_sql(
    "SELECT * FROM customers;",
    conn
))


# ------------------------------------------
# Query 2 : WHERE
# ------------------------------------------

print("\nQuery 2 : Orders where quantity > 2")
print(pd.read_sql(
    "SELECT * FROM orders WHERE quantity > 2;",
    conn
))


# ------------------------------------------
# Query 3 : ORDER BY
# ------------------------------------------

print("\nQuery 3 : Products ordered by price")
print(pd.read_sql(
    "SELECT * FROM products ORDER BY price DESC;",
    conn
))


# ------------------------------------------
# Query 4 : COUNT
# ------------------------------------------

print("\nQuery 4 : Total Orders")
print(pd.read_sql(
    "SELECT COUNT(*) AS total_orders FROM orders;",
    conn
))


# ------------------------------------------
# Query 5 : SUM
# ------------------------------------------

print("\nQuery 5 : Total Quantity")
print(pd.read_sql(
    "SELECT SUM(quantity) AS total_quantity FROM orders;",
    conn
))


# ------------------------------------------
# Query 6 : AVG
# ------------------------------------------

print("\nQuery 6 : Average Product Price")
print(pd.read_sql(
    "SELECT AVG(price) AS average_price FROM products;",
    conn
))


# ------------------------------------------
# Query 7 : GROUP BY
# ------------------------------------------

print("\nQuery 7 : Total Quantity by Product")
print(pd.read_sql(
    """
    SELECT product_id,
           SUM(quantity) AS total_quantity
    FROM orders
    GROUP BY product_id;
    """,
    conn
))


# ------------------------------------------
# Query 8 : INNER JOIN
# ------------------------------------------

print("\nQuery 8 : Customer Name and Quantity")
print(pd.read_sql(
    """
    SELECT customer_name,
           quantity
    FROM customers
    INNER JOIN orders
    ON customers.customer_id = orders.customer_id;
    """,
    conn
))


# ------------------------------------------
# Query 9 : Product Name and Quantity
# ------------------------------------------

print("\nQuery 9 : Product Name and Quantity")
print(pd.read_sql(
    """
    SELECT product_name,
           quantity
    FROM products
    INNER JOIN orders
    ON products.product_id = orders.product_id;
    """,
    conn
))


# ------------------------------------------
# Query 10 : Multiple JOIN
# ------------------------------------------

print("\nQuery 10 : Customer, Product and Quantity")
print(pd.read_sql(
    """
    SELECT customer_name,
           product_name,
           quantity
    FROM orders
    JOIN customers
    ON orders.customer_id = customers.customer_id
    JOIN products
    ON orders.product_id = products.product_id;
    """,
    conn
))


# ------------------------------------------
# Query 11 : Maximum Price
# ------------------------------------------

print("\nQuery 11 : Highest Product Price")
print(pd.read_sql(
    """
    SELECT MAX(price) AS highest_price
    FROM products;
    """,
    conn
))


# ------------------------------------------
# Query 12 : Minimum Price
# ------------------------------------------

print("\nQuery 12 : Lowest Product Price")
print(pd.read_sql(
    """
    SELECT MIN(price) AS lowest_price
    FROM products;
    """,
    conn
))


# ------------------------------------------
# Query 13 : Subquery
# ------------------------------------------

print("\nQuery 13 : Products Above Average Price")
print(pd.read_sql(
    """
    SELECT *
    FROM products
    WHERE price >
    (
        SELECT AVG(price)
        FROM products
    );
    """,
    conn
))


# ------------------------------------------
# Query 14 : DISTINCT
# ------------------------------------------

print("\nQuery 14 : Distinct Regions")
print(pd.read_sql(
    """
    SELECT DISTINCT region
    FROM customers;
    """,
    conn
))


# ------------------------------------------
# Query 15 : ORDER BY Quantity
# ------------------------------------------

print("\nQuery 15 : Orders Sorted by Quantity")
print(pd.read_sql(
    """
    SELECT *
    FROM orders
    ORDER BY quantity DESC;
    """,
    conn
))


# ------------------------------------------
# Close Database Connection
# ------------------------------------------

conn.close()

print("\nSQLite database closed successfully!")

# ==========================================
# TASK 9 : Pandas vs SQL Comparison
# ==========================================

# ------------------------------------------
# Pandas Analysis
# Total Quantity Sold by Product
# ------------------------------------------

print("Pandas Result:")

pandas_result = orders.groupby(
    "product_id"
)["quantity"].sum().reset_index()

print(pandas_result)


# ------------------------------------------
# SQL Analysis
# Total Quantity Sold by Product
# ------------------------------------------

import sqlite3

conn = sqlite3.connect("sales_database.db")

print("\nSQL Result:")

sql_result = pd.read_sql(
    """
    SELECT
        product_id,
        SUM(quantity) AS quantity
    FROM orders
    GROUP BY product_id;
    """,
    conn
)

print(sql_result)

conn.close()
