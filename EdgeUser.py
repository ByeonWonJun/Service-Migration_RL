import numpy as np

class User:
    def __init__(self, cpu_speed, max_delay, user_speed, cpu_cycle_num ,dataRate, fixedData):
        
        self.cpu_speed = cpu_speed
        self.max_delay = max_delay
        self.user_speed = user_speed
        self.position = position
        self.dataRate = dataRate
        self.cpu_cycle_num = cpu_cycle_num
        self.fixedData = fixedData
        
        
    def getLocalTime(self):
        return self.cpu_cycle_num*(1-dataRate)/self.cpu_speed
    

    

