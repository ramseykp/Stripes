import arcpy

aprx = arcpy.mp.ArcGISProject('current')

m = aprx.listMaps()[0]
lyr = m.listLayers("97_pnts")[0]
lyt = aprx.listLayouts()[0]
pointNumber = 0

#headingChange = 0.0571428571
newHeading = 39.55
mf = 0
x = 0.25
y = 23.5
while mf < 94:
    frame = lyt.listElements('MAPFRAME_ELEMENT', 'Map Frame {}'.format(str(mf)))[0]
    frame.elementPositionX = x
    frame.elementPositionY = y
    y = y - 0.25
    arcpy.SelectLayerByAttribute_management('97_pnts', 'NEW_SELECTION', 'id = {}'.format(str(pointNumber)))
    elm = lyt.listElements('MAPFRAME_ELEMENT', 'Map Frame {}'.format(str(mf)))[0]
    elm.camera.setExtent(elm.getLayerExtent(lyr, True, True))
    elm.camera.heading = 39.55
    elm.camera.scale = 25000
    pointNumber = pointNumber + 1
    mf = mf + 1

print("done")
