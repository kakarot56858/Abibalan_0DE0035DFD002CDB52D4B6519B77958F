class Player():
  def play():
    print("The player is playing")
    
class Batsman(Player):
  def play(self):
    print("The batsman is batting")
    
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")
    
Bat=Batsman()
Bowl=Bowler()
Player.play()
Bat.play()
Bowl.play()
