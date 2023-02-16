import matplotlib.pyplot as plt
import numpy as np

def step(w0: float, w1: float, alpha: float):
    '''
    Gradient descent step; you probably wanna return new w0, w1
    '''
    pass


def main():
    # your global subplot
    _, subplot = plt.subplots()
    
    X = np.array([[1, 2], [1, 3]])

    # our shape of X_1 = (2, 2)

    # print(X_1)

    y = np.array([[4], [3]])
    # our shape of y_2d = (2, 1)
    # Metadata
    
    w_0, w_1 = 0, 0
    
    plt.title("Learning rates")
    plt.xlabel("w0")
    plt.ylabel("w1")
    
    num_iters = 10

    for alpha in [0.06, 0.001, 0.03]:
        # Make container for w0's and w1's

        w0_container = []
        w1_container = []
        
        w_0 = 0
        w_1 = 0
        for i in range(num_iters):
            # Step through gradient descent
            # Calculate f
            # Collect w0, w1 in containers
            
            # temp_0 = w_0 - alpha * (w_0 * X[0][0] + w_1 * X[0][1] - y[0][0]) * X[0][0] - alpha * (w_0 * X[1][0] + w_1 * X[1][1] - y[1][0]) * X[1][0]
            # temp_1 = w_1 - alpha * (w_0 * X[0][0] + w_1 * X[0][1] - y[0][0]) * X[0][1] - alpha * (w_0 * X[1][0] + w_1 * X[1][1] - y[1][0]) * X[1][1]
            
            

            temp_0 = w_0 - alpha * 2 * (w_0 * 1 + w_1 * 2 - 4) * 1 - alpha * 2 * (w_0 * 1 + w_1 * 3 - 3) * 1
            temp_1 = w_1 - alpha * 2 * (w_0 * 1 + w_1 * 2 - 4) * 2 - alpha * 2 * (w_0 * 1 + w_1 * 3 - 3) * 3

            w_0 = temp_0
            w_1 = temp_1
            w0_container.append(w_0)
            w1_container.append(w_1)
            f_w = (w_0 * 1 + w_1 * 2 - 4)**2 + (w_0 * 1 + w_1 * 3 - 3)**2
            # Probably print all three values to submit to gradescope    
            print("alpha: ", alpha)        
            print("iteration_num", i, "w0: ", w_0, "w1: ", w_1, "f_w: ", f_w)
        print("=====================================")
        
        # Plot current descent
        subplot.scatter(w0_container, w1_container, label=alpha) # replace x, y with continers

    # Generate legend and show graph
    subplot.legend()
    plt.show()

main()