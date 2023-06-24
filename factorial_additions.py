def addFactors(self, factors):
        """
        in this you are giving the additional factors for the
        analysis such as the environmental variables for the
        analysis and the class will automatically apply the 
        linear model and the mix model approach to classify
        them along with the genomic variables.
        """
        self.factors_machine = []
        self.factors_dataframe = self.factors_dataframe
        while True:
            take_factors = input("Please enter the path to the factors files:")
            self.factors_machine.append(take_factors)
            if take_factors == "None":
                break
            for i in range(len(self.factors_machine)):
                self.factors_dataframe += pd.read_csv(self.factors_machine[i], sep = ",")
                self.final_factors = pd.concat(self.factors_dataframe)