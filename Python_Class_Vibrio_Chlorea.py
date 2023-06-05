# A vibrio clorela class that will read the genome and give you all the features,
# it will perform the IP and geographical localization of the sample collection
# sites, will estimate the coordinates, if you want to train the environmental 
# variables then it will train, if you want to train the sequences then it will
# train. It will prepare all the graphs and the maps. 
# ---> In the second release plus bug fixes this week adding the support for the multifasta,
# feature selection from multi fasta, feature drop estimation, BiLSTM application
# and application of the autoencoders.
# Gaurav Sablok
# Thulani Makhalanyane
# Senior Postdoctoral Fellow
# *Faculty of Natural and Agricultural Sciences*
# Room 7-35, Agricultural Sciences Building
# University of Pretoria, Private Bag X20
# Hatfield 0028, South Africa
# @ University of Pretoria
# Faculty of Natural and Agricultural Sciences

class VibrioMachineLearn:
    def __init__(self, fasta, expression_count, filename, outfile):
        """sumary_line
        in this you have to define the fasta file of the genome,
        expression count file from the metagenome transcriptomics
        filename to read and file name to write. it will return
        a linearized fasta file, and will also return a gff file
        as a dataframe for the count analysis. 
        """
        self.fasta = fasta
        self.expression_count = expression_count 
        self.filename = filename
        self.outfile = outfile
        self.fas = []
        self.names = ""
        self.filename = input("Enter the genome prediction file")
        with open(self.filename, "r") as fname:
            with open(outfile, "r") as text:
             for i in fname.readlines():
                if i[0] == "#":
                    continue
                else:
                    text.write(i)
                    text.close()     
                    self.gff = pd.read_csv("self.outfile", sep = "\t", header = T)

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

    def checkFasta(self, fasta):
        """
        this function will check whether you have a linear fasta
        or follows the NCBI fasta assembler rule and if it follows
        it converts into a linear fasta for easy retriveal of the
        genes 
        """
        self.__fasta = fasta
        if len(self.__fasta) == 2:
            print("Your fasta is presented as a linearized string")
        else:
            self.__sequences = []
            self.__names = ""
            with open(self.__fasta, "r") as f:
                for line in f.readlines():
                    if line.startswith(">"):
                        self.__sequences.append(self.names)
                        self.__names += line.strip()
                    else:
                        self.__sequences += line.strip()
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

    def exonDifference(self):
        exonstart = list(map(int,self.gff[["version", "start", "end", "feature"]].
                                              where(self.gff["feature"]=="exon").
                                                    dropna().iloc[::,1].tolist()))
        exonend = list(map(int,self.gff[["version", "start", "end", "feature"]].
                                                where(self.gff["feature"]=="exon").
                                                    dropna().iloc[::,2].tolist()))
        exondiff = []
        for i in range(len(exonstart)):
            exondiff.append(exonend[i] - exonstart[i])

    def geneDifference(self):
        genestart = list(map(int,list(map(int,self.gff[["version", "start", "end", "feature"]].
                                                            where(self.gff["feature"]=="gene")
                                                             .dropna().iloc[::,1].tolist()))))
        geneend = list(map(int,list(map(int,self.gff[["version", "start", "end", "feature"]].
                                                            where(self.gff["feature"]=="gene")
                                                            .dropna().iloc[::,2].tolist()))))
        genediff = []
        for i in range(len(genestart)):
           genediff.append(geneend[i] - genestart[i])
  
    def intronDifference(self):
        intronstart = list(map(int,self.gff[["version", "start", "end", "feature"]].
                                                 where(self.gff["feature"]=="intron")
                                                       .dropna().iloc[::,1].tolist()))
        intronend = list(map(int,self.gff[["version", "start", "end", "feature"]].
                                                  where(self.gff["feature"]=="intron")
                                                       .dropna().iloc[::,1].tolist()))
        introndiff = []
        for i in range(len(intronstart)):
            introndiff.append(intronend[i] - intronstart[i])
        
    def tRNADifference(self):
        tRNAstart = list(map(int,self.gff[["version", "start", "end", "feature"]].
                                                    where(self.gff["feature"]=="tRNA")
                                                          .dropna().iloc[::,1].tolist()))
        tRNAend = list(map(int,self.gff[["version", "start", "end", "feature"]]. 
                                                      where(self.gff["feature"]=="tRNA")
                                                         .dropna().iloc[::,1].tolist()))
        tRNAdiff = []
        for i in range(len(tRNAstart)):
            tRNAdiff.append(tRNAend[i] - tRNAstart[i])
            
    def getGenes(self,gff, start, stop):
         self.gff = pd.read_csv("gff", sep = "\t")
         self.__start = self.gff["start"].to_list()
         self.__end = self.gff["end"].to_list()
         self.__getgenes = []
         for i in range(len(self.__start)):
             self.__getgenes.append(self.fasta[self.__start:self.__end])
             self.__getgenes_dataframe = pd.DataFrame(self.__getgenes.append(self.fasta[self.__start:self.__end]))
             return self.__getgenes
         return self.__getgenes_dataframe

    def getIDs(self):
        return self.names
    def getSequences(self):
        return self.sequences
    def getDataframe(self):
        self._dataMatrix = [(i,j) for i,j in zip(self.names, self.sequences)]
        self.matrix = pd.DataFrame(self._dataMatrix)
        return self.matrix
    def getMeanLength(self):
        return self.matrix[1].apply(len).mean()
    def getMotifs(self, start, end):
        """_summary_
        Function to check the motifs before
        extraction and for the frequency
        calculations. This functions considers that
        you want to extract the same motif from all
        the sequence at the same position. 
        """
        self._start = start
        self._end = end
        extractMotif = {}
        for k,v in dict([(i,j) for i,j in zip(self.names, self.sequences)]):
            extractMotif[k] = v[self._start:self._end]
            return extractMotif
    def prepareMotifAlignment(self, start, end, filename):
        """_summary_
        Function to prepare the fasta files with the
        extracted motifs for the alignment
        """
        self._start = start
        self._end = end
        self.motifAlignment = list(map(lambda n: n[self._start: self._end]),
                              dict([(i,j) for i,j in zip(self.names, 
                                            self.sequences)]).values())
        self.motifNames = list(self.motifAlignment.keys())
        self.motifValues = list(self.motifAlignment.values())
        for i in range(len(self.motifNames)):
            print(">"+self.motifNames[i], self.motifValues[i], sep = "\n")
            with open(self.filename, "r+") as filename:
                filename.write(">"+self.motifNames[i], self.motifValues[i], sep = "\n")
                filename.close()
        return self.motifAlignment.keys(),list(self.motifAlignment.values())
    def frequencyCalculation(self):
        """_summary_
        Function to calculate the frequency composition of the
        observed motifs.
        """
        self.dataframe_names = pd.DataFrame([(i,j) for i,j in 
                                  zip(self.names,self.sequences)])[0].to_list()
        self.dataframe_sequences = pd.DataFrame([(i,j) for i,j in 
                                  zip(self.names,self.sequences)])[1].to_list()
        self.dataframe_character_count = list(map(lambda n: [(i,n.count(i)) for i in 
                                              list(("A", "T", "G", "C"))],
                                   pd.DataFrame([(i,j) for i,j in zip(self.names,
                                                     self.sequences)])[1].to_list()))
        return [(i,j) for i,j in zip(self.dataframe_names, self.dataframe_sequences)]
    def motifCorrelation(self,features):
        """_summary_
        if you have limited features to find the correlation
        with the motifs use this function. if you have a large
        number of variables to correlate, please use the 
        motifFeatureDataframe instead
        """
        self.feature = []
        while len(feature) != len(pd.DataFrame([(i,j) for i,j in 
                                  zip(self.names,self.sequences)]))
        text = input("Enter the name of the feature variable:")
        feature.append(text)
        if text == None:
            break
        print(f'the provided features are: {self.feature}')
        self.internal = pd.DataFrame([(i,j) for i,j in 
                                               zip(self.names,self.sequences)])
        self.internal["length"] = pd.DataFrame([(i,j) for i,j in 
                                  zip(self.names,self.sequences)])[1].apply(len)
        self.feature_dataframe = pd.DataFrame(self.feature)
        self.dataframe_plot = pd.concat(self.internal,self.feature_dataframe)
        sns.pairplot(self.dataframe_plot)
        plt.show()
    def motifFeatureDataframe(self, dataframe, sep):
        """_summary_
        Function to plot the length variability of the motifs
        for each sequence with the observed variables. 
        """
        self._csv = input("Enter the path of the csv file containing 
                          the variables you want to correlate with the motifs:") 
        self.motif_dataframe = pd.read_csv(self._csv, header=True, sep = str(self.sep))
        self.combine_dataframe = pd.concat(self.motif.dataframe, self.internal)
        sns.pairplot(self.combine_dataframe)
        plt.show()
    def extractMotifUnique(self, seqID, start, end):
        """_summary_
        if you want to extract a motif from a particular sequence
        """
        self._seq_check = seqID
        self._start = start
        self._end = end 
        self.specific_sequence = [i[1] for i in ([(i, j) for i, j in 
                               zip(self.names, self.sequences)]) if i[0]=="self._seq_check"]
        motif_specific = self.specific_sequence[self._start:self._end]
        return motif_specific
    
    def countMotifPresenceAbsence(self, motif):
        """_summary_
        this function will generate a matrix for the
        presence and absence of the specific matrix
        """
        motif_tags = []
        while True:
            take_motif = input("Enter the name of the motif or motifs 
                                   you want to search in the sequences:")
           motif_tags += take_motif
           if take_motif == None:
               break
           print(f'the entered motifs are {motif_tags}')
        
        sequence_iterations = [(i, j) for i, j in zip(self.names, self.sequences)]
        matrix_count = []
        sequence_matrix_count = []
        sequence_matrix_count.append([sequence_iterations[i], 
                                      sequence_iterations[i][1].count[j] 
                       for i in range(len(sequence_iterations)) for j in matrix_tags])
        matrix_count.append([sequence_iterations[i][1].count[j] 
                             for i in range(len(sequence_iterations)) 
                             for j in matrix_tags])
     def countMotifDataframe(self, tags):
         """_summary_
         This function will count the motifs and outputs the sequence
         and the motif count  as a dataframe. 
         """
         motif_tags = []
         while True:
            tags = input("Enter the name of the motif you want 
                                 to return along with the sequence:")
            motif_tags.append(tags)
            if tags == None:
                break
            print(f'the entered motifs are:{motif_tags}')
            for i in range(len(motif_tags)):
                print(pd.DataFrame([(i,j) for i,j in zip(self.names,self.sequences)])[1]
                  [pd.DataFrame([(i,j) for i,j in zip(self.names,self.sequences)])
                                       [1].str.contains(motif_tags[i])])
     def getMotifsCoordinates(self, motif):
         """_summary_
         Get the start and end coordinates of the motifs
         where the motif occurs in the sequences
         """
         self._motif = str(motif)
         self._motif_sequences = pd.DataFrame([(i,j) for i,j in zip(self.names,self.sequences)])[1]
                           [pd.DataFrame([(i,j) for i,j in zip(self.names,self.sequences)])[1]
                                             .str.contains("self._motif")].tolist()
         self._motif_coordinate_start = []
            for i in range(len(self._motif_sequences)):
                motif_coordinate_start.append(self._motif_sequences[i].find("self._motif"))
         self._motif_coordinate_end = [self._motif_coordinate_start[i]+len("self._motif") 
                                       for i in range(len(self._motif_coordinate_start))]
         print(f'the start and end of the motif in the sequences are: 
                       {[(i,j) for i in zip(self._motif_coordinate_start, 
                                                          self._motif_coordinate_end)]}')


   def vibrioLazyPredictClassification(self,input_path_train, input_path_test, X, y, 
                                          column:str,random_state: int):
        self.input_path_train = input_path_train
        self.train = pd.read_csv(self.input_path_train)
        self.input_path_test = input_path_test
        self.test = pd.read_csv(self.input_path_test)
        self.X = self.train.drop(column, axis=1)
        self.y = self.test[column]
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.random_state = random
        self.X_train, self.X_test, self.y_train, self.y_test =
        train_test_split(self.X, self.y, test_size=.5, random_state=self.random_state)
        estimate = LazyClassifier(
            verbose=0, ignore_warnings=True, custom_metric=None)
        models, predictions = estimate.fit
        self.X_train, self.X_test, self.y_train, self.y_test)
        compare_report = sweetviz.compare(
            [self.X_train, self.X], [self.X_test, self.y])
        compare_report.show_html('self.data.html', open_browser=True)
        compare_report.show_notebook()
        print(f'the_models_evaluated_are:{models}')
        return models

    def vibrioLazyPredictRegression(self,input_path_train, input_path_test, X, y, 
                                          column:str,random_state: int):
        self.X = self.train.drop(column, axis=1)
        self.y = self.test[str(column)]
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.X_train, self.X_test, self.y_train, self.y_test =
        train_test_split(self.X, self.y, test_size=.5, self.random_state=random)
        estimate = LazyRegressor(
            verbose=0, ignore_warnings=True, custom_metric=None)
        models, predictions = estimate.fit(
            self.X_train, self.X_test, self.y_train, self.y_test)
        compare_report = sweetviz.compare(
            [self.X_train, self.X], [self.X_test, self.y])
        compare_report.show_html('self.data.html', open_browser=True)
        compare_report.show_notebook()
        return models
        
    def trainVibrioSequences(self, genetype, gff, gff_out, batch_size):
        self.__genetype = genetype 
        self.__gff = gff
        self.__gff_out = gff_out
        self.__batch_size = batch_size
        with open(self.__gff, "r") as gff:
            with open(self.__gff, "r") as 
            for line in self.__gff.readlines():
                if line.startswith("#"):
                    continue
                else:
                    self.__gff_out.write(line)
                    self.__gff_out.close()
                    self.__gff.close()
        self.__gff_model_selection = pd.read_csv("self.gff_out", sep = "\t")
        self.__genetype = []
        while True:
            self.take_genes = input("Please enter the names of the genes for the model training:")
            self.__genetype.append(self.take_genes)
            if self.take_genes is None:
                break
        self.__batch_size = ""
        while True:
            take_batch = input("Please enter the batch size:")
            self.__batch_size += take_batch
        vibrio_model_generator = Generator(batch_size = int(self.__batch_size), 
                                           fasta_file = "self.fasta", 
                                           annotation_files = ["self.__gff_out"],
                                           annotation_list = [self.__genetype[i] 
                                                              for i in range(len(self.__genetype))])
        vibrio_model = Sequential()
        vibrio.compile(loss = "mse", optimizer = "adam")
        virbio_wrap = ModelWrapper(model = vibrio.compile, 
                                       generator_train = vibrio_model_generator)
        virbio.wrap.train(epochs = 10)
        virbio.evaluate(incl_chromosome = ["chr"])
        virbio.predict(incl_chromosome = ["chr"], chrom_size = "fasta.size")
        vibrio.wrap.save(path = "self.__path", save_model = True)
