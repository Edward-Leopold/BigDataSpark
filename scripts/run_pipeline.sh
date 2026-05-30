#!/bin/bash
echo "=== start ==="
/opt/spark/sbin/start-master.sh
echo "=== sleep 25 ==="
sleep 25

/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar /app/scripts/etl_star.py

echo "-> Отчет 1 (Продукты)..."
/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar /app/scripts/rep1_products.py

echo "-> Отчет 2 (Клиенты)..."
/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar /app/scripts/rep2_customers.py

echo "-> Отчет 3 (Время)..."
/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar /app/scripts/rep3_time.py

echo "-> Отчет 4 (Магазины)..."
/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar /app/scripts/rep4_stores.py

echo "-> Отчет 5 (Поставщики)..."
/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar /app/scripts/rep5_suppliers.py

echo "-> Отчет 6 (Качество)..."
/opt/spark/bin/spark-submit --jars /app/jars/postgresql-42.7.10.jar,/app/jars/clickhouse-jdbc-all-0.9.8.jar /app/scripts/rep6_quality.py

echo "=== end ==="
tail -f /dev/null