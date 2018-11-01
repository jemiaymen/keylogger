import rpyc
from rpyc.utils.server import ThreadedServer
import sys
import os
from plumbum import cli

class JemiService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def msg(self,conn):
    	print('hadha message')


server = ThreadedServer(JemiService, port=18861, protocol_config={'allow_public_attrs': True,})
server.start()