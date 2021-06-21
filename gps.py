import numpy as np
from sgp4.api import jday
from sgp4.api import Satrec
import time

def gps_read(init_time,read_interval,init_tle):
        """
        The purpose of this function is to simulate the orbital data i.e position and velocity and act as a gps reading 
        This function takes in a time value and TLE value and an interval between succesive gps readings and gives out the next gps output 
        *** In the first gps_read the initial time in seconds needs to be taken from 1st Jan 1970 in seconds use time.gmtime method for this***
        :param read_interval: is the time spent between succesive gps readings
        :type read_interval: float
        :param init_time: initial time in seconds from 1970 using time.gmtime method
        :type init_time: float
        :param init_tle: gives the of the previous gps output
        :type init_tle:list of strings
        returns error detection flag,position and velocity in TEME frame 
        
        """
        #A tuple giving the time in date hour min sec format which is required for the jday function
        time_next = time.localtime(init_time + read_interval)
        #jday gives the julian date from the above tuples time format
        jd,fr = jday(*(time_next[0:6]))
        #the satellites TLEs are given next.
        s,t = init_tle
        #TLEs are converted to cartesian vectors
        satellite = Satrec.twoline2rv(s,t)
        #these are propagated till the required time.
        e,r,v = satellite.sgp4(jd,fr)

        return(e,r,v)

t0 = time.mktime((2021,6,20,19,55,0,0,0,0))
T = 3650
tle = ['1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991','2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482']
# print(gps_read(t0,T,tle))