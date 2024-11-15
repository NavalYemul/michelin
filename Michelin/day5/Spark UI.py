# Databricks notebook source
spark is lazy evaluted 

# COMMAND ----------

df=spark.table("michelin.silver.sales")

# COMMAND ----------

df.filter("customer_id=1")

# COMMAND ----------

df.filter("customer_id=1").display()

# COMMAND ----------

Spark Transformation: 
  1. Narrow: filter
  2. Wide(Shuffle Tranformation): groupby,join

# COMMAND ----------

df.groupBy("customer_id").count()

# COMMAND ----------

df.groupBy("customer_id").count().display()

# COMMAND ----------


