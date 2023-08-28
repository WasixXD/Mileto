


def coAngular(pointsA, pointsB):
    return (pointsB[1] - pointsA[1]) / (pointsB[0] - pointsA[0])


def coLinear(coAngular, points):
    return points[1] - coAngular * points[0]
