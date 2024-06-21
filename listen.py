import socket
import time
import subprocess



def listen_and_sleep(port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the port
    server_address = ('', port)
    sock.bind(server_address)
    
    print(f"Listening on port {port}...")
    
    try:
        while True:
            data, address = sock.recvfrom(4096)
            
            message = data.decode('utf-8').strip()
            
            print(f"Received '{message}' from {address}")
            
            if message == "sleep":
                print("Putting system to sleep...")
                time.sleep(3)
                subprocess.run(["systemctl", "suspend"])
                
            elif message == "shutdown":
                print("Shutting down...")
                time.sleep(3)
                subprocess.run(["systemctl", "poweroff"])

            elif message == "wake":
                print("Waking up...")
                
            else:
                print("Message does not trigger sleep.")
    
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting...")
    
    finally:
        sock.close()

if __name__ == "__main__":
    listen_and_sleep(12345)