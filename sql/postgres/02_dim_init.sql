CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    email VARCHAR(150),
    country VARCHAR(100),
    postal_code VARCHAR(50),
    pet_type VARCHAR(50),
    pet_name VARCHAR(100),
    pet_breed VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_sellers (
    seller_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(150),
    country VARCHAR(100),
    postal_code VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(150),
    product_category VARCHAR(100),
    product_price NUMERIC(10,2),
    pet_category VARCHAR(100),
    product_weight NUMERIC(10,2),
    product_color VARCHAR(50),
    product_size VARCHAR(50),
    product_brand VARCHAR(100),
    product_material VARCHAR(100),
    product_description TEXT,
    product_rating NUMERIC(3,2),
    product_reviews INT,
    product_release_date DATE,
    product_expiry_date DATE
);

CREATE TABLE IF NOT EXISTS dim_stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    store_location VARCHAR(150),
    store_city VARCHAR(100),
    store_state VARCHAR(100),
    store_country VARCHAR(100),
    store_phone VARCHAR(50),
    store_email VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS dim_suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(150),
    supplier_contact VARCHAR(150),
    supplier_email VARCHAR(150),
    supplier_phone VARCHAR(50),
    supplier_address VARCHAR(200),
    supplier_city VARCHAR(100),
    supplier_country VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id INT PRIMARY KEY,
    customer_id INT REFERENCES dim_customers(customer_id),
    seller_id INT REFERENCES dim_sellers(seller_id),
    product_id INT REFERENCES dim_products(product_id),
    store_id INT REFERENCES dim_stores(store_id),
    supplier_id INT REFERENCES dim_suppliers(supplier_id),
    sale_date DATE,
    sale_quantity INT,
    sale_total_price NUMERIC(10,2)
);