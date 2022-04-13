import os

import pika


class Publisher:
    @staticmethod
    def add(cmd):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=os.getenv('RABBITMQ_HOST')))
        except pika.exceptions.AMQPConnectionError as exc:
            print(
                "Failed to connect to RabbitMQ service. Message wont be sent.")
            return

        channel = connection.channel()
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=cmd,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))

        connection.close()
        return " [x] Sent: %s" % cmd
