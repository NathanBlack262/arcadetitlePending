from turtle import *
from time import *
import math
from random import *
import gc


TARGET_FPS = 30
PLAYER_SPEED = 15



class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(0,-200)
        self.shape("classic")
        self.positionListCount = 0
        self.positionList = ["right", "up", "left", "down"]
        self.turnLeft()
        self.alive = True
        self.score = 0
        self.bulletsMAX = 5
        self.enemiesMAX = 3
        self.currentKilled = 0
        self.bullets = []
        self.enemies = []
        self.enemybullets = []
        
    def position(self):
        x = round(self.xcor())
        y = round(self.ycor())
        return (x,y)
    
    def turnLeft(self):
        self.lt(90)
        self.positionListCount = (self.positionListCount + 1) % 4
        if self.positionListCount == 0:
            self.shape("playerright.gif")
        if self.positionListCount == 1:
            self.shape("playerup.gif")
        if self.positionListCount == 2:
            self.shape("playerleft.gif")
        if self.positionListCount == 3:
            self.shape("playerdown.gif")
            
            
    def turnRight(self):
        if self.alive:
            self.rt(90)
            if self.positionListCount >= 1:
                self.positionListCount = (self.positionListCount - 1) % 4
            else:
                self.positionListCount = 3
            if self.positionListCount == 0:
                self.shape("playerright.gif")
            elif self.positionListCount == 1:
                self.shape("playerup.gif")
            elif self.positionListCount == 2:
                self.shape("playerleft.gif")
            elif self.positionListCount == 3:
                self.shape("playerdown.gif")
            
    def moveLeft(self):
        if self.alive:
            if self.positionList[self.positionListCount] == "right":
                self.backward(PLAYER_SPEED)
            elif self.positionList[self.positionListCount] == "left":
                self.forward(PLAYER_SPEED)
            elif self.positionList[self.positionListCount] == "up":
                self.lt(90)
                self.forward(PLAYER_SPEED)
                self.rt(90)
            else:
                self.rt(90)
                self.forward(PLAYER_SPEED)
                self.lt(90)
        if self.position()[0] < -400:
            self.alive = False
        
    def moveRight(self):
        if self.alive:
            if self.positionList[self.positionListCount] == "right":
                self.forward(PLAYER_SPEED)
            elif self.positionList[self.positionListCount] == "left":
                self.backward(PLAYER_SPEED)
            elif self.positionList[self.positionListCount] == "up":
                self.rt(90)
                self.forward(PLAYER_SPEED)
                self.lt(90)
            else:
                self.lt(90)
                self.forward(PLAYER_SPEED)
                self.rt(90)
        if self.position()[0] > 400:
            self.alive = False
            
    def moveUp(self):
        if self.alive:
            if self.positionList[self.positionListCount] == "right":
                self.lt(90)
                self.forward(PLAYER_SPEED)
                self.rt(90)
            elif self.positionList[self.positionListCount] == "left":
                self.rt(90)
                self.forward(PLAYER_SPEED)
                self.lt(90)
            elif self.positionList[self.positionListCount] == "up":
                self.forward(PLAYER_SPEED)
            else:
                self.backward(PLAYER_SPEED)
        if self.position()[1] > 300:
            self.alive = False
            
    def moveDown(self):
        if self.alive:
            if self.positionList[self.positionListCount] == "right":
                self.rt(90)
                self.forward(PLAYER_SPEED)
                self.lt(90)
            elif self.positionList[self.positionListCount] == "left":
                self.lt(90)
                self.forward(PLAYER_SPEED)
                self.rt(90)
            elif self.positionList[self.positionListCount] == "up":
                self.backward(PLAYER_SPEED)
            else:
                self.forward(PLAYER_SPEED)
        if self.position()[1] < -300:
            self.alive = False
                    
    def shoot(self):
        if len(self.bullets) < self.bulletsMAX:
            matthias = Bullet(self.positionList[self.positionListCount])
            matthias.color("yellow")
            matthias.penup()
            position = self.position()
            if self.positionList[self.positionListCount] == "up":
                matthias.goto(position[0], position[1] + 25)
            elif self.positionList[self.positionListCount] == "down":
                matthias.goto(position[0], position[1] - 25)
            elif self.positionList[self.positionListCount] == "left":
                matthias.goto(position[0] - 20, position[1])
            elif self.positionList[self.positionListCount] == "right":
                matthias.goto(position[0] + 20, position[1])
            matthias.pd()
            matthias.dot(5)
            matthias.pu()
            matthias.ht()
            self.bullets.append(matthias)
                
            
        
