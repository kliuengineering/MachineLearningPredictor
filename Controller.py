"""

Authours:
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach

Module Description:
    - This module employs the observer pattern.
    - This module encapsulates the publisher to the observers (Views).
    - This module is part of the MVC architecture - Controller.

"""   


from abc import ABC, abstractmethod
from Model import MachineLearningModel
from Views import MultiView


# << interface >> Abstract Publisher
class Controller(ABC):
    @abstractmethod
    def attach_view(self):
        pass

    @abstractmethod
    def detach_view(self):
        pass

    @abstractmethod
    def notify_views(self):
        pass

    @abstractmethod
    def train_model(self):
        pass

    @abstractmethod
    def make_prediction(self, x:float):
        pass


# Concrete Publisher A
class TaylorController(Controller):
    def __init__(self):
        self._model = MachineLearningModel()
        self._views = MultiView()
        self.training_complete = 0

    def attach_view(self) -> None:
        self._views.attach_view()

    def detach_view(self) -> None:
        self._views.detach_view()

    def notify_views(self, type: str, message: float | list | str) -> None:
        self._views.notify(type, message)

    def train_model(self) -> None:
        self._model.mount_model()
        self._model.execute()
        self.training_complete = 1

    def make_prediction(self, x: float | list) -> None:
        prediction = self._model.predict(x)
        self.notify_views("prediction", prediction)
    

# Driver class for the Client -> interfacing the end Client
class MachineLearning:
    def __init__(self):
        try:
            self._controller = TaylorController()
        except:
            raise ValueError("Exception occurred at run time, abort routine...\n")
    
    def run(self, input_data: list) -> None:
        if not self._controller.training_complete:
            self._controller.train_model()
        self._controller.attach_view()
        self._controller.make_prediction(input_data)
        self._controller.detach_view()

