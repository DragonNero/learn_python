reprev<-read.delim("dataset_3_2.txt",header=FALSE)
reprev<-as.character(reprev)
gl<-nchar(reprev)
splitted<-strsplit(reprev, "")[[1]] #split into individual character
for(i in 1:gl) #To Replace the sequence
{
if (splitted[i]=="A")
{splitted[i]="T"}
else if (splitted[i]=="T")
{splitted[i]="A"}
else if (splitted[i]=="G")
{splitted[i]="C"}
else {splitted[i]="G"}
}
reverse<-rev(splitted)
final<-paste(reverse,sep="",collapse="")
fix(final)
