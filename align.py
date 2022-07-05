#!/usr/bin/python
import sys,os
from timeit import default_timer as timer

# Control variables
##############################################

#bwa aln -t 1 /hg19/hg19bwaidx myread.fa > myread.sai
#bwa samse -n 10  /hg19/hg19bwaidx myread.sai myread.fa > myread.sam


dbpath = "/data/BDP1_2022/hg19/"
dbname = "hg19bwaidx"

queryname = sys.argv[1]+".fa" 

out_name = sys.argv[1]

md5file = "md5.txt"

command="mkdir output"
os.system(command)

command = "./bwa aln -t 1 " + dbpath + dbname + " " + queryname + " > " + "output/"+ out_name + ".sai"
print "launching command: " , command
os.system(command)

#Removing samse command
#command = "./bwa samse -n 10 " + dbpath + dbname + " " + out_name + ".sai " + queryname + " > " + out_name + ".sam"
#print "launching command: " , command
#os.system(command)

print "Creating md5sums"
os.system("md5sum " + "output/" + out_name + ".sai " + " > " + "output/" + "md5_" + out_name + ".txt")
#os.system("md5sum " + out_name + ".sam " + " >> " + md5file)  #avoiding the run for .sam files

#removing gzip part
#print "gzipping out text file"
#command = "gzip " + out_name + ".sai" #updated to export .sai instead of .sam
#print "launching command: " , command
#os.system(command)

print "exiting"

exit(0)
