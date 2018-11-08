game<-function(n){
  start<<-0
  bob_score<<-0
  alice_score<<-0
   repeat{
        x<-sample(1:10,1)
        if(x%%2==0) {
          bob_score<<-bob_score+1
        }
        else { 
          alice_score<<-alice_score+1
        }
        start<<-start+1
        if(start==100*n){
          break
        }
  }
}
game(10)
k<-mean(alice_score)
k
