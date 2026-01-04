import os
import logging 

# Logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log")


# Global Variables 
ALLOWED_EXT = ["txt", "md", "py", "ts", "js"]
IGNORED_FILES = ["app.log", "main.py"]

BASE_DIR = os.getcwd()
  

# Classes
class Operations: 
    def __init__(self):
        pass
    
    def read(file: str) -> str: 
        with open(file) as f:
            long_description = f.read()
            return long_description


class Movement: 
    def __init__(self):
        pass

    def forwardDirectory(dirName: str):
        os.chdir(dirName)
        print(f"Current Directory: {dirName}")

    def backDirectory(): 
        os.chdir("..")

operations = Operations
movement = Movement

def main(directory: str): 
    for file in directory: 
        try: 
            if file in IGNORED_FILES:
                pass
            else: 
                if ".txt" in file:
                    output = operations.read(file)
                    print(output)

                else:
                    logger.error(f"Error this is not a file proceed in: {file}")
                    
                    movement.forwardDirectory(file)

                    for file2 in os.listdir(): 
                        if ".txt" in file2:
                            output = operations.read(file2)
                            print(output)
                        else: 
                            movement.forwardDirectory(file2)
                            for file3 in os.listdir():
                                output = operations.read(file3)
                                print(output)
                            movement.backDirectory()

                    movement.backDirectory()    

        except TypeError as error: 
            logger.error(f"There is some error : {error}")
            break
 
       

main(os.listdir())


 