library(MASS)
cats
summary(cats)
k<-table(cats$Sex)
barplot(k,main="Number of objects by gender of the cat",xlab ="Sex",ylab="amount",names=c("Female","Male"))
x<-c(cats$Bwt)
y<-c(cats$Hwt)
plot(x,y,xlim = c(2,4),ylim = c(6,21),xlab="Body Weight(kg)",ylab="Heart Weight(g)",main="Heart Weight(g) by Body Weight(kg) of cats",col="red",pch="♡")