class Bullet(Turtle):
    def __init__(self, facing):
        super().__init__()
        self.lifeSpan = 13
        self.life = 0
        self.alive = True
        if facing == None:
            facing = "right"
        else:
            self.facing = facing
        if facing == "up":
            self.lt(90)
        if facing == "left":
            self.lt(180)
        if facing == "down":
            self.rt(90)
        
    def fadeOut(self):
        self.clear()
        self.ht()
        self.pu()
        self.goto(300,300)
        del self
        
    def changeAllignment(self, facing):
        if facing == None:
            facing = "right"
        else:
            self.facing = facing
        if facing == "up":
            self.lt(90)
        if facing == "left":
            self.lt(180)
        if facing == "down":
            self.rt(90)
    
            
    def fire(self):
        self.clear()
        self.pu()
        self.forward(PLAYER_SPEED)
        self.pd()
        self.dot(5)
        
        
class GenericEnemy(SpaceShip):
    def __init__(self):
        super().__init__()
        self.bulletsMAX = 1
        self.herobullets = []
        xgoto = randint(-200,200)
        ygoto = randint(150,200)
        self.goto(xgoto, ygoto)
        self.shape("genericEnemyup.gif")
        
    def position(self):
        x = round(self.xcor())
        y = round(self.ycor())
        return (x,y)
    
    def turnLeft(self):
        self.lt(90)
        self.positionListCount = (self.positionListCount + 1) % 4
        if self.positionListCount == 0:
            self.shape("genericEnemyright.gif")
        if self.positionListCount == 1:
            self.shape("genericEnemyup.gif")
        if self.positionListCount == 2:
            self.shape("genericEnemyleft.gif")
        if self.positionListCount == 3:
            self.shape("genericEnemydown.gif")
            
    def turnRight(self):
        self.rt(90)
        if self.positionListCount >= 1:
            self.positionListCount = (self.positionListCount - 1) % 4
        else:
            self.positionListCount = 3
        if self.positionListCount == 0:
            self.shape("genericEnemyright.gif")
        if self.positionListCount == 1:
            self.shape("genericEnemyup.gif")
        if self.positionListCount == 2:
            self.shape("genericEnemyleft.gif")
        if self.positionListCount == 3:
            self.shape("genericEnemydown.gif")
            
    def moveUp(self):
        matthias = Turtle()
        del matthias
        
        
    def shoot(self):
        if len(self.bullets) < self.bulletsMAX:
            matthias = Bullet(self.positionList[self.positionListCount])
            matthias.color("yellow")
            matthias.penup()
            position = self.position()
            if self.positionList[self.positionListCount] == "up":
                matthias.goto(position[0], position[1] + 25)
            elif self.positionList[self.positionListCount] == "down":
                matthias.goto(position[0], position[1] - 25)
            elif self.positionList[self.positionListCount] == "left":
                matthias.goto(position[0] - 20, position[1])
            elif self.positionList[self.positionListCount] == "right":
                matthias.goto(position[0] + 20, position[1])
            matthias.pd()
            matthias.dot(5)
            matthias.pu()
            matthias.ht()
            self.bullets.append(matthias)
        
                
    def perish(self):
        self.clear()
        self.ht()
        self.pu()
        self.goto(300,300)
        del self
        
        
        
    

