# Data Layer Class
class DataLayer:
  
  def __init__(self):
    self.name = "Data Layer"
    
  def setLowerLayer(self, lowerLayer):
    self.lowerLayer = lowerLayer
    
  def service_layer_1(self, param):
    print("dentro de  %s" % self.name)
    print("ejecutamos service_layer_1 con %s" % param)