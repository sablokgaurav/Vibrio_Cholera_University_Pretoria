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
