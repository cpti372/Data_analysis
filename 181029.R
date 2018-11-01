library(MASS)
str(Insurance)
summary(Insurance)
s2<-sapply(Insurance$Holders, function(x){x<500})
class(s2)
head(s2)
check<-s2
Holders<-Insurance$Holders
sample<-data.frame(Holders,check)
sample
merge(Insurance,sample)
tapply(Insurance$Claims,Insurance$Age,sum)
