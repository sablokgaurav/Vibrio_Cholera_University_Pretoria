 def controlFactors(self, control, replicates):
        """
        this functions takes the expression data and sum them
        along the replicates so that you can take the control
        mean across all the control and the replicates
        """
        self.__control = []
        while True: 
                take_control = input("Please enter the control columns:")
                self.__control.append(take_control)
                if take_control is None:
                    break
                self.controls = self.final_factors[self.__control]
                self.controls["cummulative_exp"] = self.final_factors[self.__control].dropna().apply(lambda n: sum(n), axis=1)
        self.__replicates = []
        while True:
            take_replicates = input("Please enter the replicates columns:")
            self.__replicates.append(take_replicates)
            if take_replicates is None:
                break
            self.replicates = self.final_factors[self.__replicates]
            self.replicates["cummulative_exp"] = self.final_factors[self.__replicates].dropna().apply(lambda n: sum(n), axis = 1)