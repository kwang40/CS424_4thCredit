import socket
import time
import picamera

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
my_server = '10.194.170.243'
client_socket = socket.socket()
client_socket.connect((my_server, 8000))

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 20
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)
        # Start recording, sending the output to the connection for 60
        # seconds, then stop
        camera.start_recording(connection, format='h264')
        camera.wait_recording(240)
        camera.stop_recording()
finally:
    connection.close()
    client_socket.close()