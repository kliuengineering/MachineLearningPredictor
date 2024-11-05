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
    def make_prediction(self):
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

    def train_model(self, model = None, debug: bool = False) -> None:
        self._model.mount_model(model)
        self._model.execute(debug)       
        self.training_complete = 1

    def make_prediction(self, x: float | list) -> None:
        prediction = self._model.predict(x)
        self.notify_views("prediction", prediction)
    

# Driver class for the Client -> interfacing the end Client
class MachineLearning:
    def __init__(self, debug: bool = False):
        self._instantiation = False
        self._debug = debug
        self._controller = None
        self._model_type = None

    """ private -> get user preference """
    def _set_model(self) -> None:
        print(             "Choose a model to mount: \n",
                           "\t[1] Taylor Approximation \t(available) \n",
                           "\t[2] Polynomial Regression \t(under development) \n")             
        self._model_type = int(input("Your choice is -> "))

        try:
            if self._model_type == 1:
                self._controller = TaylorController()
        except:
            pass
    
    """ main routine """
    def run(self, input_data: list) -> None:
        if not self._model_type:
            self._set_model()
        if not self._controller.training_complete:
            self._controller.train_model(self._model_type, self._debug)               
        self._controller.attach_view()
        self._controller.make_prediction(input_data)
        self._controller.detach_view()

    """ enforces check before running the instance """
    def instantiation_success(self) -> bool:
        self._instantiation = True
        return self._instantiation

