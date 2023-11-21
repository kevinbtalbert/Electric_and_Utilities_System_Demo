# CDF Portion of Electric and Utilities System Demo

### [<-- Click here to go back to top-level Readme](/README.md)

Cloudera DataFlow here is an abstraction of NiFi on Kubernetes which will allow us to deploy our flow template and ingest disparate data simulating real scenarios, process it and perform real time actions based on outcomes identified. 

## Deploying the Template

Use the `ElectricUtilitiesDemo.json` NiFi flow template at the top level of the CDF-Assets folder to deploy in CDF or NiFi.

## Demonstrating the parts of the Flow

### Setup the Iceberg Tables for Data Warehouse

![](/CDF-Assets/screenshots/nifi-create-tables.png)

### Ingest Electrical, Utility, Billing, and Customer Data from Disparate Data Sources and Push to Data Warehouse

*See top level README for more details on the 5 data sources.*

![](/CDF-Assets/screenshots/nifi-ingest-push-data.png)

### Other Dataset Transformations Samples

![](/CDF-Assets/screenshots/nifi-other-outcomes.png)

### Real Time Alerting through Email and Slack

![](/CDF-Assets/screenshots/nifi-real-time-alert.png)

![](/CDF-Assets/screenshots/nifi-alert-outage-email.png)


### Required Services and Parameters Setup

#### Required Services for Flow

![](/CDF-Assets/screenshots/required-services.png)

#### Required Parameters for Flow

![](/CDF-Assets/screenshots/parameter-setup.png)