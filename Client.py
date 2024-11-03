
import random
from Controller import MachineLearning

def main() -> int:
    inputData = []
    ret = 0

    # Add code
    model = MachineLearning()
    prints = PrintStuff()

    if ret == 0:
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

    prints.end()


# utility class for printing some stuff
class PrintStuff:
    def iteration(self, num: int) -> None:
        print(f"\n\n===================== iteration {num} =====================\n")

    def separation(self) -> None:
        print(f"\n===========================================================\n\n")

    def end(self) -> None:
        print(f"\n===================== END OF PROGRAM ======================\n\n")


if __name__ == '__main__':
    main()




                
            