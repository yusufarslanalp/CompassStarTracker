from math import *
import numpy as np

"""
RA = yaw
Dec = pitch
Roll = roll
"""

def euler_to_rotMat(yaw, pitch, roll):
    Rz_yaw = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw),  np.cos(yaw), 0],
        [          0,            0, 1]])
    Ry_pitch = np.array([
        [ np.cos(pitch), 0, np.sin(pitch)],
        [             0, 1,             0],
        [-np.sin(pitch), 0, np.cos(pitch)]])
    Rx_roll = np.array([
        [1,            0,             0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll),  np.cos(roll)]])
    # R = RzRyRx
    rotMat = np.dot(Rz_yaw, np.dot(Ry_pitch, Rx_roll))
    return rotMat

#paremeters are degree
def find_A_BI( ra, dec, roll ):

    #convert parameters to radian
    yaw = radians( ra )
    pitch = radians( dec )
    roll = radians( roll )


    return euler_to_rotMat( yaw, pitch, roll )

#print( find_A_BI( 212, -52, -72 ) )



"""    A_BI = [
            [ cos(theta)*cos(psi),   -cos(phi)-sin(psi) + sin(), 0 ],
            [ cos(theta)*cos(psi),   0, 0 ],
            [ -sin(theta),           0, 0 ]
    ]
"""
