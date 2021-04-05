# Challenge 2 - Copy some Data

Hey, the first requirements have hit your inbox! I know you are excited to get going and since we are data people here, let's start but ingesting some data!

Another team has been working on extracting data from some source systems an dropping it into an Azure storage account for you. Aren't they sweet. 

> This is a bit of a hack to get you to data quickly without much supporting infrastructure. Through a similar process we can access data from on-prem systems, cloud databases, service APIs, etc.

This is the URL that the transaction data team has given you for access to this extracted data: 

https://andyrobretaildata.blob.core.windows.net/?sv=2020-02-10&ss=b&srt=sco&sp=rl&se=2022-03-30T22:49:22Z&st=2021-03-30T14:49:22Z&spr=https&sig=yAh%2FzMs6Gaaa0jXQpraE9hWoh8suhF5h%2BiXvDwlrUGo%3D

Challenge Requirements: 
* Load the transactional files into your data lake storage 
* Make sure that you can re-run this job on demand (you don't need to schedule it to run on a schedule, but it should be quick to reload the data if necessary)
* make sure that any resources that you create are stored in your team's branch in the github repo