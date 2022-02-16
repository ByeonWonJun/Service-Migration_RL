import numpy as np
import time

class User():
    def __init__(self,dataRate):
        
        self.cpu_speed = 250000 #  250MB/s ->1KB/s
        self.max_delay = 1000
        self.user_speed = 100*1000/(60*60) # 100Km/h -> m/s : 27.777
        self.dataRate = dataRate
        self.cpu_cycle_num = 0.1e9
        self.fixedData = 1024*3
        
        self.position = 0
        self.savedPosition = 0
        
        self.trans_power = 100
        self.SNR = -40
        self.path_loss_exp = 3.5
        
        self.edges= 0
        #self.Bandwidth = 3000
        
        self.ChannelCapacity = 360/8*np.log2(1 + (self.trans_power * np.power(self.position, -1 * self.path_loss_exp)) / np.power(10, self.SNR / 10))
        
    def getLocalTime(self):
        return self.cpu_cycle_num*(1-self.dataRate)/self.cpu_speed
    
    def getNowServer(self, time):
        if self.savedPosition == 0:
            for i in range(186):
                self.position += user_speed
                self.savedPosition += self.user_speed
                time.sleep(0.001)
                if self.savedPosition < 1000:
                    return edges = 0
                
                elif self.savedPosition >= 1000 && self.savedPosition < 2000:
                    self.position = 0
                    return edges = 1
                
                elif self.savedPosition >= 2000 && self.savedPosition < 3000:
                    self.position = 0
                    return edges = 2
                
                elif self.savedPosition >= 3000 && self.savedPosition < 4000:
                    self.position = 0
                    return edges = 3
                
                elif self.savedPosition >= 4000 && self.savedPosition < 5000:
                    self.position = 0
                    return edges = 4
                
                else:
                    break
               
            
            
    

    

