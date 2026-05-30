from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg, year, month

spark = SparkSession.builder \
    .appName("Report 3 - Time") \
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

rep_time = facts \
    .withColumn("year", year("sale_date")) \
    .withColumn("month", month("sale_date")) \
    .groupBy("year", "month") \
    .agg(
        sum("sale_total_price").alias("total_revenue"),
        count("sale_id").alias("total_sales_count"),
        avg("sale_quantity").alias("avg_order_size")
    )

rep_time.write.jdbc(url=ch_url, table="default.rep_time", mode="append", properties=ch_props)
print("Отчет 3 успешно записан в ClickHouse!")
spark.stop()