from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = float(celsius + 273.15)
        fahrenheit = float(celsius * 1.8 + 32)  
        ans = [kelvin, fahrenheit]
        return ans  
