import geojson

# 1.  binary data  which contains a position for each of 2 million vehicles.
# 2.  Task : find the nearest vehicle position in the data file to each of the 10 co-ordinates provided below....


class vehiclePositions(object):
        def __init__(self,position, positionId,latitude,longitude):
                self.position = position
                self.positionId = positionId
                self.latitude = latitude
                self.longitude = longitude
                
        def __geo_interface__(self):
                return{'position','latitude','longitude','string'}


