def mapVibrio(self, csv, coord):
        self.__coord = coord
        self.__coord = []
        self.__distance = {}
        while True:
                take_coords = input("please enter the genomics coordinates:")
                self.__coord.append(take_coords)
                if take_coords == None:
                    break
        for i in range(len(self.__coord)):
            self.__distance[DbIpCity.get(self.__coord[i]), api = "free"] = [DbIpCity.city(self.__coord[i]),
                                                                            DbIpCity.latitude(self.__coord[i]),
                                                                            DbIpCity.longitude(self.__coord[i])]
            self.distance_dataframe = pd.Dataframe(self.__distance)
            return self.distance_dataframe
def printGeographicalMaps(self, ip_lat, ip_long, title):
        self.__ip_lat = ip_lat
        self.__ip_long = ip_long
        self.__ip_lat = []
        self.__ip_long = []
        self.__title = title
        while True:
            take_ip_lat = input("Please enter the geographical latitude:")
            take_ip_long = input("Please enter the geographical longitude:")
            self.__ip_lat.append(take_ip_lat)
            self.__ip_long.append(take_ip_long)
            if take_ip_lat or take_ip_long is None:
                print("Finished taking the IPs")
            return self.__ip_lat, self.__ip_long
        for i in range(len(self.__ip_lat)):
            map = folium.Map(location = (self.__ip_lat[i], self.__ip_long[i]), title = self.__title )
            map.save(geographical_map_chlorea.html) 