This project is a server. To start the server run [server.py](server.py) file with python3. Life cycle of a one request is following:
- The server accept night-sky-image image as POST request.
- Server saves received image to [ReceivedImages](ReceivedImages) folder.
- The server run the [StarTracker](StarTracker) project for finding attitude values.
- The [StarTracker](StarTracker) project writes attitude values to [ProcessCommunication.txt](StarTracker/RPI/ProcessCommunication.txt)
- The server find cordinate using attitude values and time. Cordinate is in terms of latitude and longitude.
- The server returns cordinate as http response.

This project run on Linux. Python2 and Python3 should be inslalled on the machine for running project