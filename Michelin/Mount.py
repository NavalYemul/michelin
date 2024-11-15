# Databricks notebook source
dbutils.fs.mount(
  source = "wasbs://<container>@<storage_account>.blob.core.windows.net",
  mount_point = "/mnt/<storage_account>/<container>",
  extra_configs = {"fs.azure.account.key.<storage_account>.blob.core.windows.net":"<Access Key>"})

#this is the final mounting
dbutils.fs.mount(
  source = "wasbs://raw@adls.blob.core.windows.net",
  mount_point = "/mnt/<storage_account>/<container>",
  extra_configs = {"fs.azure.account.key.<storage_account>.blob.core.windows.net":"<Access Key>"})
