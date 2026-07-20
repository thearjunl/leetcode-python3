class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the angle of the hour hand (30° per hour + 0.5° per minute)
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # Calculate the angle of the minute hand (6° per minute)
        minute_angle = minutes * 6
        
        # Find the absolute difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller angle (if angle > 180°, return 360 - angle)
        return min(angle, 360 - angle)