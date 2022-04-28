from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['0.0.0.0:9092'])

#if __name__ == "__main__":
for i in range(1,10):
        producer.send('user.registrations',value={"hello Kafka, How are you!!":i})
        print(i)
        sleep(0.3)