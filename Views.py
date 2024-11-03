"""

Authours:
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach

Module Description:
    - This module employs the observer pattern.
    - This module encapsulates the subscribers to the main even manager (Controller).
    - This module is part of the MVC architecture.

"""   


from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np


# << interface >> Abstract Subscriber
class View(ABC):
    @abstractmethod
    def update(self):
        pass


# Concrete Subscriber A
class ConsoleView(View):
    def update(self, message: dict | str):
        print("Console data received...")

        if isinstance(message, str):
            print(message, "\n")

        if isinstance(message, dict):
            print("x\t\tf(x)\t")
            for x, f_x in message["data"].items():
                print(f"{x:.5f}\t\t{f_x:.5f}")
            print("")


# Concrete Subscriber B
class GraphicalView(View):
    def update(self, message: dict | str):
        print("Graphical data received...")

        if isinstance(message, str):
            print(message, "\n")

        if isinstance(message, dict):
            print("Graph view computation begins...")
            parsed_data = self._parse_message(message)

            self._plt_graph(parsed_data)

            print("Graphs shown as pop-up windows...\n")

    """ utility parsing method """
    def _parse_message(self, message: dict) -> dict:
        parsed_data = { x : f_x for x, f_x in message["data"].items()  }
        return parsed_data
    
    """ utility graphing method """
    def _plt_graph(self, data: dict) -> None:
        x_values = list(data.keys())
        f_x_values = list(data.values())

        # Generate smooth curve for sin(x) over a full cycle from 0 to 2π
        x_smooth = np.linspace(0, 2 * np.pi, 500)
        y_smooth = np.sin(x_smooth)

        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Left graph: actual sin(x) curve over full cycle
        axes[0].plot(x_smooth, y_smooth, color='blue', label="sin(x)")
        axes[0].set_title("Actual sin(x) - Full Cycle")
        axes[0].set_xlabel("x (radians)")
        axes[0].set_ylabel("sin(x)")
        axes[0].grid(True)
        axes[0].legend()

        # Middle graph: predicted values as scatter plot
        axes[1].scatter(x_values, f_x_values, color='red', label="Predicted f(x)")
        axes[1].set_title("Predicted f(x) Values")
        axes[1].set_xlabel("x (radians)")
        axes[1].set_ylabel("f(x)")
        axes[1].grid(True)
        axes[1].legend()

        # Right graph: superimposed sin(x) and predicted f(x) values
        axes[2].plot(x_smooth, y_smooth, color='blue', label="sin(x)")
        axes[2].scatter(x_values, f_x_values, color='red', label="Predicted f(x)", zorder=5)
        axes[2].set_title("sin(x) vs Predicted f(x) - Full Cycle")
        axes[2].set_xlabel("x (radians)")
        axes[2].set_ylabel("Value")
        axes[2].grid(True)
        axes[2].legend()

        plt.tight_layout()
        plt.show()


# Driver classs for the Views -> interfacing the Controller
class MultiView:
    def __init__(self):
        self._view_container = {}
        
    def attach_view(self) -> None:
        print("Choose a view to be attached: \n",
                "\t[1] Console View \n",
                "\t[2] Graphical View \n",
                "\t[3] Both Views\n")
        try:
            view_type = int( input("Your choice is -> ") )
        except ValueError:
            exit("Invalid input, please enter a number next time...\n")

        if view_type == 1:
            self._view_container["console"] = ConsoleView()
            print("attached console view successfully.\n")

        elif view_type == 2:
            self._view_container["graphical"] = GraphicalView()
            print("attached graphical view successfully.\n")

        elif view_type == 3:
            self._view_container["console"] = ConsoleView()
            self._view_container["graphical"] = GraphicalView()
            print("attached console and graphical views successfully.\n")

        else:
            raise TypeError("Unrecognizable view attachment, abort routine...")

    def detach_view(self) -> None:
        view_mapping = {1: "console", 2: "graphical", 3: "both"}

        print("Choose a view to be detach: \n",
                "\t[1] Console View \n",
                "\t[2] Graphical View \n",
                "\t[3] Both Views\n")
        
        try:
            user_input = int(input("Your choice is -> "))
            view_type = view_mapping.get(user_input)
        except ValueError:
            exit("Invalid input, please enter a number next time...\n")     

        if view_type == "console" and "console" in self._view_container:
            del self._view_container["console"]
            print("Detached console view successfully.\n")

        elif view_type == "graphical" and "graphical" in self._view_container:
            del self._view_container["graphical"]
            print("Detached graphical view successfully.\n")

        elif view_type == "both":
            if "console" in self._view_container:
                del self._view_container["console"]
                print("Detached console view successfully.")
            if "graphical" in self._view_container:
                del self._view_container["graphical"]
                print("Detached graphical view successfully.\n")

        else:
            print("View does not exist or invalid choice.\n")

    def notify(self, type: str, message: dict | str) -> None:
        for view in self._view_container.values():
            if view is not None:
                view.update( {"type": type, "data": message} )

