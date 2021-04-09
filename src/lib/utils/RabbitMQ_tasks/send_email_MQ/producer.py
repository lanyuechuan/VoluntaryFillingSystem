import pika

from django.conf import settings


class RabbitMQ():
    def __init__(self, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        user_id = kwargs.get('user_id')
        # 1、连接rabbitmq服务器
        connection = pika.BlockingConnection(pika.ConnectionParameters(settings.SERVER_IP))
        channel = connection.channel()

        # 2、创建一个名为hello的队列
        channel.queue_declare(queue='hello')
        # 3、简单模式,向名为hello队列中插入用户邮箱地址email
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=str([email, username, user_id]),
                              )

        # print("发送用户邮箱：‘{}’ 到MQ成功".format(email))
        connection.close()
