"""

Development Log:

October 25, 2024
    - Refactored for future scalability;
      models in general should have training and validation methods.
        + Employed strategy pattern.
        + Studied the mechanics of Taylor approximation.

October 28, 2024
    - Bug fixes
        + Added input validation and test cases.

"""

from abc import ABC, abstractmethod
import math

# << interface >>, abstract strategy
class Model(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def error_analysis(self):
        pass


# concrete strategy A
class TaylorModel(Model):
    """ parametric constructor. """
    def __init__(self, frequency=50.0, steps=360, tolerance=0.001) -> None:
        self.name = "Taylor Model"
        self.PI = 3.141592653589793238
        self.frequency = frequency
        self.steps = steps
        self.weights = [0.0 for _ in range(steps)]
        self.angular_velocity = 2.0 * self.PI * self.frequency
        self.period = 1.0 / self.frequency
        self.TOLERANCE = tolerance

    """ private -> computes Taylor expansion """
    def _compute(self, x: float, tolerance: float) -> float:
        pass

    """ Trains the model using Taylor Series approximation. """
    def train(self) -> None:
        for i in range(self.steps // 4 + 1):                        # 1st quadrant approximation
            time = self.period * i / self.steps
            x = self.angular_velocity * time                        # angular displacement
            self.weights[i] = x                                     # caches angular displacement

        for i in range(self.steps // 4, self.steps // 2):           # 2nd quadrant approximation
            self.weights[i] = self.weights[self.steps // 2 - i]     # odd function symmetry

        for i in range(self.steps // 2, self.steps):                # 3th + 4th quadrant approximation
            self.weights[i] = -self.weights[i - self.steps // 2]    # odd function symmetry again

    """ Analyzes the error using standard deviation. """
    def error_analysis(self) -> bool:
        diff_sum = 0.0

        for i in range(self.steps):
            time = self.period * i / self.steps                     # get current delta-t
            true_value = math.sin(self.angular_velocity * time)     # get the ground truth
            diff_sum += (self.weights[i] - true_value) ** 2         # squared error sum
        std_dev = math.sqrt( diff_sum / (self.steps - 1) )          # n-1 sample

        if std_dev > self.TOLERANCE:
            print(f"\nstdDev: {std_dev}\nERROR: The training model is inaccurate!\n")
            return False
        else:
            print("The training model is accurate.\n")
            return True

    """ gets the name of the model """    
    def get_name(self) -> str:
        return self.name
        

# Context (interface) for the client side
class MachineLearningModel:
    def __init__(self, model: Model | None = None):
        self.model = model
        self.cost = float("inf")                                    # we assign the cost to be inf. to start with

    def __str__(self) -> str:
        return f"Current model is set to -> {self.model.get_name()}\n"

    """ private utility method """
    def _set_model(self, model_type:str) -> bool:
        if int(model_type) == 1:
            self.model = TaylorModel()
            self.cost = float("inf")                                # initializes the cost every time we set a new model
            print(self)
            return True
        else:
            return False

    """ user invoked method -> chooses a model to mount """
    def mount_model(self) -> bool:
        print(             "Choose a model to mount: \n",
                           "\t[1] Taylor Approximation \t(available) \n",
                           "\t[2] Polynomial Regression \t(under development) \n")             
        model_type = input("Your choice is -> ")

        self._set_model(model_type)
        
        if self.model:
            return True
        else:
            exit("\nError mounting the model, abort routine...\n")

    """ user invoked method -> main execution of the model """        
    def execute(self) ->  bool:
        self.mount_model()
        self.model.train()
        
        rc = self.model.error_analysis()
    

def main():
    model = MachineLearningModel()
    model.execute()


if __name__ == "__main__":
    main()