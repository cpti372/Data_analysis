rate<-c(0.37,0.17,0.34,0.42,0.41,0.31,0.71,0.22,0.33)
names(rate)<-c("a","b","c","d","e","f","g","h","i")
rate
//구역 별 침몰되는 배의 수 집계 
ship<-function(list) {
  size<-length(list)
  for(i in 1:size){
    random<-sample(1:100,1)
    if(random/100<= list[i]){
      return (names(list)[i])
    }
  }
  return("Alive")
}
ship(rate)
simul<-function(n,list){
  v<-c()
  for(i in 1:n){
    s<-ship(list)
    if(s!="Alive"){
      v<-c(v,s)
    }
  }
  v
}
result<-simul(1000,rate)
table(result)
