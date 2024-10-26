# Summary
This is a demo on how to stream real-time data from **Apache Kafka** to **Apache Pinot** on your local machine using **Docker**.

# Description
The following [docker-compose.yml](/docker-compose.yml) file creates containers for **Apache Pinot**, **Apache Kafka**, and a message producer using a local image.  
Additionally, two Kafka listeners (**INTERNAL** and **EXTERNAL**) will be configured.  
**Apache Pinot** will ingest real-time data from **Apache Kafka** on the **INTERNAL** address "kafka:9092".  
The host will be able to produce and consume **Apache Kafka** messages on the **EXTERNAL** address "localhost:9093".  
All communication is done over **non-secure** HTTP PLAINTEXT.

![Diagram](/images/diagram.png)

# Quickstart ([Docker required](https://docs.docker.com/engine/install/))
1. `$ git clone https://github.com/thread53/kafka-demo.git`
2. `$ cd kafka-demo`
3. `$ docker compose build --no-cache && docker compose up -d`
4. Wait a bit for the **Apache Pinot** container to finish initializing, then create the schema and table:  
`$ curl -i -X POST -H 'Content-Type: application/json' -d @pinot/schema.json localhost:9000/schemas`  
`$ curl -i -X POST -H 'Content-Type: application/json' -d @pinot/table.json localhost:9000/tables`
5. Point your browser to http://localhost:9000/#/query and query `demotopic` table

# Run Local Producer and Consumer Without Ingesting to Apache Pinot
1. `$ git clone https://github.com/thread53/kafka-demo.git`
2. `$ cd kafka-demo`
3. `$ python -m venv .venv`
4. `$ source .venv/bin/activate`
5. `$ pip install -r requirements.txt`
6. `$ python src/producer.py` (ensure to set `bootstrap_servers` to `'localhost:9093'`)
7. In another terminal run `$ python src/consumer.py` to start consuming the messages.

# Sources
- [Run Apache Pinot in Docker](https://docs.pinot.apache.org/basics/getting-started/running-pinot-in-docker)
- [Apache Kafka Listeners](https://kafka.apache.org/documentation/#listener_configuration)
- [Ingest from Apache Kafka](https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka#table-config)
- [kafka-python-ng](https://kafka-python.readthedocs.io/en/master/apidoc/modules.html)