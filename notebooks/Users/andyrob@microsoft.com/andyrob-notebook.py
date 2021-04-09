# Databricks notebook source
# If mounting with OAth

# configs = {"fs.azure.account.auth.type": "OAuth",
#        "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
#        "fs.azure.account.oauth2.client.id": "<appId>",
#        "fs.azure.account.oauth2.client.secret": "<clientSecret>",
#        "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<tenant>/oauth2/token",
#        "fs.azure.createRemoteFileSystemDuringInitialization": "true"0}
# 
# dbutils.fs.mount(
# source = "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/folder1",
# mount_point = "/mnt/flightdata",
# extra_configs = configs)

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://datalake@andyrobretailstor.blob.core.windows.net/andyrob",
  mount_point = "/mnt/datalake",
  extra_configs = {"fs.azure.account.key.andyrobretailstor.blob.core.windows.net":dbutils.secrets.get(scope = "datalake", key = "datalakeStorageAccountKey")})




# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/datalake/raw

# COMMAND ----------

dfCustomer = spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/mnt/datalake/raw/RetailCustomer.csv")
dfProduct = spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/mnt/datalake/raw/RetailProducts.csv")
dfStore = spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/mnt/datalake/raw/RetailStores.csv")
dfTxnHeader = spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/mnt/datalake/raw/RetailTransactionHeader.csv")
dfTxnDetail = spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/mnt/datalake/raw/RetailTransactionDetails.csv")


# COMMAND ----------

dfTxnDetail.printSchema()
dfTxnDetail.head(10)


# COMMAND ----------

import pyspark.sql.functions as f

dfAggregate = dfTxnDetail \
.join(dfTxnHeader, dfTxnDetail.TransactionHeaderID == dfTxnHeader.TransactionHeaderID, "inner") \
.join(dfStore, dfTxnHeader.StoreRetailID == dfStore.StoreRetailID, "inner") \
.withColumn("year", f.year(dfTxnHeader.Date.cast("date"))) \
.withColumn("month", f.month(dfTxnHeader.Date.cast("date"))) \
.groupBy("year", "month", dfStore.StoreRetailID).agg(f.sum("TotalAmount").alias("TotalAmount"), f.sum("ShippingCost").alias("ShippingCost"), f.first("Name").alias("StoreName"))



# COMMAND ----------

dfAggregate.coalesce(1).repartition(1).write.option("header", "true").csv("/mnt/datalake/processed/StoreSalesByMonthSpark2.csv")

# COMMAND ----------

