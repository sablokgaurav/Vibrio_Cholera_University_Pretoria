import os
import arguably 
import pyprofilers as pp
import pandas as pd
from geopy.geocoders import Nominatim
@pp.profile(sort_by='cumulative', out_lines=30) 
@pp.profile_by_line(exit=1) 
@pp.simple_timer(num=1)
snap = CodeSnap()
snap = CodeSnap(tracer="python") 
snap.start()
@arguably.command 
def geograhicalOutbreakOdds(population_dataframe = False,\
                            geo_dataframe = False,\
                                latitude = False,\
                                longitude = False):
    """
    _summary_
    estimating the geograhical odds of having an outbreak
    in a geospatial mode and estimating the geodistribution
    of the disease outbreak. This function will take the disease
    dataframe of two columns: exposed and unexposed, latitude and 
    longitude. The order should be latitude and longitude in one dataframe
    and the exposed and the unexposed in the another dataframe and the 
    geo corrdinates should correspond to the exposed and the unexposed
    populations count.
    
    """
    if population_dataframe, geo_dataframe and latitude:
         controls_exposed = []
         controls_unexposed = []
             while True:
                 take_contols_infected = input("Please input the number of the controls infected means\
                     that the number of the population that become infected without \
                         exposing to that latitude:")
                 take_control_non_infected = input("Please input the number of the controls non-infected means\
                     that the number of the population that become infected without \
                         exposing to that latitude:")
                 controls_exposed.append(take_controls_infected)
                 controls_unexposed.append(take_contols_non_infected)
                 if take_contols_infected and take_control_non_infected == "":
                     break
                     print (f"odd ratio for the predictability cant be calculated as 
                            the controls infected and non-ingected are not defined 
                            and the details of the ex: {unexposed}, {exposed} and {latitude_char}")
             disease_dataframe = pd.read_csv(os.path.join(os.getcwd(), population_dataframe))
             geographical_dataframe = pd.read_csv(os.path.join(os.getcwd(), geo_dataframe))
             merged_dataframe = pd.concat([disease_dataframe, geographical_dataframe])
             latitude_wide = latitude
             latitude_dataframe = merged_dataframe[::].where(merged_dataframe["latitude"] == latitude_wide)
             exposed = merged_dataframe[::].where(merged_dataframe["latitude"] \ 
                                                    == latitude_wide).iloc[::,1].to_list()
             unexposed = merged_dataframe[::].where(merged_dataframe["latitude"] \
                                                    == latitude_wide).iloc[::,3].to_list()
             latitude_char = merged_dataframe[::].where(merged_dataframe["latitude"] \
                                                   == latitude_wide).iloc[::,3].to_list()         
            odd_ratio_1 = (exposed//controls_exposed)
            odd_ratio_2 = (unexposed//control_unexposed)
            odd_ratio_print = odd_ratio_1//odd_ratio_2
            odd_ratio_location = geolocator.reverse("str(''.join(merged_dataframe[::].where(merged_dataframe["latitude"] \
                                                   == latitude_wide).iloc[::,3].to_list())),\
            str(''.join(merged_dataframe[::].where(merged_dataframe["longitude"] \
                                                   == longitude_wide).iloc[::,4].to_list()))")
            print(f"the odd ratio and the predictability of the outbreak in this latitude is {odd_ratio_print}")
            print(f"The location for the odd ratio is {odd_ratio_location}")
            print(f"The location latitude and the latitude are {odd_ratio_location.latitude}, {odd_ratio_location.longitude}")
            print(f"The raw address is {odd_ratio_location.raw}")
            
            
    elif population_dataframe, geo_dataframe and longitude:
         controls_exposed = []
         controls_unexposed = []
             while True:
                 take_contols_infected = input("Please input the number of the controls infected means\
                     that the number of the population that become infected without \
                         exposing to that longitude:")
                 take_control_non_infected = input("Please input the number of the controls non-infected means\
                     that the number of the population that become infected without \
                         exposing to that longitude:")
                 controls_exposed.append(take_controls_infected)
                 controls_unexposed.append(take_contols_non_infected)
                 if take_contols_infected and take_control_non_infected == "":
                     break
                     print (f"odd ratio for the predictability cant be calculated as 
                            the controls infected and non-ingected are not defined 
                            and the details of the ex: {unexposed}, {exposed} and {latitude_char}")
             disease_dataframe = pd.read_csv(os.path.join(os.getcwd(), population_dataframe))
             geographical_dataframe = pd.read_csv(os.path.join(os.getcwd(), geo_dataframe))
             merged_dataframe = pd.concat([disease_dataframe, geographical_dataframe])
             longitude_wide = longitude
             longitude_dataframe = merged_dataframe[::].where(merged_dataframe["longitude"] == longitude_wide)
             exposed = merged_dataframe[::].where(merged_dataframe["longitude"] \ 
                                                    == longitude_wide).iloc[::,1].to_list()
             unexposed = merged_dataframe[::].where(merged_dataframe["longitude"] \
                                                    == longitude_wide).iloc[::,3].to_list()
             longitude_char = merged_dataframe[::].where(merged_dataframe["longitude"] \
                                                   == longitude_wide).iloc[::,4].to_list()         
            odd_ratio_1 = (exposed//controls_exposed)
            odd_ratio_2 = (unexposed//control_unexposed)
            odd_ratio_print = odd_ratio_1//odd_ratio_2
            odd_ratio_location = geolocator.reverse("str(''.join(merged_dataframe[::].where(merged_dataframe["latitude"] \
                                                   == latitude_wide).iloc[::,3].to_list())),\
            str(''.join(merged_dataframe[::].where(merged_dataframe["longitude"] \
                                                   == longitude_wide).iloc[::,4].to_list()))")
            print(f"the odd ratio and the predictability of the outbreak in this latitude is {odd_ratio_print}")
            print(f"The location for the odd ratio is {odd_ratio_location}")
            print(f"The location latitude and the latitude are {odd_ratio_location.latitude}, {odd_ratio_location.longitude}")
            print(f"The raw address is {odd_ratio_location.raw}")
    else:
        print(f"this function cant be executed because there are no corrdinates \
                                selected and neither the amount of the outbreak defined")
snap.stop()
snap.save()
if __name__ ==  "__main__":
    arguably.run()        
