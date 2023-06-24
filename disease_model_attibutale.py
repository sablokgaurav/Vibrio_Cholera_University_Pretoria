import os
import arguably 
import pyprofilers as pp
import pandas as pd
@pp.profile(sort_by='cumulative', out_lines=30) 
@pp.profile_by_line(exit=1) 
@pp.simple_timer(num=1)
snap = CodeSnap()
snap = CodeSnap(tracer="python") 
snap.start()
@arguably.command 
def attibutable_fractions(dataframe = False):
    """
    _summary_
    A python function to calcuate the attributable fractions in 
    infected virbio areas outbreak. 
    """
    if dataframe:
        while True:
            take_dataframe = input("Please enter the infected population \
                metrics csv file:")
            take_exposed = input("Please enter the infected exposed columns")
            take_unexposed = input("Please enter the unexposed columns")
            if take_dataframe and take_exposed and take_unexposed == "":
                break
            infected_dataframe = pd.read_csv(os.path.join(os.getcwd(), take_dataframe), sep = ",")
            exposed_population = infected_dataframe["take_exposed"]
            unexposed_population = infected_dataframe["take_unexposed"]
            exposed_risk = len(infected_dataframe["take_exposed"].to_list())//
                                     (len(infected_dataframe["take_exposed"].to_list()) + \
                                                    len(infected_dataframe["take_unexposed"].to_list()))
            unexposed_risk = len(uninfected_dataframe["take_unexposed"].to_list())//
                                        (len(infected_dataframe["take_exposed"].to_list()) + \
                                                    len(infected_dataframe["take_unexposed"].to_list()))
            prediction_risk = (exposed_risk - unexposed_risk)//exposed_risk
            attibutable_fraction =  prediction_risk*len(infected_dataframe["take_exposed"].to_list())// \
                                                           (len(infected_dataframe["take_exposed"].to_list()) + \
                                         len(infected_dataframe["take_unexposed"].to_list()))
            with open(predictive_risk_calculation, "r") as risk_cal:
                risk_cal.write(f"Number of exposed are: {exposed_risk} \
                                \nNumber of unexposed risk are: {unexposed_risk} \
                                \nThe prediction risk is : {prediction_risk} \
                                \nThe attibutable fractions is: {attibutable_fraction}")                            
            return prediction_risk, attributable_fraction
snap.stop()
snap.save()        
if __name__ == __main__:
    arguably.run() 
