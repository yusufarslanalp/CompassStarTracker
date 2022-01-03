from PIL import Image
def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

print( get_date_taken( r"C:\Users\yusuf\AndroidStudioProjects\CompassStarTracker\StarTracker\RPI\Sample_images\26_07_-_20_27_08_image6_700.jpg" ) )


print( get_date_taken( r"C:\Users\yusuf\AndroidStudioProjects\CompassStarTracker\StarTracker\RPI\Sample_images\IMG_20220103_115626.jpg" ) )

