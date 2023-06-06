## Apache Airflow ETL Data Pipeline

My workplaces current CRM is poorly managed and myself and some coworkers wanted to create our own dashboards so that we could understand our data from working with clients and stores much better. So I set off on building the data pipeline myself. 

### Diagram showing the different technologies used:
![shop_data_pipeline_project_diagram](https://github.com/speropoulos/airflow_project/blob/main/sharecrm%20pipeline%20diagram.png?raw=true)

  Each batch is then sent to the designated Amazon S3 bucket to update the preexisting table.
### Webscraping
[webscraping_code](https://github.com/speropoulos/airflow_project/blob/main/scrape_visit_info.py)

I am webscraping certain tables that i choose from the ShareCRM that my workplace uses. I am extracting the data using selenium in python to automate this scraping.

### Airflow DAG code
[airflow_dag_code](https://github.com/speropoulos/airflow_project/blob/main/scrape_visit_info_dag.py)

Then I wrote python code that transformed the data response from json to .  I deployed and scheduled that code using Apache Airflow running on an Amazon EC2 Ubuntu machine.

### Amazon S3 Bucket

After airflow runs successfully, we will have a new updated object in our S3 bucket. Now we can take this data and load it into any data warehouse you enjoy!
