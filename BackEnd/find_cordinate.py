import A_GI
from PIL import Image

def get_date_taken( path ):
    return Image.open( path )._getexif()[36867]



#returns lat long
def find_cordinate( image_name ):
    date_taken = get_date_taken( image_name )

    #print( date_taken )


#find_cordinate( r"C:\Users\yusuf\AndroidStudioProjects\CompassStarTracker\BackEnd\StarTracker\RPI\Sample_images\26_07_-_20_27_08_image6_700.jpg" )