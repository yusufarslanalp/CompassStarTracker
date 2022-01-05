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
        str_time=  Image.open( path )._getexif()[36867]
        print ( "belowwwwwwwwwwwwwwwwwwwwwwwwwww" )
        print( path )
        print( str_time )
        return datetime.datetime.strptime( str_time, '%Y:%m:%d %H:%M:%S' )
    except:
        return datetime.datetime.now()

def find_attitude( image_name ):
    
    currentDir = Path( os.getcwd() )
    dirStarTracker = Path.joinpath( currentDir, "StarTracker" )
    dirRPI = Path.joinpath( dirStarTracker, "RPI" )
    print( dirRPI )


    os.chdir( str( dirRPI ) )
    os.system( "ls" )


    os.system( "python2 StarTracker_10_deg.py " + image_name )
    print( "hereeeeeeeeeeeeeeeeeeeee" )


    f = open("ProcessCommunication.txt", "r")
    arr = f.read().split( " " )
    ra, dec, roll = float( arr[0] ), float( arr[1] ), float( arr[2] )

    #print( f.read().split( " " ) )
    f.close()
    
    os.chdir( str( currentDir ) )
    return ra, dec, roll

#returns lat long
def find_cordinate( image_name ):
    date_taken = get_date_taken( "ReceivedImages/" + image_name )
    print( "date::::::::::::::::::::::::::::::" + str( date_taken ) )

    A_IG = A_GI.calc_A_IG( date_taken )

    ra, dec, roll = find_attitude( image_name )
    A_BI = A_BI_file.find_A_BI( ra, dec, roll )


    A = np.matmul( A_BI , A_IG )

    lat = math.acos( A[2][2] )
    lat = math.degrees( lat )
    longi = math.atan( A[2][1] / A[2][0] )
    longi = math.degrees( longi )


    #lat = lat - 10
    #longi = longi - 30

    print( "lat: " + str( lat ) )
    print( "longi: " + str( longi ) )


    return { "lat": lat, "longi": longi }


#find_cordinate( r"26_07_-_21_01_51_image8_900.jpg" )

#d = datetime.datetime.strptime( '2016:07:26 20:42:38', '%Y:%m:%d %H:%M:%S' )
#print( d )


