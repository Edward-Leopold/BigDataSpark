CREATE TABLE IF NOT EXISTS source_data (
    id INT,
    customer_first_name VARCHAR(100),
    customer_last_name VARCHAR(100),
    customer_age INT,
    customer_email VARCHAR(150),
    customer_country VARCHAR(100),
    customer_postal_code VARCHAR(50),
    customer_pet_type VARCHAR(50),
    customer_pet_name VARCHAR(100),
    customer_pet_breed VARCHAR(100),
    seller_first_name VARCHAR(100),
    seller_last_name VARCHAR(100),
    seller_email VARCHAR(150),
    seller_country VARCHAR(100),
    seller_postal_code VARCHAR(50),
    product_name VARCHAR(150),
    product_category VARCHAR(100),
    product_price NUMERIC(10,2),
    product_quantity INT,
    sale_date VARCHAR(50),
    sale_customer_id INT,
    sale_seller_id INT,
    sale_product_id INT,
    sale_quantity INT,
    sale_total_price NUMERIC(10,2),
    store_name VARCHAR(100),
    store_location VARCHAR(150),
    store_city VARCHAR(100),
    store_state VARCHAR(100),
    store_country VARCHAR(100),
    store_phone VARCHAR(50),
    store_email VARCHAR(150),
    pet_category VARCHAR(100),
    product_weight NUMERIC(10,2),
    product_color VARCHAR(50),
    product_size VARCHAR(50),
    product_brand VARCHAR(100),
    product_material VARCHAR(100),
    product_description TEXT,
    product_rating NUMERIC(3,2),
    product_reviews INT,
    product_release_date VARCHAR(50),
    product_expiry_date VARCHAR(50),
    supplier_name VARCHAR(150),
    supplier_contact VARCHAR(150),
    supplier_email VARCHAR(150),
    supplier_phone VARCHAR(50),
    supplier_address VARCHAR(200),
    supplier_city VARCHAR(100),
    supplier_country VARCHAR(100)
);

COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA.csv' DELIMITER ',' CSV HEADER;
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(1).csv' DELIMITER ',' CSV HEADER;
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(2).csv' DELIMITER ',' CSV HEADER;
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(3).csv' DELIMITER ',' CSV HEADER;        
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(4).csv' DELIMITER ',' CSV HEADER;        
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(5).csv' DELIMITER ',' CSV HEADER;        
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(6).csv' DELIMITER ',' CSV HEADER;        
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(7).csv' DELIMITER ',' CSV HEADER;        
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(8).csv' DELIMITER ',' CSV HEADER;        
COPY source_data FROM '/var/lib/postgresql/csv_data/MOCK_DATA(9).csv' DELIMITER ',' CSV HEADER;                                                                                 