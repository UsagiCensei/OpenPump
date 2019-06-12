# openPump
# An open source file pumper

# Import sys for arguments
import sys

# Import Hashlib for checksum
import hashlib

# Function to generate checksum
def getmd5(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Code if ran through command line
# Arguments, openPump.py [path to file] [pump amount] [-kb/-mb]
if (len(sys.argv) < 4):
    sys.exit("Error: Incorrect Arguments!\nUsage: openPump.py [path to file] [pump amount] [-kb/-mb]")
    
elif (len(sys.argv) == 4):
    filePath = sys.argv[1]
    pumpSize = int(sys.argv[2])
    unitType = sys.argv[3]

    oldMD5 = getmd5(filePath)
    pumpFile = open(filePath, 'ab')

    b_fSize = 0

    if (unitType == "-kb"):
        b_fSize = pumpSize * 1024

    elif (unitType == "-mb"):
        b_fSize = pumpSize * pow(1024, 2)

    else:
        sys.exit("Invalid unit type!")

    buffer = 256
    for i in range(int(b_fSize/buffer)):
        pumpFile.write((b"0" * buffer))

    newMD5 = getmd5(filePath)

    print("File Pumping Completed!")
    print("Original MD5: " + oldMD5)
    print("Pumped MD5: " + newMD5)

    pumpFile.close()

