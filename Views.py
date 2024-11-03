"""
TODO: 
    1. write the graphical view class
    2. write the console view class

"""   

import matplotlib.pyplot as plt

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

    # Plot the current approximation after each epoch
    self.plot_approximation()