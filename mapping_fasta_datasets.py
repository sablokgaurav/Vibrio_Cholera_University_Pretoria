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