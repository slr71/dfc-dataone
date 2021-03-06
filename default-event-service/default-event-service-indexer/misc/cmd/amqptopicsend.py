#!/usr/bin/env python2.6
#
# This always exits with 0 status, as a work around for iRODS msiExecCmd microservice. To detect
# errors, monitor stderr.

import logging
import pika
import os
import sys

try:
  
	
	logging.basicConfig(stream=sys.stdout)
	
	ephemeral = sys.argv[1].lower() == 'true'
	 
	key = sys.argv[2]
	sys.stdout.write("key:" + key)
	body = sys.argv[3]
	sys.stdout.write("body:" + body)
	
	exchange = 'irods'
	
	connParams = pika.URLParameters("amqp://irods:irods@10.0.2.2") //FIXME: add as env param
	
	connection = pika.BlockingConnection(connParams)
	sys.stdout.write("hello")
	channel = connection.channel()
	
	channel.exchange_declare(exchange=exchange,
	                             exchange_type='topic',
	                             durable=(not ephemeral),
	                             auto_delete=ephemeral)
	
	channel.basic_publish(exchange=exchange,
	       routing_key=key,
	       body=body,
	       properties=pika.BasicProperties(delivery_mode=2))
	
	connection.close()

except BaseException as e:
    sys.stderr.write('ERROR: %s\n' % e)
    sys.exit(1)