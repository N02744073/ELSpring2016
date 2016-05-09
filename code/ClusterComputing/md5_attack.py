from mpi4py import MPI
from datetime import datetime
startTime=datetime.now()

import hashlib
import sys

hash_to_crack = "6124d98749365e3db2c9e5b27ca04db6"
dict_file = "/home/pi/python_test/dict.txt"
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

def main():
    with open(dict_file) as fileobj:
	fdata = [line.rstrip() for line in fileobj]

        for line in fdata[rank::(rank*size)+1]:
            line = line.strip()
            if hashlib.md5(line).hexdigest() == hash_to_crack:
                print("RANK %s, successfully cracked the hash %s: \nIt's %s") % (rank, hash_to_crack, line)
                print datetime.now()-startTime
		return ""
    print("FAiled to crack the file.")

if __name__ == "__main__":
    main()
