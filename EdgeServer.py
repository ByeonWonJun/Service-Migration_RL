from EdgeUser import User
import numpy as np

class EdgeEnv():
    
    def __init__(self, server_cpu_speed , dataRate, computing_resource ):
                                     
        self.max_delay = 1000
        self.server_cpu_speed = server_cpu_speed*1e6 # n*1GB/s -> 2KB/s
        self.dataRate = dataRate
        self.cpu_cycle_num = 0.1e9
        self.fixedData = 1024*3 # 3KB
        
        self.avg_taskTrans_rate = 1024
        self.avg_dis_hop = 2
        self.computing_resource = computing_resource
        self.avg_taskTrans_EdgeRate = 1024
        self.avg_dis_EdgeHop = 2
        
        self.dataRateLocal = User(self.dataRate)
        
    
    def getWirelessTransmission(self):
        return self.fixedData*self.dataRate/self.dataRateLocal.ChannelCapacity

    def getTransmissionTime(self):
        return self.fixedData*self.dataRate/self.avg_taskTrans_rate*self.avg_dis_hop
    
    def getEdgeProcessingTime(self):
        return self.dataRate*self.cpu_cycle_num/(self.server_cpu_speed*self.computing_resource)
    
    def getMigrationTime(self):
        return 2*self.fixedData*self.dataRate/self.avg_taskTrans_EdgeRate*self.avg_dis_EdgeHop
    
    def getEdgeTotlaTime_Nomigration(self):
        return self.getWirelessTransmission()+self.getTransmissionTime()+self.getEdgeProcessingTime()
    
    def getEdgeTotlaTime_migration(self):
        return self.getWirelessTransmission()+self.getTransmissionTime()+self.getEdgeProcessingTime()+self.getMigrationTime()
    
    def getMaxTime(self):
        return max(self.dataRateLocal.getLocalTime(),self.getEdgeTotlaTime_migration(),self.getEdgeTotlaTime_Nomigration())
    
    

