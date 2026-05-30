# scripts/etl_star.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, dense_rank
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("PostgreSQL Star Schema ETL") \
    .config("spark.jars", "/app/jars/postgresql-42.7.10.jar") \
    .getOrCreate()

pg_url = "jdbc:postgresql://postgres:5432/lab2_db"
pg_properties = {
    "user": "admin",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

raw_df = spark.read.jdbc(url=pg_url, table="source_data", properties=pg_properties)

processed_df = raw_df \
    .withColumn("parsed_sale_date", to_date(col("sale_date"), "M/d/yyyy")) \
    .withColumn("parsed_release_date", to_date(col("product_release_date"), "M/d/yyyy")) \
    .withColumn("parsed_expiry_date", to_date(col("product_expiry_date"), "M/d/yyyy"))

dim_customers = processed_df.select(
    col("sale_customer_id").alias("customer_id"),
    col("customer_first_name").alias("first_name"),
    col("customer_last_name").alias("last_name"),
    col("customer_age").alias("age"),
    col("customer_email").alias("email"),
    col("customer_country").alias("country"),
    col("customer_postal_code").alias("postal_code"),
    col("customer_pet_type").alias("pet_type"),
    col("customer_pet_name").alias("pet_name"),
    col("customer_pet_breed").alias("pet_breed")
).filter(col("customer_id").isNotNull()).dropDuplicates(["customer_id"])

dim_sellers = processed_df.select(
    col("sale_seller_id").alias("seller_id"),
    col("seller_first_name").alias("first_name"),
    col("seller_last_name").alias("last_name"),
    col("seller_email").alias("email"),
    col("seller_country").alias("country"),
    col("seller_postal_code").alias("postal_code")
).filter(col("seller_id").isNotNull()).dropDuplicates(["seller_id"])

dim_products = processed_df.select(
    col("sale_product_id").alias("product_id"),
    col("product_name"),
    col("product_category"),
    col("product_price"),
    col("pet_category"),
    col("product_weight"),
    col("product_color"),
    col("product_size"),
    col("product_brand"),
    col("product_material"),
    col("product_description"),
    col("product_rating"),
    col("product_reviews"),
    col("parsed_release_date").alias("product_release_date"),
    col("parsed_expiry_date").alias("product_expiry_date")
).filter(col("product_id").isNotNull()).dropDuplicates(["product_id"])

unique_stores = processed_df.select(
    "store_name", "store_location", "store_city", "store_state", "store_country", "store_phone", "store_email"
).distinct()
store_window = Window.orderBy("store_name", "store_location", "store_city", "store_state", "store_country", "store_phone", "store_email")
dim_stores = unique_stores.withColumn("store_id", dense_rank().over(store_window))

unique_suppliers = processed_df.select(
    "supplier_name", "supplier_contact", "supplier_email", "supplier_phone", "supplier_address", "supplier_city", "supplier_country"
).distinct()

supplier_window = Window.orderBy("supplier_name", "supplier_contact", "supplier_email", "supplier_phone", "supplier_address", "supplier_city", "supplier_country")
dim_suppliers = unique_suppliers.withColumn("supplier_id", dense_rank().over(supplier_window))

fact_sales = processed_df \
    .join(dim_stores, on=["store_name", "store_location", "store_city", "store_state", "store_country", "store_phone", "store_email"], how="inner") \
    .join(dim_suppliers, on=["supplier_name", "supplier_contact", "supplier_email", "supplier_phone", "supplier_address", "supplier_city", "supplier_country"], how="inner") \
    .select(
        col("id").alias("sale_id"),
        col("sale_customer_id").alias("customer_id"),
        col("sale_seller_id").alias("seller_id"),
        col("sale_product_id").alias("product_id"),
        col("store_id"),
        col("supplier_id"),
        col("parsed_sale_date").alias("sale_date"),
        col("sale_quantity"),
        col("sale_total_price")
    ).filter(
        col("sale_id").isNotNull() & 
        col("customer_id").isNotNull() & 
        col("seller_id").isNotNull() & 
        col("product_id").isNotNull()
    ).dropDuplicates(["sale_id"])

dim_customers.write.jdbc(url=pg_url, table="dim_customers", mode="append", properties=pg_properties)
dim_sellers.write.jdbc(url=pg_url, table="dim_sellers", mode="append", properties=pg_properties)
dim_products.write.jdbc(url=pg_url, table="dim_products", mode="append", properties=pg_properties)
dim_stores.write.jdbc(url=pg_url, table="dim_stores", mode="append", properties=pg_properties)
dim_suppliers.write.jdbc(url=pg_url, table="dim_suppliers", mode="append", properties=pg_properties)
fact_sales.write.jdbc(url=pg_url, table="fact_sales", mode="append", properties=pg_properties)

print("Star schema populated in Postgres!")
spark.stop()