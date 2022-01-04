import A_GI
from PIL import Image
import datetime
import os
from pathlib import Path
import A_BI as A_BI_file
import numpy as np
import math as math

def get_date_taken( path ):
    try:
        return Image.open( path )._getexif()[36867]
    except:
        return datetime.datetime.now()

def find_attitude():
    
    currentDir = Path( os.getcwd() )
    dirStarTracker = Path.joinpath( currentDir, "StarTracker" )
    dirRPI = Path.joinpath( dirStarTracker, "RPI" )
    print( dirRPI )


    os.chdir( str( dirRPI ) )
    os.system( "ls" )


    os.system( "python2 StarTracker_10_deg.py image-2.jpg" )
    print( "hereeeeeeeeeeeeeeeeeeeee" )


    f = open("ProcessCommunication.txt", "r")
    arr = f.read().split( " " )
    ra, dec, roll = float( arr[0] ), float( arr[1] ), float( arr[2] )

    #print( f.read().split( " " ) )
    f.close()    
    return ra, dec, roll

#returns lat long
def find_cordinate( image_name ):
    date_taken = get_date_taken( "ReceivedImages/" + image_name )
    print( date_taken )

    A_IG = A_GI.calc_A_IG( date_taken )
    print( A_IG )
    ra, dec, roll = find_attitude()
    A_BI = A_BI_file.find_A_BI( ra, dec, roll )

    A = np.matmul( A_BI , A_IG )

    lat = math.acos( A[2][2] )
    long = math.atan( A[2][1] / A[2][0] )

    print( "---------------------------------------------" )
    print( long )


    return { "lat": 40.809, "longi": 29.362 }


find_cordinate( r"C:\Users\yusuf\AndroidStudioProjects\CompassStarTracker\BackEnd\StarTracker\RPI\Sample_images\26_07_-_20_27_08_image6_700.jpg" )