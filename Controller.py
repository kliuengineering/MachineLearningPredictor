"""

Observer pattern is used for the controller module of the MVC.

"""


from abc import ABC, abstractmethod
from Model import MachineLearningModel
from Views import MultiView


# << interface >>, abstract subscriber
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


# concrete subscriber for Taylor Approximation
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


def main():
    controller = TaylorController()


if __name__ == "__main__":
    main()