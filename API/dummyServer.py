from multiprocessing.connection import Listener

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey= 'secret password' )
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
#msg = conn.recv()

#print( msg )

conn.send( "image-1.jpg" )


ra = conn.recv()
dec = conn.recv()
roll = conn.recv()

print( ra )

listener.close()
