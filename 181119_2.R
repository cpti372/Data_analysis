library(MASS)
Nile
hist(Nile,main="nile",xlab="nile",ylab="Frequency",breaks=10)
survey
summary(MASS$survey)
summary(survey)
k<-table(survey$Smoke)
k
lab<-c("Heavy","Never","Occasionaly","Regularly")
pct<-round(k/sum(k)*100)
lab<-paste(lab,pct)
lab<-paste(lab,"%",sep="")
pie(k,init.angle = 90,label=lab,col=rainbow(length(k)))
