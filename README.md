# Summary
This is a demonstration on how to stream real-time data from Kafka to Pinot on your local machine using Docker

# Description
The following config file will create Apache Pinot and Apache Kafka containers in Docker and configure two Kafka Listeners (INTERNAL and EXTERNAL)  
Pinot will be able to ingest real-time data from Kafka on the INTERNAL address "kafka:9092"  
Host will be able to produce and consume Kafka messages on the EXTERNAL address "localhost:9093"  
All communication is done in non-secure HTTP PLAINTEXT  

![Kafka](https://github.com/thread53/kafka-demo/blob/main/diagram.png)

# Configuration
1. Install Docker Desktop  
https://docs.docker.com/desktop/

2. From any shell run the following command  
```bash
$ docker-compose -f kafka-compose.yml up -d
```

3. Check containers are running  
```bash
$ docker ps
```

Now you have Pinot and Kafka running locally in Docker. Next steps:  
1. Produce messages to Kafka topic  
1.1. You can do that by writing your own script or shell to Kafka  

2. Create schema and realtime table config in Pinot  
https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka#schema  

3. Go to Pinot Query Console and query your new realtime table  
http://localhost:9000/#/query  

# Source
https://docs.pinot.apache.org/basics/getting-started/running-pinot-in-docker  
https://kafka.apache.org/documentation/#listener_configuration  
https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka#table-config  