 def  OnlineRetrival(self,onlinelinkGenome, onlinelinkCDS, 
                               onlinelinkProteins, onlinelinkGFF):
        """
        if you have been provided the links to the online fasta,
        coding regions, proteins sequences and gff files then fetch
        them using this function. 
        """
        self.__onlinelinkGenome = onlinelinkGenome
        self.__onlinelinkCDS = onlinelinkCDS
        self.__onlinelinkProteins = onlinelinkProteins
        self.__onlinelinkGFF = onlinelinkGFF
        self.onGenome = wget.download(self.__onlinelinkGenome)
        self.onCDS = wget.download(self.__onlinelinkCDS)
        self.onProteins = wget.download(self.__onlinelinkProteins)
        self.onGFF = wget.download(self.__onlinelinkGFF)