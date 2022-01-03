import os
from pathlib import Path
import subprocess




dirAPI = Path( os.getcwd() ).parent
dirStarTracker = Path.joinpath( dirAPI, "StarTracker" )
dirRPI = Path.joinpath( dirStarTracker, "RPI" )
print( dirRPI )


os.chdir( str( dirRPI ) )
os.system( "ls" )


os.system( "python2 StarTracker_10_deg.py image-2.jpg" )
print( "hereeeeeeeeeeeeeeeeeeeee" )


f = open("ProcessCommunication.txt", "r")
print( f.read().split( " " ) )
f.close()

