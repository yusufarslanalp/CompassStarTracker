from math import *
import numpy as np
import Jdate as jd
import datetime

#finds t from jullian date.
def find_t( JD ):
    return (JD- 2451545) / 36525



arr = [ cos( radians( 60 ) ), cos( radians( 30 ) ) ]

def R3( deg ):
    return [ 
        [ cos( deg ), -sin( deg ), 0 ],
        [ sin( deg ), cos( deg ),  0 ],
        [ 0,              0,       1 ]
     ]

def R2( deg ):
    return [
        [ cos(deg),  0, sin(deg) ],
        [ 0,         1,     0    ],
        [ -sin(deg), 0, cos(deg)  ]
    ]

def R1( deg ):
    return [
        [ 1,       0,        0     ],
        [ 0,   cos(deg), -sin(deg) ],
        [ 0,   sin(deg),  cos(deg) ]
    ]

#parameter is image_date
def calc_A_GI( idate ):
    float_day = idate.day + ( idate.hour / 24 )
    jdate = jd.date_to_jd( idate.year, idate.month, float_day )
    t = find_t( jdate )

    epsilon = ( 84381.4428 - ( 46.8388 * t ) - ( 0.0002 * t * t ) + (0.002 * t * t* t) )/3600
    psi = ( -( 0.0431 ) + (5038.4739 * t) + (1.5584 * t * t) - (0.0002 * t * t * t) ) / 3600
    phi = ( (84381.4479) - (46.814 * t) + (0.0511 * t * t) + (0.0005 * t * t * t) ) / 3600 
    gamma = ( (10.5525 * t) + (0.4932 * t * t) - (0.0003 * t * t * t) ) / 3600    

    A_GI = np.matmul( R3(psi) , R1(-epsilon) )
    A_GI = np.matmul( A_GI , R3(-psi) )
    A_GI = np.matmul( A_GI, R1(phi) )
    A_GI = np.matmul( A_GI, R3(gamma) )

    return A_GI



#A_GI = calc_A_GI( datetime.datetime.now() )
#print( A_GI )







