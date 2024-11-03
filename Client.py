
import random
from Controller import MachineLearning

def main():
    inputData = []
    ret = 0

    # Add code
    prints = PrintStuff()
    prints.begin()
    choice = Validate( input("Do you want to enter DEBUG mode? [Y/N]: ") )

    model = MachineLearning(choice)
    ret = model.instantiation_success()

    if ret == True:
        # Generate some random data and make predictions, five times
        TRIALS = 5
        for i in range(TRIALS):
            prints.iteration(i+1)
            NUM = 1000
            for j in range(NUM):
                inputData.append(random.random())  # generate a number between 0 and 1
            
            # Make a prediction using the trained model and display it in all views
            model.run( inputData )
            
            # clear out the list for the next trial
            inputData.clear()
    else:
        raise ValueError("Model instantiation failure, abort program...\n")

    prints.end()


# utility class for printing some stuff
class PrintStuff:
    def iteration(self, num: int) -> None:
        print(f"\n\n===================== iteration {num} =====================\n")

    def separation(self) -> None:
        print(f"\n===========================================================\n\n")

    def end(self) -> None:
        print(f"\n===================== END OF PROGRAM ======================\n\n")

    def begin(self) -> None:
        print(f"\n=================== START OF PROGRAM ======================\n\n")


# utility function for input validation
def Validate(s: str):
    if s.lower() == "y":
        print("Entering DEBUG: you will observe the training epochs.\n")
        return True
    elif s.lower() == "n":
        print("Entering NORMAL mode: you will not see training epochs.\n")
        return False
    else:
        raise ValueError('Incorrect Entry: You must enter either "Y" or "N", abort program...\n')


if __name__ == '__main__':
    main()




                
            