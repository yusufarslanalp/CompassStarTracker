import A_GI
from PIL import Image
import datetime

def get_date_taken( path ):
    try:
        return Image.open( path )._getexif()[36867]
    except:
        return datetime.datetime.now()



#returns lat long
def find_cordinate( image_name ):
    date_taken = get_date_taken( "ReceivedImages/" + image_name )
    print( date_taken )
    return { "lat": 40.809, "longi": 29.362 }


#find_cordinate( r"C:\Users\yusuf\AndroidStudioProjects\CompassStarTracker\BackEnd\StarTracker\RPI\Sample_images\26_07_-_20_27_08_image6_700.jpg" )