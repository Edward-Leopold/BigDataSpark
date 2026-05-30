from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder \
    .appName("Report 5 - Suppliers") \
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
suppliers = spark.read.jdbc(url=pg_url, table="dim_suppliers", properties=pg_props)
products = spark.read.jdbc(url=pg_url, table="dim_products", properties=pg_props)

rep_suppliers = facts.join(suppliers, "supplier_id").join(products, "product_id") \
    .groupBy("supplier_id", "supplier_name", "supplier_country") \
    .agg(
        sum("sale_total_price").alias("total_revenue"),
        avg("product_price").alias("avg_product_price")
    )

rep_suppliers.write.jdbc(url=ch_url, table="default.rep_suppliers", mode="append", properties=ch_props)
print("Отчет 5 успешно записан в ClickHouse!")
spark.stop()