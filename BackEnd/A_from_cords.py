from math import *

def fromCords( phi, lamda, epsilon ):
    phiCos = cos( radians( phi ) )
    phiSin = sin( radians( phi ) )

    lamdaCos = cos( radians( lamda ) )
    lamdaSin = sin( radians( lamda ) )

    epsCos = cos( radians( epsilon ) )
    epsSin = sin( radians( epsilon ) )

    A = [
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ]
    ]

    A[0][0] = ( phiCos * lamdaCos * epsCos ) - ( epsSin *   lamdaSin )
    A[0][1] = ( epsCos * phiCos * lamdaSin ) + ( epsSin * lamdaCos )
    A[0][2] = epsCos * phiSin

    A[1][0] = -( epsSin * phiCos * lamdaCos ) - ( epsCos * lamdaSin )
    A[1][1] = -( epsSin * phiCos * lamdaSin ) + ( epsCos * lamdaCos )
    A[1][2] = -( epsSin * phiSin )

    A[2][0] = -( phiSin * lamdaCos )
    A[2][1] = -( phiSin * lamdaSin )
    A[2][2] = phiCos

    print( A[0] )
    print( "" )

    print( A[1] )
    print( "" )

    print( A[2] )
    print( "" )        


fromCords( 30.59916347, -96.39482772, 42.55152162 )   



