product<-function(){
  fault<-3
  random<-sample(1:100,1)
  if(random<fault){
    return("Fail") 
  }
  else{
    return("Success")
  }
}
product()
product_line<-function(){
  fault<-0
  for(i in 1:100) {
    result<-product()
    if(result == "Fail") {
      fault<- fault +1
    }
  }
  return (fault)
}
product_line()
factory<- function(n) {
  total_fault<-0
  for(i in 1:n) {
    total_fault<-total_fault+product_line()
  }
  return(total_fault/n)
}

factory(1000)