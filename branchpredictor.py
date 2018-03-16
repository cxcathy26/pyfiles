from array import array

class BranchPredictor : 

    # constructor for tournament predictor
    def __init__(self):
        self.mode = -1

    def configure_tournament(self, nbts, m0, n0, k0, m1, n1, k1):
        self.mode = 2   # two because we are using two predictors
        self.verbose = 0
        self.nbts = nbts
        self.mask_selector_index = (1 << nbts) - 1
        self.predictor0 = BranchPredictor()
        self.predictor0.configure(m0, n0, k0)
        self.predictor1 = BranchPredictor()
        self.predictor1.configure(m1, n1, k1)
        self.reset()

    # constructor for bimodal predictor
    def configure(self, m, n, k):
        self.mode = 1   # one because we are using one predictor
        self.verbose = 0
        self.m = m
        self.n = n
        # TODO: add your code here before calling reset
        # For example, you can generate masks here. 
        #   mask_ghr = (1 < m) - 1
        self.reset()

    def reset(self):
        if (self.mode == 1):
            self.g_hist= 0
            # creates an array of size 2^(nb_i) filled with zeroes, for counters
            # the data in the array is of type 'signed char', specified by the first argument
            # you need to calculate the number of counters. Use << operation 
            # TODO
        elif (self.mode == 2):
            self.predictor0.reset()
            self.predictor1.reset()
            self.num_selected0 = 0;
            # create an array of bytes for selectors  
            # TODO
        self.num_branches = 0
        self.num_taken = 0
        self.num_mispredictions = 0

    def set_verbose(self, v):
        if (self.mode == 1):
            self.verbose = v
        elif (self.mode == 2):
            self.verbose = v
            self.prediction0.set_verbose(v)
            self.prediction1.set_verbose(v)

    # return 1 for taken prediction 
    # return 0 for not-taken
    def predict(self, addr, outcome):
        self.num_branches += 1
        self.num_taken += outcome
        # remember to set the prediction (the return value) for all cases
        # it is set to 0 for now, always predicting not-taken.
        prediction = 0
        if (self.mode == 1):
            # Predict, update, return
            # TODO
            # update global history
            self.g_hist = (self.g_hist << 1) + outcome
        else:
            # Predict, update, return 
            prediction0 = self.predictor0.predict(addr, outcome) 
            prediction1 = self.predictor1.predict(addr, outcome) 
            # now you need to check which predition to use
            # and update the selector
            # keep track how many times predictor0 is used
            # TODO
        return prediction

    # report the statistics
    def report(self):
        if (self.mode == 1):
            print("Total number of branches   = {}".format(self.num_branches))
            print("Number of taken branches   = {}".format(self.num_taken))
            print("Number of untaken branches = {}".format(self.num_branches - self.num_taken))
            print("Number of mispredictions   = {}".format(self.num_mispredictions))
            if (self.num_branches):
                print("Misprediction rate         = {:.2f}%".format(self.num_mispredictions/self.num_branches * 100))
        elif (self.mode == 2):
            print("Predictor 0:")
            self.predictor0.report()
            print("\nPredictor 1:")
            self.predictor1.report()
            print("\n")
            if (self.num_branches):
                print("Misprediction rate         = {:.2f}%".format(self.num_mispredictions/self.num_branches * 100))
                print("Percentage of using 0      = {:.2f}%".format(self.num_selected0/self.num_branches * 100))

