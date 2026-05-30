from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder \
    .appName("Report 1 - Products") \
    .config("spark.jars", "/app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar") \
    .getOrCreate()

pg_url = "jdbc:postgresql://postgres:5432/lab2_db"
pg_props = {"user": "admin", "password": "password", "driver": "org.postgresql.Driver"}

ch_url = "jdbc:clickhouse://clickhouse:8123/default"
ch_props = {
    "user": "default",
    "password": "password",  # Явный пароль
    "driver": "com.clickhouse.jdbc.ClickHouseDriver"
}

facts = spark.read.jdbc(url=pg_url, table="fact_sales", properties=pg_props)
products = spark.read.jdbc(url=pg_url, table="dim_products", properties=pg_props)

rep_products = facts.join(products, "product_id") \
    .groupBy("product_id", "product_name", "product_category") \
    .agg(
        sum("sale_total_price").alias("total_revenue"),
        sum("sale_quantity").alias("total_sales_quantity")
    )

rep_products.write.jdbc(url=ch_url, table="default.rep_products", mode="append", properties=ch_props)
print("Отчет 1 успешно записан в ClickHouse!")
spark.stop()    