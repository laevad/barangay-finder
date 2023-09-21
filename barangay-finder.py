import os

class BarangayFinder:
    # constructor
    def __init__(self):
        pass

    # open directory
    def open(self, path):
     
        self.files = []
        
        for file in os.listdir(path):
            if file.endswith(".json"):
                self.files.append(file)
                print(file)


    
    def openFile(self, path):
        
        self.findText = []
        
        self.files = []
        
        for file in os.listdir(path):
            if file.endswith(".json"):
                self.files.append(file)
                print(file)
                
                f = open(path + "/" + file, "r")
                
                for line in f:
                    
                    if "ADM1_EN" in line:
                        
                        if "REGION X (NORTHERN MINDANAO)" in line:
                            # print that line of text
                            print(line)
                            
                            if line[-2] != ",":
                                line = line[:-1] + ",\n"
                            
                            self.findText.append(line)
                # close file
                f.close()
                # create a new file
                f = open("cluster_3.txt", "w")
                # write all find text
                f.writelines(self.findText)
                # close file
                f.close()

    # example 1
    def openFile1(self, path):
        
        self.findText = []
        
        self.files = []
        
        for file in os.listdir(path):
            if file.endswith(".json"):
                self.files.append(file)
                print(file)
                
                f = open(path + "/" + file, "r")
                
                for line in f:
                    
                    if "ADM2_EN" in line:
                        
                        if "MISAMIS ORIENTAL" in line:
                            # print that line of text
                            print(line)
                            
                            if line[-2] != ",":
                                line = line[:-1] + ",\n"
                            
                            self.findText.append(line)
                # close file
                f.close()
                # create a new file
                f = open("misamis_oriental.txt", "w")
                # write all find text
                f.writelines(self.findText)
                # close file
                f.close()

    # example 2
    def openFile2(self, path):
        
        self.findText = []
        
        self.files = []
        
        for file in os.listdir(path):
            if file.endswith(".json"):
                self.files.append(file)
                print(file)
                
                f = open(path + "/" + file, "r")
                
                for line in f:
                    
                    if "ADM3_EN" in line:
                        
                        if "CAGAYAN DE ORO CITY (Capital)" in line:
                            # print that line of text
                            print(line)
                            
                            if line[-2] != ",":
                                line = line[:-1] + ",\n"
                            
                            self.findText.append(line)
                # close file
                f.close()
                # create a new file
                f = open("CAGAYAN DE ORO CITY (Capital).txt", "w")
                # write all find text
                f.writelines(self.findText)
                # close file
                f.close()
# main
if __name__ == '__main__':
    # create object
    barangayFinder = BarangayFinder()
    
    barangayFinder.openFile2("YOUR PATH")
