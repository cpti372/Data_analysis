escape<-function(n){
  t<-sample(x=1:10,1)
  repeat{
    n<-readline("choose random number:")
    if(t!=n){
      print("Incorrect")
    }
    else{
      print("correct")
      break
    }
  }
}
escape()