class Application:
    def __init__(self):
        spicyBoi = Screen()
        self.window = spicyBoi
        self.window.tracer(0,0)
        self.window.title("<Title Pending>")
        self.window.addshape("playerright.gif")
        self.window.addshape("playerup.gif")
        self.window.addshape("playerleft.gif")
        self.window.addshape("playerdown.gif")
        self.window.addshape("genericEnemyright.gif")
        self.window.addshape("genericEnemyup.gif")
        self.window.addshape("genericEnemyleft.gif")
        self.window.addshape("genericEnemydown.gif")
        self.window.bgcolor("black")
        self.window.update()
        self.window.bgpic("landscape1.png")
        self.window.update()
        self.introMode = True
        self.play = False
        self.quit = False
        self.moveTime = 10
        self.moveTimeCounter = 0
        self.tryAgainMode = False
        self.tryAgain = False
        self.currentKilled = 0
        self.player = SpaceShip()
        self.draw_walls()
        self.createSideBars()
        self.window.update()
        
    def startUp(self):
        self.window.clear()
        self.window.tracer(0,0)
        self.window.bgcolor("black")
        matthias = Turtle()
        matthias.ht()
        matthias.pencolor("orange")
        matthias.pu()
        matthias.goto(0,200)
        matthias.write("Title", True, align = "center", font =("BankGothic MD BT",75,"bold"))
        matthias.write
        matthias.goto(0,100)
        matthias.write("Pending", True, align = "center", font =("BankGothic MD BT",75,"bold"))
        matthias.write
        self.window.update()
        sleep(1)
        matthias.goto(0,50)
        matthias.pencolor("red")
        matthias.write("Press Enter to Play", True, align = "center", font =("BankGothic MD BT",25,"bold"))
        sleep(1)
        matthias.goto(0,0)
        matthias.write("Press X to Exit", True, align = "center", font =("BankGothic MD BT",25,"bold"))
        self.window.onkey(lambda : self.playToggle(), "p")
        t1 = time()
        t2 = time()
        while True:
            elapsed = t2 - t1
            if elapsed >= TARGET_FPS:
                t1 = t2
                if self.play == True:
                    self.window.clear()
                    self.window.bgcolor("black")
                    self.window.bgpic("landscape1.png")
                    self.newGame()
                    return
            t2 = time()
                    
    def playToggle(self):
        print("eyy")
        self.play = True
                    
    
    def draw_walls(self):
        matthias = Turtle()
        matthias.ht()
        matthias.pencolor("white")
        matthias.pu()
        matthias.goto(-400,-300)
        matthias.pd()
        for i in range(2):
            matthias.fd(800)
            matthias.lt(90)
            matthias.fd(600)
            matthias.lt(90)
        del matthias
        
    def createSideBars(self):
        matthias = Turtle()
        matthias.ht()
        matthias.pencolor("red")
        matthias.pu()
        matthias.goto(580,175)
        matthias.write("Score: " + str(self.player.score), True, align = "center", font =("BankGothic MD BT",22,"bold"))
        matthias.goto(500,-20)
        matthias.pencolor("orange")
        matthias.pd()
        del matthias
        
    def updateScore(self):
        matthias = Turtle()
        matthias.ht()
        matthias.pu()
        matthias.goto(425,215)
        matthias.pd()
        matthias.fillcolor('black')
        matthias.begin_fill()
        for i in range(2):
            matthias.fd(400)
            matthias.rt(90)
            matthias.fd(100)
            matthias.rt(90)
        matthias.end_fill()
        matthias.pu()
        matthias.pencolor("red")
        matthias.goto(580,175)
        matthias.write("Score: " + str(self.player.score), True, align = "center", font =("BankGothic MD BT",22,"bold"))
        del matthias
                
            
    def check_players(self):
        for enemy in self.player.enemies:
            for bullet in enemy.bullets:
                if bullet.position()[0] + 15 >= self.player.position()[0] and bullet.position()[0] - 15 <= self.player.position()[0] and bullet.position()[1] + 15 >= self.player.position()[1] and bullet.position()[1] - 15 <= self.player.position()[1]:
                    self.player.alive = False
        for bullet in self.player.bullets:
            for enemy in self.player.enemies:
                if bullet.position()[0] + 15 >= enemy.position()[0] and bullet.position()[0] - 15 <= enemy.position()[0] and bullet.position()[1] + 15 >= enemy.position()[1] and bullet.position()[1] - 15 <= enemy.position()[1]:
                    enemy.alive = False
                    self.player.score += 100
        for enemy in self.player.enemies:
            if self.player.position()[0] + 15 >= enemy.position()[0] and self.player.position()[0] - 15 <= enemy.position()[0] and self.player.position()[1] + 15 >= enemy.position()[1] and self.player.position()[1] - 15 <= enemy.position()[1]:
                self.player.alive = False
                    
    def explode(self, character):
        for i in range(2):
            for bullet in character.bullets:
                bullet.clear()
                del bullet
        character.hideturtle()
                    
    def eliminateSprites(self):
        for enemy in self.player.enemies:
            if enemy.alive == False:
                self.explode(enemy)
                self.player.enemies.remove(enemy)
                enemy.perish()
                self.player.currentKilled += 1
        if self.player.alive == False:
            self.explode(self.player)
        
                
                
    def bulletsCheck(self):
        for bullet in self.player.bullets:
            if bullet.life >= bullet.lifeSpan:
                bullet.fadeOut()
                self.player.bullets.remove(bullet)
            else:
                bullet.fire()
                bullet.life += 1
        for enemy in self.player.enemies:
            for bullet in enemy.bullets:
                if bullet.life >= bullet.lifeSpan:
                    bullet.fadeOut()
                    enemy.bullets.remove(bullet)
                else:
                    bullet.fire()
                    bullet.life += 1
                
    def gameOverTryAgain(self):
        timer = 15
        self.window.clear()
        self.window.onkey(lambda : self.restart(), "r")
        self.tryAgainMode = True
        self.window.bgcolor("black")
        matthias = Turtle()
        matthias.ht()
        matthias.pu()
        matthias.goto(0,250)
        matthias.pencolor("red")
        matthias.write("Game Over.", True, align = "center", font =("BankGothic MD BT",50,"bold"))
        sleep(1)
        matthias.goto(0,175)
        matthias.write("Play Again?", True, align = "center", font =("BankGothic MD BT",40,"normal"))
        sleep(.5)
        matthias.goto(0,150)
        matthias.write("(Press R To Restart)", True, align = "center", font =("BankGothic MD BT",20,"normal"))
        sleep(.5)
        del matthias
        michael = Turtle()
        michael.ht()
        michael.pu()
        michael.goto(0,0)
        michael.pencolor("red")
        michael.write(str(timer), True, align = "center", font =("BankGothic MD BT",60,"normal"))
        t1 = time()
        t2 = time()
        while timer > 0:
            elapsed = t2 - t1
            if elapsed >= 1:
                t1 = t2
                timer -= 1
                michael.clear()
                michael.goto(0,0)
                michael.write(str(timer), True, align = "center", font =("BankGothic MD BT",60,"normal"))
                if self.tryAgain == True:
                    self.tryAgainMode = False
                    return True
            t2 = time()
        return False
                
    def restart(self):
        if self.tryAgainMode == True:
            self.tryAgain = True
                
        
        
        
    def facePlayer(self, enemy):
        if self.player.position()[1] < enemy.position()[1] - 25:
            if enemy.positionList[enemy.positionListCount] == "up":
                for i in range(2):
                    enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "right":
                enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "left":
                enemy.turnLeft()
        elif self.player.position()[1] > enemy.position()[1] + 25:
            if enemy.positionList[enemy.positionListCount] == "down":
                for i in range(2):
                    enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "left":
                enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "right":
                enemy.turnLeft()
        elif self.player.position()[0] > enemy.position()[0] + 25:
            if enemy.positionList[enemy.positionListCount] == "left":
                for i in range(2):
                    enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "up":
                enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "down":
                enemy.turnLeft()
        elif self.player.position()[0] < enemy.position()[0] - 25:
            if enemy.positionList[enemy.positionListCount] == "right":
                for i in range(2):
                    enemy.turnRight()
            elif enemy.positionList[enemy.positionListCount] == "up":
                enemy.turnLeft()
            elif enemy.positionList[enemy.positionListCount] == "down":
                enemy.turnRight()         
        
    def enemyCalibrateShoot(self):
        for enemy in self.player.enemies:
            if self.player.position()[0] > enemy.position()[0] + 25:
                ey = randint(1,13)
                if ey == 1:
                    self.facePlayer(enemy)
                    enemy.moveRight()
            if self.player.position()[0] < enemy.position()[0] - 25:
                ey = randint(1,13)
                if ey == 1:
                    self.facePlayer(enemy)
                    enemy.moveLeft()
            if self.player.position()[1] < enemy.position()[1] - 25:
                ey = randint(1,13)
                if ey == 1:
                    self.facePlayer(enemy)
                    enemy.moveDown()
            if self.player.position()[1] > enemy.position()[1] + 25:
                ey = randint(1,13)
                if ey == 1:
                    self.facePlayer(enemy)
                    enemy.moveUp()
            eyy = randint(1,30)
            if eyy == 1:
                enemy.shoot()
                
    def newGame(self):
        self.window.clear()
        self.window.tracer(0,0)
        self.currentKilled = 0
        self.player = SpaceShip()
        self.window.bgcolor("black")
        self.window.bgpic("landscape1.png")
        self.moveTimeCounter = 0
        self.tryAgainMode = False
        self.tryAgain = False
        self.draw_walls()
        self.createSideBars()
        self.window.update()
        
        
                                 
    def run(self):
        self.play = True
        if self.play == False:
            self.startUp()
        self.window.onkey(lambda : self.player.turnLeft(), "a")
        self.window.onkey(lambda : self.player.turnRight(), "d")
        self.window.onkeypress(lambda : self.player.moveRight(), "Right")
        self.window.onkeypress(lambda : self.player.moveLeft(), "Left")
        self.window.onkeypress(lambda : self.player.moveUp(), "Up")
        self.window.onkeypress(lambda : self.player.moveDown(), "Down")
        self.window.onkey(lambda : self.player.shoot(), "space")
        self.window.listen()
        t1 = time()
        t2 = time()
        while True:
            self.window.onkey(lambda : self.player.turnLeft(), "a")
            self.window.onkey(lambda : self.player.turnRight(), "d")
            self.window.onkeypress(lambda : self.player.moveRight(), "Right")
            self.window.onkeypress(lambda : self.player.moveLeft(), "Left")
            self.window.onkeypress(lambda : self.player.moveUp(), "Up")
            self.window.onkeypress(lambda : self.player.moveDown(), "Down")
            self.window.onkey(lambda : self.player.shoot(), "space")
            self.window.onkey(lambda : self.restart(), "r")
            self.window.listen()
            gc.collect()
            elapsed = t2 - t1
            if elapsed > 1 / TARGET_FPS:
                t1 = t2
                self.bulletsCheck()
                self.check_players()
                self.eliminateSprites()
                self.updateScore()
                if self.player.alive == False:
                    del self.player
                    if self.gameOverTryAgain() == False:
                        self.play = False
                        self.startUp()
                    else:
                        self.newGame()
                self.moveTimeCounter = (self.moveTimeCounter + 1) % self.moveTime
                if self.moveTimeCounter == 0: 
                    for enemy in self.player.enemies:
                        enemy.moveDown()
                        if enemy.position()[0] <= -300:
                            self.player.enemies.remove(enemy)
                            del enemy
                self.enemyCalibrateShoot()
                if self.player.score % 1500 == 0 and self.player.currentKilled != self.currentKilled:
                    self.player.enemiesMAX += 1
                    self.currentKilled = self.player.currentKilled
                if len(self.player.enemies) < self.player.enemiesMAX:
                    randomenemyValue = randint(1,30)
                    if randomenemyValue == 1:
                        self.bob = GenericEnemy()
                        self.player.enemies.append(self.bob)
                self.window.update()
            t2 = time()
        
        
def main():
    eyy = Application()
    eyy.run()
    
if __name__ == "__main__":
    main()