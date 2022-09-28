# 1.  binary data  which contains a position for each of 2 million vehicles.
# 2.  Task : find the nearest vehicle position in the data file to each of the 10 co-ordinates provided below....


"""
The structure of the binary data file is as follows:

                DATA STRUCTURE:

Field

Data Type

PositionId

Int32

VehicleRegistration

Null Terminated ASCII String

Latitude

Float (4 byte floating-point number)

Longitude

Float (4 byte floating-point number)

RecordedTimeUTC

UInt64 (number of seconds since Epoch)

"""

"""           

        CO-ORDINATES STRUCTURE:

Position 2

Latitude = 32.345544

Longitude = -99.123124
            

Position 3

Latitude = 33.234235

Longitude = -100.214124
             

Position 4

Latitude = 35.195739

Longitude = -95.348899
         

Position 5

Latitude = 31.895839

Longitude = -97.789573
            

Position 6

Latitude = 32.895839

Longitude = -101.789573

            
Position 7

Latitude = 34.115839

Longitude = -100.225732
            

Position 8

Latitude = 32.335839

Longitude = -99.992232
             

Position 9

Latitude = 33.535339

Longitude = -94.792232
             

Position 10

Latitude = 32.234235

Longitude = -100.222222

"""


