import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as rc
import System.Drawing
import datetime
from Rhino.Geometry import Point3d


crcl = rs.AddCircle(Point3d.Origin, 5.0)
# path = rs.AddLine([5,0,0], [10,0,10])
# rs.ExtrudeCurve(crcl, path)
# extr = rs.ExtrudeCurveStraight(crcl, [0,0,0], [0,0,20])
#

for i in range (crcl):


# vts = []
# for i in range(10):
#     pt = rc.Geometry.Point3d(i,i,i)
#     vts.append(pt)


#def GetPointDynamicDrawFunc( sender, args ):
  #pt1 = Rhino.Geometry.Point3d(0,0,0)
  #pt2 = Rhino.Geometry.Point3d(10,10,0)
  #args.Display.DrawLine(pt1, args.CurrentPoint, System.Drawing.Color.Red, 2)
  #args.Display.DrawLine(pt2, args.CurrentPoint, System.Drawing.Color.Blue, 2)

#gp = Rhino.Input.Custom.GetPoint()
#gp.DynamicDraw += GetPointDynamicDrawFunc
#gp.Get()

#def renameobject():
    #object_id = rs.GetObject("Select an object to rename", select=True)
    #if object_id:
        #newname = "Date tag: " + str(datetime.datetime.now())
        #rs.ObjectName(object_id, newname)


#if __name__=="__main__":
    #renameobject()
