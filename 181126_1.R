k<-1-pbinom(q=2,size=10,prob=0.4,lower.tail = TRUE)
k
dpois(x=3,lambda = 6/4)
p<-0.001
while(1){  
  q<-pbinom(15,size=100,p,lower.tail = TRUE)
  if(q < 0.2)break
  p<-p+0.001
}
print(p)



