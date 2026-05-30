from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder \
    .appName("Report 6 - Product Quality") \
    .config("spark.jars", "/app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar") \
    .getOrCreate()

pg_url = "jdbc:postgresql://postgres:5432/lab2_db"
pg_props = {"user": "admin", "password": "password", "driver": "org.postgresql.Driver"}

ch_url = "jdbc:clickhouse://clickhouse:8123/default"
ch_props = {
    "user": "default",
    "password": "password",
    "driver": "com.clickhouse.jdbc.ClickHouseDriver"
}

facts = spark.read.jdbc(url=pg_url, table="fact_sales", properties=pg_props)
products = spark.read.jdbc(url=pg_url, table="dim_products", properties=pg_props)

rep_product_quality = facts.join(products, "product_id") \
    .groupBy("product_id", "product_name", "product_category") \
    .agg(
        avg("product_rating").alias("avg_rating"),
        sum("product_reviews").alias("total_reviews"),
        sum("sale_quantity").alias("sales_quantity")
    )

rep_product_quality.write.jdbc(url=ch_url, table="default.rep_product_quality", mode="append", properties=ch_props)
print("Отчет 6 успешно записан в ClickHouse!")
spark.stop()