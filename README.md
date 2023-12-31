# Electric and Utilities System Demo
Using CDF, CDW, CML and Data Viz, this demo is a complete Electric and Utilities Company use case to broadly leverage the CDP Data Services platform

This demo is in three parts. Refer to the component parts by their individual markdowns below:

### [CDF Readme](/CDF-Assets/README.md)

### [CDW / Data Viz Readme](/CDW-Assets/README.md)

### [CML Readme](/CML-Assets/README.md)

## Situation and Outcomes for this Use Case

![](/CML-Assets/app_assets/situation-to-outcomes.png)

## Architectural Landscape

![](/CML-Assets/app_assets/architecture.png)

## The Data Sources

### Data Flow Data Sets Used

1. **ORS - Outage Reporting System**

Simulated by [openei_utility_info_export_as_of_2015_08_28_1.csv](/datasets/openei_utility_info_export_as_of_2015_08_28_1.csv) dataset. This dataset comes from the US Dept of Energy as part of an initiative to create a public outage information dataset. See more: https://data.world/us-doe-gov/a6ac378e-0270-4d3e-9813-34dcd0ad7322

2. **Power Lines Data**

Simulated by [U.S._Electric_Power_Transmission_Lines.csv](/datasets/U.S._Electric_Power_Transmission_Lines.csv) dataset. This dataset originated from ArcGIS Hub's mapping of U.S. Electric Power Transmission Lines. See more: https://hub.arcgis.com/datasets/d4090758322c4d32a4cd002ffaa0aa12/explore

3. **ESRI - GIS data for power distribution assets**

Simulated by [sample_gis_power_distribution.csv](/datasets/sample_gis_power_distribution.csv) dataset. This dataset was generated by OpenAI to be representative of data which may be stored by ArcGIS or some other GIS platform.

4. **Customer Consumption Data**

Simulated by [household_power_consumption.csv](/datasets/household_power_consumption.csv) dataset.  This dataset comes from data.world as part of the UCI Machine Learning Repository and represents a slice of the total dataset. See more: https://data.world/databeats/household-power-consumption

5. **Customer Billing Data**

Simulated by [sample_billing_invoices.csv](/datasets/sample_billing_invoices.csv) dataset. This dataset was generated by OpenAI to be representative of data which may have originated from a database or other data analysis solution.


### Machine Learning Data Sets Used

6. **Outage data for a day in November 2023 from CLECO**

Website data from CLECO converted to CSV in [utility_outage_data.csv](/CML-Assets/data/utility_outage_data.csv) dataset.  See CLECOs outage map for a current representation of outages.

7. **Customer Utility Data**

Simulated by [generated_utility_data_12_months.csv](/CML-Assets/data/generated_utility_data_12_months.csv) dataset. This dataset was generated by OpenAI to be representative of data which may have been generated by a meter for a customer's consumption.
