
from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'users.verifications'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer.send(topicName, b'Hello from kafka')

print("Message Sent")