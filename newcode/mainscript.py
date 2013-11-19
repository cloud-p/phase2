import os
number=sys.argv[1]
inputfile=sys.argv[2]
outputfile=sys.argv[3]
classtobeused=sys.argv[4]
jarorhqlfile=sys.argv[5]
os.system("python main.py "+ number +" 2 6")
os.system("./main.sh pp")
if classtobeused==" ":
	os.system("python runhive.py "+jarorhqlfile+" "+inputfile+" " +outputfile)
else:
	os.system("python runmapreduce.py "+jarorhqlfile +" "+ inputfile+" " +outputfile+" " +classtobeused)
