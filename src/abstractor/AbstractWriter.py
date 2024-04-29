"""
This class is responsible for taking a ready abstract and writing it to the appropriate output file.
1. The output directory is defined in the configuration file
2. The output file path is defined as the function input
3. This class has only 1 method
"""

class AbstractWriter():
    def __init__(self,config_path:str = "config.json"):
        with open(config_path,"r") as f:
            config = json.load(f)
            basicConfig(level=config["log_level"])
            debug("Initializing AbstractWriter")
            self.output_dir = config["output_dir"]
            self.output_file = None
            self.output_file_path = None
        debug("Output directory: %s",self.output_dir)
        info("AbstractWriter initialized successfully \n\n")
    def write(self,abstract:str):
        """
        Writes the abstract to the output file
        """
        info("Writing abstract to output file")
        debug("Writing abstract to file: %s",self.output_file_path)
        with open(self.output_file_path,"w") as f:
            f.write(abstract)
        info("Abstract written successfully \n\n")
    def set_output_file(self,output_file:str):
        """
        Sets the output file path
        """
        self.output_file = output_file
        self.output_file_path = path.join(self.output_dir,self.output_file)
        debug("Output file set to: %s",self.output_file_path)