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

# When to use ETL vs. ELT
Extract, load, and transform (ELT) is the standard choice for modern analytics. However, you might consider extract, transform, and load (ETL) in the following scenarios.

## Legacy databases
It is sometimes more beneficial to use ETL to integrate with legacy databases or third-party data sources with predetermined data formats. You only have to transform and load it once into your system. Once transformed, you can use it more efficiently for all future analytics.

## Experimentation
In large organizations, data engineers conduct experiments—things like discovering hidden data sources for analytics and trying out new ideas to answer business queries. ETL is useful in data experiments to understand the database and its usefulness in a particular scenario.

## Complex analytics
ETL and ELT may both be used together for complex analytics that use multiple data formats from varied sources. Data scientists may set up ETL pipelines from some of the sources and use ELT with the rest. This improves analytics efficiency and increases application performance in some cases.

## IoT applications
Internet of Things (IoT) applications that use sensor data streams often benefit from ETL over ELT. For examples, here are some common use cases for ETL at the edge:
* to receive data from different protocols and convert it into standard data formats for use in cloud workloads
* to filter high-frequency data, perform averaging functions on large datasets, then load averaged or filtered values at a reduced rate
* to calculate values from disparate data sources on the local device, and send filtered values to the cloud backend
* to cleanse, deduplicate, or fill missing time series data elements


# Comparison between Lambda and Glue, and when to use them?

Lambda and Glue are both services offered by Amazon Web Services (AWS) that are used for data processing and transformation tasks, but they have different focuses and use cases. Let's compare Lambda and Glue and explore when to use each of them:

## AWS Lambda:

    Functionality: AWS Lambda is a serverless compute service that allows you to run code in response to events without provisioning or managing servers. It's designed for executing small, event-driven functions in a variety of programming languages.

    Use Cases:
        Microservices: Lambda is great for building microservices architecture where each function performs a specific task.
        Event-Driven Processing: It's ideal for processing events such as data uploads, incoming messages, or triggers from other AWS services.
        Real-Time Processing: Lambda can handle real-time processing of data as it comes in.
         Custom Data Transformations: If  needed to perform specific data transformations that don't fit into the capabilities of AWS Glue, Lambda can be a more customizable solution.
        Scalability: Lambda functions automatically scale based on the incoming workload, allowing you to handle varying processing demands seamlessly.
        Languages: Lambda supports multiple programming languages, allowing developers to choose the language they are comfortable with.

# AWS Glue:

    Functionality: AWS Glue is a managed Extract, Transform, Load (ETL) service designed to make it easy to prepare and load data for analytics. It provides data cataloging, data transformation, and data loading capabilities.

    Use Cases:
        ETL Pipelines: Glue is well-suited for building ETL pipelines to extract data from various sources, transform it into the desired format, and load it into data warehouses or data lakes.
        Data Cataloging: Glue's data cataloging capabilities help in discovering and understanding data from various sources in a centralized manner.
        Automated Schema Evolution: Glue can help manage changes in data schema over time, ensuring compatibility between different versions of data.
        Data Cleansing and Enrichment: It's suitable for performing data cleansing, validation, and enrichment as part of the ETL process.
        Managed Service: Glue is a fully managed service that abstracts much of the underlying infrastructure management, making it easier to set up and use for ETL tasks.
        Scalability: Glue can automatically scale resources to handle larger data volumes and processing demands.
        Data Catalog: Glue includes a data catalog that helps organize metadata, making it easier to understand and access different datasets.

# When to Use Each:

Use AWS Lambda When: You need to execute small, event-driven functions in response to specific events. It's suitable for real-time processing, custom transformations, and building microservices.

Use AWS Glue When: You need to build comprehensive ETL pipelines for data transformation, data cataloging, and loading data into data warehouses or data lakes. It's ideal for managing larger-scale data integration and preparation tasks.

In many scenarios, Lambda and Glue can complement each other. For example, you might use Lambda to perform custom real-time data transformations and use Glue for the more complex and organized ETL processes involving data cataloging, transformation, and loading.

