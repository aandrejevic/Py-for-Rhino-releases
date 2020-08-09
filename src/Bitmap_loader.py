import System
import rhinoscriptsyntax as rs

def remap(uval,u,h):
    start = u[0]
    end = u[1]

    startt= 0
    endt= h

    hval = (uval-start)/(end-start) *(endt)

    return hval

path = "/Users/aandrejevic/downloads/O5Fwd.bmp"
srf = "3e8b01e5-8da8-451e-a86f-060df82a94c9"
bitmap = System.Drawing.Bitmap.FromFile(path)
width = bitmap.Width
height = bitmap.Height

rs.EnableRedraw(False)
listUdomain = rs.SurfaceDomain(srf,0)
listVdomain = rs.SurfaceDomain(srf,1)
floatUstep = (listUdomain[1]-listUdomain[0])/40
floatVstep = (listVdomain[1]-listVdomain[0])/40

for i in rs.frange(listUdomain[0],listUdomain[1],floatUstep):
    for j in rs.frange(listVdomain[0],listVdomain[1],floatVstep):

        temppt = rs.EvaluateSurface(srf,i,j)

        targetwidth = remap(i,listUdomain,width)
        targetheight = remap(j,listVdomain,height)


col = System.Drawing.Bitmap.GetPixel(bitmap, abs(targetwidth-1), abs(targetheight-1))


pt = rs.AddSphere(temppt,.3)
rs.ObjectColor(pt,[col.R,col.B,col.G])

rs.EnableRedraw(True)
