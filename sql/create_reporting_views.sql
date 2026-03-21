-- 1. Executive Summary View
-- Combines Sales and Products with Profit Margin logic
DROP VIEW IF EXISTS view_executive_summary;
CREATE VIEW view_executive_summary AS
SELECT 
    s.transaction_id,
    s.sale_date,
    p.product_name,
    p.category,
    s.quantity,
    s.total_amount AS revenue,
    s.net_profit,
    (s.net_profit / s.total_amount) * 100 AS profit_margin_pct,
    s.store_location
FROM fact_sales s
JOIN dim_products p ON s.product_id = p.product_id;

-- 2. Product Performance View
-- Aggregates sales and profit by product for ranking
DROP VIEW IF EXISTS view_product_performance;
CREATE VIEW view_product_performance AS
SELECT 
    p.product_name,
    p.category,
    SUM(s.quantity) AS units_sold,
    SUM(s.total_amount) AS total_revenue,
    SUM(s.net_profit) AS total_profit,
    AVG(s.net_profit / s.total_amount) * 100 AS avg_margin
FROM fact_sales s
JOIN dim_products p ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category;
