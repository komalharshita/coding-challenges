class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x, closest_y = self.findClosestPointOnRectangle(xCenter, yCenter, x1, y1, x2, y2)
        dist_sq = self.squaredDistance(xCenter, yCenter, closest_x, closest_y)
        return self.isWithinRadius(dist_sq, radius)

    def findClosestPointOnRectangle(self, xCenter, yCenter, x1, y1, x2, y2):
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        return closest_x, closest_y

    def squaredDistance(self, x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    def isWithinRadius(self, dist_sq, radius):
        return dist_sq <= radius ** 2