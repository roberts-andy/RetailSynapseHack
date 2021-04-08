# Challenge 2 - Copy some Data

Hey, the first requirements have hit your inbox! I know you are excited to get going and since we are data people here, let's start by ingesting some data!

Another team has been working on extracting data from some source systems and dropping it into an Azure storage account for you. Aren't they sweet. 

> This is a bit of a hack to get you to data quickly without much supporting infrastructure. Through a similar process we can access data from on-prem systems, cloud databases, service APIs, etc.

This is the URL that the transaction data team has given you for access to this extracted data: 

https://andyrobretaildata.blob.core.windows.net/?sv=2020-02-10&ss=b&srt=sco&sp=rl&se=2022-03-30T22:49:22Z&st=2021-03-30T14:49:22Z&spr=https&sig=yAh%2FzMs6Gaaa0jXQpraE9hWoh8suhF5h%2BiXvDwlrUGo%3D

> Hint: If you are not familiar, this URL is a link to an Azure Blob Storage account using a SAS token. The url can be broken into two parts: "https://andyrobretaildata.blob.core.windows.net/" is the path to the storage account and the query query url parameter "sv=2020-02-10&ss=b&srt=sco&sp=rl&se=2022-03-30T22:49:22Z&st=2021-03-30T14:49:22Z&spr=https&sig=yAh%2FzMs6Gaaa0jXQpraE9hWoh8suhF5h%2BiXvDwlrUGo%3D" is the SAS token. 

## Challenge Requirements: 
* Load the transactional files into your data lake storage 
* Make sure that you can re-run this job on demand (you don't need to schedule it to run on a schedule, but it should be quick to reload the data if necessary)
* Make sure that any resources that you create are stored in your team's branch in the github repo

## Resources and Links

Some Links that may be helpful to you: 
* [Integrate Data with Azure Data Factory or Azure Synapse Pipelines](https://docs.microsoft.com/en-us/learn/modules/data-integration-azure-data-factory/)
* [Azure Data Factory Documentation](https://docs.microsoft.com/en-us/azure/data-factory/)
* [Azure Synapse Analytics Documentation](https://docs.microsoft.com/en-us/azure/synapse-analytics/)
* [Azure Storage Explorer](https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer?tabs=windows)
* [Azure Synapse Copy Data Tool](https://docs.microsoft.com/en-us/azure/data-factory/copy-data-tool)

## [Previous](Challenge-1.md)
## [Next](Challenge-3.md)
