# Databricks notebook source
from pyspark.sql.functions import *
def add_ingestion_col(df):
  df_final=df.withColumn("ingestion_date",current_timestamp())
  return df_final

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema michelin
