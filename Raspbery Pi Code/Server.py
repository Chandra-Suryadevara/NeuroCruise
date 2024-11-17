import socket
import serial

# Set up the serial connection to the Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Set up a TCP server
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 65432      # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")
    
    while True:
        print("Waiting for a connection...")
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)  # Receive data from the client
                if not data:
                    print("Client disconnected.")
                    break
                command = data.decode('utf-8').strip()
                print(f"Received command: {command}")
                
                # Send command to Arduino
                arduino.write((command + '\n').encode())
                print(f"Command sent to Arduino: {command}")
