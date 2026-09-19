class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the closest point in the rectangle to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Squared distance from circle center to closest point
        dx = closest_x - xCenter
        dy = closest_y - yCenter

        return dx * dx + dy * dy <= radius * radius