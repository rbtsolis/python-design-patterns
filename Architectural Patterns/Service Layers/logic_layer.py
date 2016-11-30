# Logic Layer Class
class LogicLayer:
  
  def __init__(self):
    self.name = "Logic Layer"
    
  def setLowerLayer(self, lowerLayer):
    self.lowerLayer = lowerLayer
    
  def service_layer_2(self, param):
    print("entramos al %s " % self.name)
    self.lowerLayer.service_layer_1(param)
    print("terminamos %s " % self.name)