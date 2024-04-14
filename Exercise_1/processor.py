
import os
import shutil # module that contains file copying, moving etc.

# Define the directories
addedDir = "deployPackage/added"
removedDir = "deployPackage/removed"
fileDiffName = "file_diff.txt"

# Check if those directories exists, if not create a new one
# added dir
if not os.path.exists(addedDir):
    os.makedirs(addedDir)
# removed dir
if not os.path.exists(removedDir):
    os.makedirs(removedDir)

# Check if the file_diff.txt exists
if not os.path.exists(fileDiffName):
    print(f"{fileDiffName} does not found. Make sure this file is exists to proceed with processing.")

else:
    # Open the file_diff.txt to read the content
    with open(fileDiffName, "r") as file:
        # Read the file line by line
        for line in file:
            status, filePath = line.strip().split(maxsplit=1)

            # Extract filename
            fileName = filePath.split("/")[-1]

            # Check the status if equal to M (modify) or A (add)
            if status == "M" or status == "A":
                if os.path.exists(filePath):
                    # Copy the file to the added dir
                    destinationPath = os.path.join(addedDir, fileName)
                    shutil.copy(filePath, destinationPath)
                else:
                    print(f"File '{filePath}' not found.")
            
            # Check the status if equal to R (remove) or D (delete)
            if status == "R" or status == "D":
                if os.path.exists(filePath):
                    # Move the file to the removed dir
                    destinationPath = os.path.join(removedDir, fileName)
                    shutil.move(filePath, destinationPath)
                else:
                    print(f"File '{filePath}' not found.")
            
            # Write to added.txt for files with status M (modify) and A (add)
            if status == "M" or status == "A":
                with open("added.txt", "a") as addedFile:
                    addedFile.write(fileName + "\n")

            # Write to removed.txt for files with status R (rename) and D (delete)
            elif status == "R" or status == "D":
                with open("removed.txt", "a") as removedFile:
                    removedFile.write(fileName + "\n")