import sys 
jarfile=sys.argv[1]
inputfile=sys.argv[2]
outputfile=sys.argv[3]
classtobeused=sys.argv[4]
os.system("/usr/local/hadoop/bin/hadoop dfs -copyFromLocal "+inputfile+" /user/root/")
os.system("/usr/local/hadoop/bin/hadoop dfs -rmr /user/root/out2")
os.system("/usr/local/hadoop/bin/hadoop jar "+ jarfile +" "+ classtobeused + " /user/root/"+inputfile.split("/")[-1]+" /user/root/out2")
os.system("/usr/local/hadoop/bin/hadoop dfs -cat /user/root/out2/part* > "+ outputfile)
