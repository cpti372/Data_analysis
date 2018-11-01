DF<-read.csv('week8.csv')
DF
tapply(DF$Effect,DF$Medicine,mean)
tapply(DF$Problem,DF$Medicine,mean)
DF2<-tapply(DF$Problem,DF$Medicine,mean)
sort(DF2,decreasing = T)
DF3<-data.frame(Medicine=c("A","B","C"),Effect_prob=c(0.566,0.274,0.390),Problem_prob=c(0.454,0.396,0.286))
DF3
DF4<-c(0.112,-0.396,0.104)
DF5<-cbind(DF3,DF4)
DF5
