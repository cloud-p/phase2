import sys 
hqlfile=sys.argv[1]
inputdir=sys.argv[2]
outputfile=sys.argv[3]
os.system("source ~/.bashrc")
os.system("/usr/local/hadoop/bin/hadoop dfs -copyFromLocal "+inputdir+" /user/root/")
os.system("/usr/local/hive/bin/hive -f "+hqlfile+ " > " + outputfile)
