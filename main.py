import os
import logging 

# Logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log")

# Global Variables 
ALLOWED_EXT = (".txt", ".md", ".py", ".ts", ".js")
IGNORED_FILES = ["app.log", "main.py", ".gitignore", ".git"]

   

# Classes
class Operations: 
    def read(file: str) -> str: 
        with open(file) as f:
            long_description = f.read()
            return long_description


class Movement: 
    def forwardDirectory(dirName: str):
        os.chdir(dirName)

    def backDirectory(): 
        os.chdir("..")

operations = Operations
movement = Movement


def is_allowed(file: str) -> bool:
    return file.lower().endswith(ALLOWED_EXT)

line: int = 1
def main(directory: str, line: int): 

    for file in directory: 
        try: 
            if file in IGNORED_FILES:
                pass
            else: 
                if is_allowed(file):
                    # File Scanning 
                    output = operations.read(file)
                    print(line, output.split("\n"))
                    line = line + len(output.split("\n")) 

                else:
                    logger.error(f"Error this is not a file proceed in: {file}")
                    movement.forwardDirectory(file)
                    main(os.listdir(), line)
                    movement.backDirectory()

        except TypeError as error: 
            logger.error(f"Internal Error: {error}")
            break

    return line

total = main(os.listdir(), line)
print("total line: ", total)
