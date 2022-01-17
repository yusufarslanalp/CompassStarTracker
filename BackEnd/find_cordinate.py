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
        return datetime.datetime.strptime( str_time, '%Y:%m:%d %H:%M:%S' )
    except:
        return datetime.datetime.now()

#returns ra, dec, roll, isSuccessfull
def find_attitude( image_name ):
    
    currentDir = Path( os.getcwd() )
    dirStarTracker = Path.joinpath( currentDir, "StarTracker" )
    dirRPI = Path.joinpath( dirStarTracker, "RPI" )


    os.chdir( str( dirRPI ) )
    os.system( "ls" )


    status = os.system( "python2 StarTracker_10_deg.py " + image_name )
    print( "status::::::::::::::::::::::::::::::::::::.::::::" + str( status ) )
    if( status != 0 ):
        os.chdir( str( currentDir ) )
        return 0, 0, 0, False

    f = open("ProcessCommunication.txt", "r")
    arr = f.read().split( " " )

    ra, dec, roll = float( arr[0] ), float( arr[1] ), float( arr[2] )
    print( "\n\n\n" )
    print( "----------------------Attitude Information ----------------------" )
    print( "RA: " + str(ra) )
    print( "DEC: " + str(dec) )
    print( "ROLL: "+ str(roll) )
    f.close()
    
    os.chdir( str( currentDir ) )
    return ra, dec, roll, True

#returns lat long
def find_cordinate( image_name ):
    date_taken = get_date_taken( "ReceivedImages/" + image_name )
    

    A_IG = A_GI.calc_A_IG( date_taken )
    


    ra, dec, roll, is_successfull = find_attitude( image_name )
    if( is_successfull == False ):
        print( "Image is not successfulllllllllllllllllllllllll" )
        return { "lat": 0.0, "longi": 0.0, "isSuccessfull": "false" }
    A_BI = A_BI_file.find_A_BI( ra, dec, roll )


    A = np.matmul( A_BI , A_IG )
    
    print( "-----------The time the image was taken-------------" )
    print( str( date_taken ) )
    
    print( "---------------------Calculated Rotations------------------------" )
    print( "A_BI: \n" + str( A_BI ) + "\n"  )
    print( "A_IG: \n" + str( A_IG ) + "\n"  )
    print( "A_BG: \n" + str( A ) + "\n"  )

    lat = math.acos( A[2][2] )
    lat = math.degrees( lat )
    longi = math.atan( A[2][1] / A[2][0] )
    longi = math.degrees( longi )


    #lat = lat - 10
    #longi = longi - 30

    print( "---------------------the determined cordinate------------------------" )
    print( "lat: " + str( lat ) )
    print( "longi: " + str( longi ) )


    return { "lat": lat, "longi": longi, "isSuccessfull": "true" }


#find_cordinate( r"26_07_-_21_01_51_image8_900.jpg" )

#d = datetime.datetime.strptime( '2016:07:26 20:42:38', '%Y:%m:%d %H:%M:%S' )
#print( d )


