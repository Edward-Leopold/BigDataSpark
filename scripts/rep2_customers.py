from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, concat, lit, dense_rank, desc
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("Report 2 - Customers") \
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
customers = spark.read.jdbc(url=pg_url, table="dim_customers", properties=pg_props)

cust_window = Window.orderBy(desc("total_spend"))
rep_customers = facts.join(customers, "customer_id") \
    .groupBy("customer_id", concat("first_name", lit(" "), "last_name").alias("customer_name"), "country") \
    .agg(
        sum("sale_total_price").alias("total_spend"),
        avg("sale_total_price").alias("avg_check")
    ) \
    .withColumn("customer_rank", dense_rank().over(cust_window))

rep_customers.write.jdbc(url=ch_url, table="default.rep_customers", mode="append", properties=ch_props)
print("Отчет 2 успешно записан в ClickHouse!")
spark.stop()