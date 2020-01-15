def geometricToStandard(lat, long):
    latDecimal = str(lat)[len(str(lat)) - 4:]
    longDecimal = str(long)[len(str(long)) - 4:]

    latSecs = latDecimal[2:]
    latMins = latDecimal[:2]
    latDeg = str(lat)[:len(str(lat)) - 5]
    longSecs = longDecimal[2:]
    longMins = longDecimal[:2]
    longDeg = str(long)[:len(str(long)) - 5]
    latRealSecs = int(latSecs) / 60
    latRealMins = (int(latMins) + latRealSecs) / 60
    latRealDeg = int(latDeg) + latRealMins
    longRealSecs = int(longSecs) / 60
    longRealMins = (int(longMins) + longRealSecs) / 60
    longRealDeg = int(longDeg) + longRealMins

    latKM = latRealDeg * (10000 / 90)
    longKM = longRealDeg * (10000 / 90)

    latFeet = latKM * 3280.4
    longFeet = longKM * 3280.4

    return [latFeet, longFeet]
