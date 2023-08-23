# ETL

# Introduction to ETL 
ETL, which stands for extract, transform and load, is a data integration process that combines data from multiple data sources into a single, consistent data store that is loaded into a data warehouse or other target system.
ETL provides the foundation for data analytics and machine learning workstreams. Through a series of business rules, ETL cleanses and organizes data in a way which addresses specific business intelligence needs, like monthly reporting, but it can also tackle more advanced analytics, which can improve back-end processes or end user experiences. ETL is often used by an organization to: 

- Extract data from legacy systems
- Cleanse the data to improve data quality and establish consistency
- Load data into a target database

# Introduction to ELT
Extract, Load, Transform (ELT) is a data integration process for transferring raw data from a source server to a data system (such as a data warehouse or data lake) on a target server and then preparing the information for downstream uses.ELT is a variation of the Extract, Transform, Load (ETL), a data integration process in which transformation takes place on an intermediate server before it is loaded into the target. In contrast, ELT allows raw data to be loaded directly into the target and transformed there.

With an ELT approach, a data extraction tool is used to obtain data from a source or sources, and the extracted data is stored in a staging area or database. Any required business rules and data integrity checks can be run on the data in the staging area before it is loaded into the data warehouse. All data transformations occur in the data warehouse after the data is loaded.

# ETL VS ELT

| Category | ETL | ELT |
| -------  | ------| ------- |
| Stands for |Extract, transform, and load   | Extract, load, and transform |
|	Process | Takes raw data, transforms it into a predetermined format, then loads it into the target data warehouse|Takes raw data, loads it into the target data warehouse, then transforms it just before analytics|
|Data compatibility|Best with structured data|Can handle structured, unstructured, and semi-structured data|
|Speed|ETL is slower than ELT|ELT is faster than ETL as it can use the internal resources of the data warehouse|
|Costs|Can be time-consuming and costly to set up depending on ETL tools used|More cost-efficient depending on the ELT infrastructure used|
|Security|May require building custom applications to meet data protection requirements|You can use built-in features of the target database to manage data protection|


