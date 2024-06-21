import socket
from wakeonlan import send_magic_packet

def wol():

    mac_address = '74:56:3C:78:56:07' # MAC ADDRESS OF THE COMPUTER YOU WANT TO WAKE UP
    send_magic_packet(mac_address)

    print("WAKING UP...")

def shutdown(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "shutdown"
    server_address = (ip, port)
    try:
        print("SHUTTING DOWN...")
        sock.sendto(message.encode('utf-8'), server_address)

    finally:
        sock.close()

def sleep(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "sleep"
    server_address = (ip, port)
    try:
        print("SUSPENDING...")
        sock.sendto(message.encode('utf-8'), server_address)

    finally:
        sock.close()

def main():
    while True:

        ip = "192.168.0.184"  # CHANGE THIS TO YOUR SERVER IP ADDRESS

        choice = input("Enter 1 for WAKE, 2 for SLEEP and 0 for SHUTDOWN, q to Quit: ")

        if choice == '1':
            wol()
        elif choice == '2':
            sleep(ip, 12345)
        elif choice == '0':
            shutdown(ip, 12345)
        elif choice.lower() == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
