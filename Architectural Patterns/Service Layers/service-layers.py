from presentation_layer import PresentationLayer
from logic_layer import LogicLayer
from data_layer import DataLayer



# This is main method in "Java"
if __name__ == "__main__":

  # Instance of the clases
  ui = PresentationLayer()
  logic = LogicLayer()
  data = DataLayer()
  
  ui.setLowerLayer(logic)
  logic.setLowerLayer(data)
  
  ui.service_layer_3("exampleParam")