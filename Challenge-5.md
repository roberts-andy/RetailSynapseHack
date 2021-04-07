# Challenge 5 - Load Data to Relational Store

Your users and internal customers are extremely impressed with how quickly you have been able to ingest data and curate datasets for them. 

Business is growing out of control! Some of the data that you have been loading is expected to grow very quickly and in preparation for that you would like to load it into a relational data warehouse. Specifically, the data that you copied into the data lake earlier. 

> Note: Again, we are taking a little bit of a shortcut here. It is unlikely that you would take data straight from source systems and load it into a warehouse. You would likely be loading data that came from OLTP sources, cloud services, etc and gone through dimensional modeling exercises and the like before loading into the warehouse. Think through some of the work you did in earlier challenges like joining tables together and writing curated datasets out to storage. In the interest of time for this hackathon we are going to take the data straight from what you loaded into the raw/landing zone of your datalake and send that straight to the data warehouse.  

## Challenge Objectives

Create a new file that contains
* Create a schema in the Azure Synapse Dedicated SQL Pool for your work
* Create 5 tables in your schema: Customer, Product, Store, TransactionDetail, TransactionHeader
* Load the 5 files in your datalake storage account into your new tables
* Descibe the distribution method that you selected for each table. Why did you choose this distribution? What are some pros and cons of that model? 

> We have a sample SQL Script to get you started with the table creation [here](./dw_ddl.sql). Some data load methods will create the table for you. Take a look at any differences between the auto-generated script and the script that is included in this repo. What are the differences? What impact might it have on your performance? 

## Resources and Links

Some Links that may be helpful to you: 
* [Azure Synapse Integration Pipleine Data Flows](https://docs.microsoft.com/en-us/azure/data-factory/control-flow-execute-data-flow-activity)
* [Azure Synapse Integration Pipeline Copy Data Activity](https://docs.microsoft.com/en-us/azure/data-factory/copy-activity-overview)
* [Bulk Load Data into Dedicated SQL Pool](https://docs.microsoft.com/en-us/azure/synapse-analytics/quickstart-load-studio-sql-pool)
* [Designing a Polybase Data Loading Strategy](https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/load-data-overview)
* [Write data from Synapse Spark Pool to SQL Dedicated Pool](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/synapse-spark-sql-pool-import-export)
