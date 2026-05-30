CREATE TABLE IF NOT EXISTS default.rep_products (
    product_id Int32,
    product_name String,
    product_category String,
    total_revenue Decimal(18,2),
    total_sales_quantity Int32
) ENGINE = MergeTree() ORDER BY (total_revenue, product_id);

CREATE TABLE IF NOT EXISTS default.rep_customers (
    customer_id Int32,
    customer_name String,
    country String,
    total_spend Decimal(18,2),
    avg_check Decimal(18,2),
    customer_rank Int32
) ENGINE = MergeTree() ORDER BY (total_spend, customer_id);

CREATE TABLE IF NOT EXISTS default.rep_time (
    year Int32,
    month Int32,
    total_revenue Decimal(18,2),
    total_sales_count Int32,
    avg_order_size Float64
) ENGINE = MergeTree() ORDER BY (year, month);

CREATE TABLE IF NOT EXISTS default.rep_stores (
    store_id Int32,
    store_name String,
    store_city String,
    store_country String,
    total_revenue Decimal(18,2),
    avg_check Decimal(18,2)
) ENGINE = MergeTree() ORDER BY (total_revenue, store_id);

CREATE TABLE IF NOT EXISTS default.rep_suppliers (
    supplier_id Int32,
    supplier_name String,
    supplier_country String,
    total_revenue Decimal(18,2),
    avg_product_price Float64
) ENGINE = MergeTree() ORDER BY (total_revenue, supplier_id);

CREATE TABLE IF NOT EXISTS default.rep_product_quality (
    product_id Int32,
    product_name String,
    product_category String,
    avg_rating Float64,
    total_reviews Int32,
    sales_quantity Int32
) ENGINE = MergeTree() ORDER BY (avg_rating, product_id);