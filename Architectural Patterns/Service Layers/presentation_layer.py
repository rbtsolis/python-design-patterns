# Presentation Layer Class
class PresentationLayer:
  
  # Constructor Method
  def __init__(self):
    self.name = "Presentation Layer"
    
  def setLowerLayer(self, lowerLayer):
    self.lowerLayer = lowerLayer
    
  def service_layer_3(self, param):
    print("entramos al %s " % self.name)
    self.lowerLayer.service_layer_2(param)
    print("terminamos %s " % self.name)