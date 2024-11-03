"""

Authours:
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach

Module Description:
    - This module employs the Strategy pattern.
    - This module encapsulates the business logic.
    - This module is part of the MVC architecture - Model.

"""   

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import math


# << interface >>, abstract strategy
class Model(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def error_analysis(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


# concrete strategy A
class TaylorModel(Model):
    """ parametric constructor. """
    def __init__(self, frequency=50.0, steps=360, tolerance=0.001):
        self.name = "Taylor Model"
        self.PI = 3.141592653589793238
        self.frequency = frequency
        self.steps = steps
        self.weights = [0.0 for _ in range(steps)]
        self.angular_velocity = 2.0 * self.PI * self.frequency
        self.period = 1.0 / self.frequency
        self.TOLERANCE = tolerance
        self.cost = float("inf")
        self.epochs = 0
        self.model_is_trained = False

    """ private computational methods -> for Taylor expansion """
    def _power(self, x: float, n: int) -> float:
        result = 1.0
        for _ in range(n):
            result *= x
        return result
    
    def _factorial(self, x: int) -> int:
        if x <= 1:
            return x
        else:
            return x * self._factorial(x-1)

    def _compute(self, x: float) -> float:
        result = 0.0

        for n in range(self.epochs):
            term = (-1)**n * self._power(x, 2*n+1) / self._factorial(2*n+1)
            result += term

        # self.epochs += 1
        return result
    
    """ private computational methods -> the trained Taylor expansion model. """
    def _trained_model(self, x: float, expansion_terms: int) -> float:
        result = 0.0

        for n in range(expansion_terms):
            current_term = (-1)**n * self._power(x, 2*n + 1) / self._factorial(2*n + 1)
            result += current_term
        return result

    """ Trains the model using Taylor Series approximation. """
    def train(self, debug: bool = False) -> bool:
        for i in range(self.steps // 4 + 1):                        # 1st quadrant approximation
            time = self.period * i / self.steps
            x = self.angular_velocity * time                        # angular displacement
            self.weights[i] = self._compute(x)                      # training epoc begins here

        for i in range(self.steps // 4, self.steps // 2):           # 2nd quadrant approximation
            self.weights[i] = self.weights[self.steps // 2 - i]     # odd function symmetry

        for i in range(self.steps // 2, self.steps):                # 3th + 4th quadrant approximation
            self.weights[i] = -self.weights[i - self.steps // 2]    # odd function symmetry again

        # Plot the current approximation after each epoch, only invoked in DEBUG mode
        if debug:
            self.plot_approximation()
            print("")

        if self.error_analysis():
            self.model_is_trained = True
            return True
        else:
            self.epochs += 1                                        # increments epoch if not converged
            return False

    """ Analyzes the error using standard deviation. """
    def error_analysis(self) -> bool:
        diff_sum = 0.0

        for i in range(self.steps):
            time = self.period * i / self.steps                     # get current delta-t
            true_value = math.sin(self.angular_velocity * time)     # get the ground truth
            diff_sum += (self.weights[i] - true_value) ** 2         # squared error sum
        std_dev = math.sqrt( diff_sum / (self.steps - 1) )          # n-1 sample

        if std_dev > self.TOLERANCE:
            print(f"stdDev: {std_dev}, epochs: {self.epochs + 1}\nERROR: The training model is inaccurate!\n")
            return False
        else:
            print(f"The training model is accurate with stdDev: {std_dev} and epochs: {self.epochs + 1}\n")
            return True
        
    """ Prediction by the trained model. """
    def predict(self, x: float | list, in_degrees: bool = False) -> dict:
        if not self.model_is_trained:
            raise ValueError("Model is not trained yet... Please train the model before making predictions...")
        
        # checks for degree / radian
        if in_degrees:
            if isinstance(x, float):
                x = x * self.PI / 180
            elif isinstance(x, list):
                x = [ itr * self.PI / 180 for itr in x ]
        
        else:
            if isinstance(x, float):
                return { x: self._trained_model(x, self.epochs + 1) }           # max # of terms is basically the epochs + 1
            if isinstance(x, list):
                # return [ self._trained_model(itr, self.epochs + 1) for itr in x ]
                return { angle: self._trained_model(angle, self.epochs + 1) for angle in x }

    """ only used in the debug mode """
    def plot_approximation(self):
        # Generate the true sine wave
        x_values = [self.angular_velocity * self.period * i / self.steps for i in range(self.steps)]
        true_sine = [math.sin(x) for x in x_values]

        # Plot the Taylor approximation
        plt.plot(x_values, self.weights, label=f"Taylor Approximation (Epoch {self.epochs + 1})")
        plt.plot(x_values, true_sine, label="True Sine Wave", linestyle="--", color="gray")
        plt.xlabel("Angle (radians)")
        plt.ylabel("Sine Value")
        plt.title("Taylor Series Approximation vs True Sine Wave")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    """ gets the name of the model """    
    def get_name(self) -> str:
        return self.name
        

# Context (interface) for the client side
class MachineLearningModel:
    def __init__(self, model: Model | None = None, max_iteration=10000):
        self.model = model
        self.MAX_ITERATION = max_iteration
        
    def __str__(self) -> str:
        return f"Current model is set to -> {self.model.get_name()}\n"

    """ private utility method """
    def _set_model(self, model_type:str) -> bool:
        if int(model_type) == 1:
            self.model = TaylorModel()
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
            raise TypeError("Invalid model selection, aborting...\n")

    """ controller invoked method -> main execution of the model """        
    def execute(self, debug: bool = False) -> bool:
        iteration = 0
        while (self.model.train(debug) == False) and (iteration < self.MAX_ITERATION): # here
            iteration += 1

    """ selected model prediction, takes in a single float or an array of floats """
    def predict(self, x: float | list) -> dict:
        return self.model.predict(x)
    
