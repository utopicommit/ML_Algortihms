import argparse

#standard parser to read the data and set certain parameters for the algorithm
parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str, default = 'random3.csv')
#deault learning rate
parser.add_argument("--eta", type = float, default = 0.00005)
#threshold of difference of error for the algorithm to stop learning
parser.add_argument("--threshold", type = float, default = 0.0001)
args = parser.parse_args()
data = args.data
eta = args.eta
threshold = args.threshold

#batch descent
def BDM(data, eta, threshold):
    #data is the name of the CSV file, eta is the learning rate and threshold is the allowance of difference
    #of error up until the algorithm should stop
    f = open(data, 'r')
    #labels
    X = []
    #target variable
    y = []

    for line in f:
        l = line.split(',')
        x1, x2, a = float(l[0]), float(l[1]), float(l[2].strip())
        X.append([x1, x2])
        y.append(a)
            

    m = len(X)
    for i in range(m):
        X[i] = [1] + X[i]

    w = []
    ##Initializing weights
    for i in range(len(X[0])):
        w.append(0)
    
    check = 1
    iteration = 0
    sse = [0]

    while check > threshold:
        
        grad = 0
        error = 0
        g = [0,0,0]
        for j in range(len(X)):
            
            f = [m * l for m,l in zip(w, X[j])]
            f_x = sum(f)
            res = (y[j] - f_x)
            grad = [i * (y[j] - f_x) for i in X[j]]
            
            g = [sum(t) for t in zip(g, grad)]
            
            error += abs(res*res)
        
        weights = str(iteration) + ','
        w1 = list(w)
        for i in range(len(w)):    
            weights = weights + str(w1[i])+','
        weights += str(error)
        print(weights)
        
        w = [p + eta*gradient for p, gradient in zip(w,g)]
        sse.append(error)

        check = abs(sse[len(sse)-2]-sse[len(sse)-1])
       
        iteration += 1
        
BDM(data, eta, threshold)