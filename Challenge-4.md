# Challenge 4 - Data Transformation

Word has gotten out that you have a great platform for data analytics and exploration and the requests are starting to come fast! One common theme is that many people are looking for transaction information rolled up by store by month. There are a number of tools that they will use to connect to this data so if you place the data in a new zone in your data lake they will be able to access it. 

## Challenge Objectives

Create a new file that contains
* RetailStoreID, 
* Store Name, 
* Store City, 
* Store State, 
* Store Country, 
* Store Postal Code, 
* Number of Transactions for that store/month
* Total Transaction Amount for that store/month
* Total Shipping Costs for that store/month

> Hint: Don't pay attention to getting column names or details of the aggregations exactly correct. Really the challenge is about transforming data into a curated data set. 

## Resources and Links

Some Links that may be helpful to you: 
* [Azure Synapse Integration Pipleine Data Flows](https://docs.microsoft.com/en-us/azure/data-factory/control-flow-execute-data-flow-activity)
* [CETAS - Create External Table as Select](https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-cetas)
* [Store Query Results to Storage using Serverless SQL Pool](https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/create-external-table-as-select)
* [Write to Datalake fom Synapse Spark Pool](https://github.com/Azure-Samples/Synapse/blob/main/Notebooks/PySpark/01%20Read%20and%20write%20data%20from%20Azure%20Data%20Lake%20Storage%20Gen2.ipynb)

## [Previous](Challenge-3.md)
## [Next](Challenge-5.md)
