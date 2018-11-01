slibrary(MASS)
str(Cars93)
summary(Cars93)
c<-(Cars93$Price)
c
mean(c)
sum(c)
sort(c)
m<-matrix(nrow = 2,ncol = 2)
m
rownames(m)<-c("smoke","nonsmoke")
colnames(m)<-c("drink","non-drink")
m
m[1,1]<-c(15)
m[1,2]<-c(7)
m[2,1]<-c(5)
m[2,2]<-c(13)
m
m<-rbind(m,c(m[1,1]+m[2,1],m[1,2]+m[2,2]))
m<-cbind(m,c(m[1,1]+m[1,2],m[2,1]+m[2,2],m[3,1]+m[3,2]))
m
rownames(m)<-c("smoke","nonsmoke","sum")
m
colnames(m)<-c("drink","non-drink","sum")
m


