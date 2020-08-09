import rhinoscriptsyntax as rs
allCurves = rs.GetObjects()
for curve in allCurves:


    point = 0,0,0
    distance = 3
    curve1 = rs.OffsetCurve(curve, point, distance)

    id = curve1
    trans = 0,0,3
    curve2 = rs.CopyObjects(id,trans)

    point = 0,0,0
    distance = -6
    curve3 = rs.OffsetCurve(curve2, point, distance)
    area = rs.CurveArea(curve3)
    radius = (4*area[0]/3.14)**0.5
    dep = radius
    #dep = 15

    id = curve3
    trans = 0,0,-dep
    curve4 = rs.CopyObjects(id,trans)

    point = 0,0,0
    distance = -5
    #curve44 = rs.OffsetCurve(curve4, point, distance)

    center = rs.CurveAreaCentroid(curve4)
    scale = 0.5, 0.5, 1
    curve44 = rs.ScaleObject(curve4, center[0], scale)

    id = curve
    trans = 0,0,-dep
    curve5 = rs.CopyObjects(id,trans)

    point = 0,0,0
    distance = -5
    #curve55 = rs.OffsetCurve(curve5, point, distance)
    center = rs.CurveAreaCentroid(curve5)
    scale = 0.5, 0.5, 1
    curve55 = rs.ScaleObject(curve5, center[0], scale)

    ids = curve2, curve3
    srf1 = rs.AddLoftSrf(ids)

    ids = curve1, curve2
    srf2 = rs.AddLoftSrf(ids)

    ids = curve, curve1
    srf3 = rs.AddLoftSrf(ids)

    ids = curve, curve55
    srf4 = rs.AddLoftSrf(ids)

    ids = curve3, curve44
    srf5 = rs.AddLoftSrf(ids)

    ct = rs.CurveAreaCentroid(curve4)[0]
    area = rs.CurveArea(curve)
    dia = area[0]/3.14/2/2/50
    cir1 = rs.AddCircle(ct, dia)

    ct2 = rs.CurveAreaCentroid(curve55)[0]
    cir2 = rs.AddCircle(ct2, dia)


    ids = cir1, curve44
    srf6 = rs.AddPlanarSrf(ids)

    for srf in srf6:
        area = rs.SurfaceArea(srf)
        print area
        if area < dia*dia*3.15/4:
            rs.DeleteObject(srf)

    ids = cir2, curve55
    srf7 = rs.AddPlanarSrf(ids)

    for srf in srf7:
        area = rs.SurfaceArea(srf)
        if area < dia*dia*3.15/4:
            rs.DeleteObject(srf7)

    ids = cir1, cir2
    srf9 = rs.AddLoftSrf(ids)

#    srf8 = rs.AddPlanarSrf(ids)
#    for srf in srf8:
#        area = rs.SurfaceArea(srf)
#        if area < dia*dia*3.15/4:
#            rs.DeleteObject(srf)

    srflist1 = srf1, srf2
    srf = rs.JoinSurfaces(srflist1)

    srflist2 = srf, srf3
    srf = rs.JoinSurfaces(srflist2)

    srflist3 = srf, srf4
    srf = rs.JoinSurfaces(srflist3)

    srflist4 = srf, srf7
    srf = rs.JoinSurfaces(srflist4)

    srflist5 = srf, srf9
    srf = rs.JoinSurfaces(srflist5)

    srflist6 = srf, srf6
    srf = rs.JoinSurfaces(srflist6)

    srflist7 = srf, srf5
    srf = rs.JoinSurfaces(srflist7)

    srflist8 = srf, srf1
    srf = rs.JoinSurfaces(srflist8)

    rs.DeleteObject(srf1)
    rs.DeleteObject(srf2)
    rs.DeleteObject(srf3)
    rs.DeleteObject(srf4)
    rs.DeleteObject(srf5)
    rs.DeleteObject(srf6)
    rs.DeleteObject(srf7)
    rs.DeleteObject(srf9)
    rs.DeleteObject(curve)
    rs.DeleteObject(curve1)
    rs.DeleteObject(curve2)
    rs.DeleteObject(curve3)
    rs.DeleteObject(curve4)
    rs.DeleteObject(curve44)
    rs.DeleteObject(curve5)
    rs.DeleteObject(curve55)
    rs.DeleteObject(cir1)
    rs.DeleteObject(cir2)
