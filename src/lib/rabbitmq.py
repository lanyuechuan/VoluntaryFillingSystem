"""rabbitmq
"""
import pika
import json
from django.conf import settings

class RabbitMq():
    """rabbitmq队列类
    """
    def __init__(self, queue_name):
        try:
            auth = pika.PlainCredentials(settings.RABBITMQ['user'], settings.RABBITMQ['password'])
            connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ['host'], settings.RABBITMQ['port'], settings.RABBITMQ['virtual_hosts'], auth))
            self.queue_name = queue_name
            self.channel = connection.channel()
            self.channel.queue_declare(queue=queue_name)
        except Exception as err:
            raise RuntimeError('连接rabbitmq错误:'+str(err))

    def to_queue(self, data, exchange=''):
        """入队
        """
        try:
            json.loads(data)
        except Exception:
            data = json.dumps(data)
        self.channel.basic_publish(exchange=exchange, routing_key=self.queue_name, body=data)

    def out_queue(self, callback):
        """出队
        """
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback)
        self.channel.start_consuming()
