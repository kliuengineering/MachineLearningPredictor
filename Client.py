
import random

def main():
    inputData = []
    ret = 0

    # Add code

    if ret == 0:
        # Generate some random data and make predictions, five times
        TRIALS = 5
        for i in range(TRIALS):
            NUM = 1000
            for j in range(NUM):
                inputData.append(random.random())  # generate a number between 0 and 1
            # Make a prediction using the trained model and display it in all views

            # clear out the list for the next trial
            inputData.clear()
            print()

    # Add code

    return ret

if __name__ == '__main__':
    main()




                
            