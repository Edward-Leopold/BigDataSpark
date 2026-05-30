from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder \
    .appName("Report 4 - Stores") \
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
stores = spark.read.jdbc(url=pg_url, table="dim_stores", properties=pg_props)

rep_stores = facts.join(stores, "store_id") \
    .groupBy("store_id", "store_name", "store_city", "store_country") \
    .agg(
        sum("sale_total_price").alias("total_revenue"),
        avg("sale_total_price").alias("avg_check")
    )

rep_stores.write.jdbc(url=ch_url, table="default.rep_stores", mode="append", properties=ch_props)
print("Отчет 4 успешно записан в ClickHouse!")
spark.stop()