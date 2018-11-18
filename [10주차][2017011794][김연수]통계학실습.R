cnt<<-1
win<<-0
alice<<-6000
bob<<-4000
trial<-function() {
    dice<-sample(1:6,1)
    if (cnt%% 5!= 0 && dice >= 5) {
      alice<<-alice+100
      bob<<-bob-100
      cnt<<-cnt+1
    }
    
    if (cnt%%5!=0 && dice<=4) {
      bob<<-bob+100
      alice<<-alice-100
      cnt<<-cnt+1
    }
    if (cnt%%5==0 && dice>=5) {
      alice<<-alice+300
      bob<<-bob-300
      cnt<<-cnt+1
    }
    
    if (cnt%%5==0 && dice<=4) {
      alice<<-alice-300
      bob<<-bob+300
      cnt<<-cnt+1
    }
}

ingame<-function(){
  while(alice>0 && bob>0){
    trial()
  }
  if(alice > bob){
    win<<-win+1
  }
}

startGame<-function(n){
  for(i in 1:n){
    ingame()
  }
  prob=win/n
  cat("alice가 이길 확률:",prob);
}

startGame(5000)
