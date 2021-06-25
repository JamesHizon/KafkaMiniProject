# Kafka Mini-Project

For this mini-project, check the Kafka folder.

### Dependencies
Inside the requirements.txt file, one should see a requirements.txt file with kafka package along with version number.

### Objective
The main objective is to build a real-time fraud detection system from scratch using Apache Kafka and Python. I first had to generate a stream of transactions. Then, I needed to write a Python script which would process those stream messages to detect which ones are fraud.

### Steps
In order to get the streaming application running, I first needed to create the essential files (app.py, Dockerfile, requirements.txt., transactions.py, docker-compose.kafka.yml and docker-compose.yml files). The steps would then proceed as follows for a successfully running Kafka streaming application:

1. Run command to spin up broker and zookeeper:
```docker-compose -f docker-compose.kafka.yml up -d```

2. Run command to spin up generator and start producing infinite stream of messages:
```docker-compose --f docker-compose.yml up```

3. Check to make sure everything is up and running as it should:
```docker-compose -f docker-compose.kafka.yml ps```
```docker-compose -f docker-compose.kafka.yml ps```

4. Run command to log into broker:
```docker exec -it kafka-frauddetector_broker_1 sh```

5. Verify that I am able to produce messages:
```kafka-console-consumer --bootstrap-server localhost:9092 --topic queueing.transactions --from-beginning```

6. Verify that I am able to consume messages as legit:
```kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit```

7. Verify that I am able to consume messages as fraud:
```kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud```


### Screenshot Info
Attached are screenshots of when I was able to obtain the essential desired queueing.transactions (from generator), legit and fraud messages. I am not always able to have it successfully run, however. For one of the screenshots, I took it before "gracefully exiting" using ```Ctrl+C```.

