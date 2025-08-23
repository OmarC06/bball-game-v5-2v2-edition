from random import randint

#### half court is 47 ft away
#### court is 50 wide
#lets make (0,0) the center of the hoopv 
spots = [
  "Deep Center", #0
  "Deep Right Wing", #1
  "Deep Left Wing", #2


  "Top 3", #3
  "Right Wing 3", #4
  "Left Wing 3", #5
  
  "Right Corner 3", #6
  "Left Corner 3", #7


  "Top Mid", #8
  "Right Wing Mid", #9
  "Left Wing Mid", #10
  
  "Right Corner Mid", #11
  "Left Corner Mid", #12


  "Top Paint", #13
  "Right Paint", #14
  "Left Paint", #15
]


class Player:    
    def __init__(self, name, playerType):
        self.name, self.playerType = name, playerType #will not affect shooting ratings
        
        self.recentActions = []
        
        self.points = 0
        self.rebounds = 0
        self.steals = 0
        self.blocks = 0
        self.turnovers = 0
        
        self.holdingBall = False
        self.guardingBall = False #the defender on the one holding the ball
        
        self.ankleBroken = False
        
        self.onOffense = False
        self.onDefense = False
        
        if name == "ONE":
            self.location = spots[0]
        elif name == "TWO":
            self.location = spots[randint(4, 5)]
    
        
        match self.playerType:
            
            case "Guard": #better dribbling, shorter, 
                self.basicRatings = {
                    # "staminaBonus" : randint(0, 25),   # higher means more energy per game or possession? what if you run out, you die? lmao.
                                                    # or maybe it determines how much energy is used per action and everyone starts out at 0 used.
                                                    # the more you use, the worse your ratings get. but maybe you cant run out? all players just thug it out. 
                                                    # used to prevent spamming dribbling (could also make chance to just drop ball).
                                                    # number could be a percentage of how much less energy is used to do an action. call it staminaBonus instead?
                    "Stamina" : randint(0,100), # how much the rest of the ratings go down as you use more energy points. (idk what the number will mean yet)
                    "Height" : randint(65, 77), #number represents inches. helps shoot over players, on rebounds, and throwing and catching passes.
                    # "Strength" : randint(45, 55), #number has to be arbitrary ig. not sure if i want to include this
                    # "Hustle" : randint(45, 55), #same with this as strength
                    
                    "Open" : randint(45, 55),
                    "Contested" : randint(45, 55),
                    
                    "StandStill Shot" : randint(45, 55), #catch and shoot, right off pass or at the start of the possession i guess
                    "Moving Shot" : randint(45, 55), #after dribble moves
                    
                    "Draw Foul" : randint(45, 55), #higher = better at drawing fouls
                    "Foul" : randint(45, 55), #higher = more likely to foul someone (worse)
                    "Ball Security" : randint(45, 55), #protect against getting stripped
                    # "Heatablility" : randint(45, 55), #how easy to heat up? idek if i want this to be a thing
                    
                    "Interior D" : randint(45, 55), #cutting off drives and cuts after screens
                    "Perimeter D" : randint(45, 55), #prevent ankle breakers and get through screens or switch
                    
                    "Rebound" : randint(45, 55), #or should i do height, hustle, and verticallity??
                    "Screen" : randint(45, 55), #ability to set screen
                    "Passing" : randint(45, 55), #pass throwing ability
                    "Hands" : randint(45, 55), #pass catching ability, pass stealing ability

                    #### harder to steal when in post i guess
                    "Back Down" : randint(45, 55), #in post. should there just be a strength rating for screens, driving, interior D, and post back downs?
                    "Post Fade" : randint(45, 55), #choose over right or left shoulder?
                    "Post Hook" : randint(45, 55), #standard center hookshot = kareem hook shot = brunson post floater
                    "Post Dropstep" : randint(45, 55),
                    
                    # "Ball Handle" : randint(45, 55), #ability to chain together moves?
                    "Stepback" : randint(45, 55), #used in post too
                    "Crossover" : randint(45, 55),
                    "Between Legs" : randint(45, 55), #dk if i wanna keep this
                    "Behind the back" : randint(45, 55), #or this 
                    "Hesitation" : randint(45, 55),
                    "Spin" : randint(45, 55), #used in post too
                    "Hopstep" : randint(45, 55), #used in post too
                    
                    "Drive" : randint(45, 55), #used for cuts and ball handler drives. left and right side rating?
                    # "Eurostep" : randint(45, 55), 
                    
                    "Deep" : randint(45, 55),
                    "3" : randint(45, 55),
                    "MidRange" : randint(45, 55),
                    "Inside" : randint(45, 55),
                    
                    "Dunk" : randint(45, 55),
                    # "Layup" : randint(45, 55), layup types? scoop layup, reverse layup, switch hand layup?
                    "Floater" : randint(45, 55), #only available after drive
                    
                    "Steal" : randint(45, 55), #pick pocket ability and interception
                    "Block" : randint(45, 55),
                    "Contest" : randint(45, 55), #how good your contest affects the shot
                    
                    "Defensive IQ" : randint(0, 100), #used to detect pump fakes or pass fakes. not sure if it will apply anywhere else. maybe against hesis?
                    "Offensive IQ" : randint(0, 100), #pump fakes or pass fakes believability rating
                                                      #if its successful it will only display as the player shooting or passing, if not it will tell the defender that they are faking a shot/pass   
                }
                
                self.hotzones = {
                    "Deep Center" : randint(45, 55), 
                    "Deep Right Wing" : randint(45, 55),
                    "Deep Left Wing" : randint(45, 55), 
                    "Top 3" : randint(45, 55), 
                    "Right Wing 3" : randint(45, 55),
                    "Left Wing 3" : randint(45, 55), 
                    "Right Corner 3" : randint(45, 55),
                    "Left Corner 3" : randint(45, 55),
                    "Top Mid" : randint(45, 55), 
                    "Right Wing Mid" : randint(45, 55),
                    "Left Wing Mid" : randint(45, 55), 
                    "Right Corner Mid" : randint(45, 55),
                    "Left Corner Mid" : randint(45, 55),
                    "Top Paint" : randint(45, 55), 
                    "Right Paint" : randint(45, 55),
                    "Left Paint" : randint(45, 55),
                }
            case "Wing": #idk maybe most balanced?
                pass
            case "Big": #bigger height, better interior D, block, dunk, rebound
                pass
        
        self.tendencies = {}
        
    def makeDecision(self, use_cpuOptions): #for cpu using tendencies
        return use_cpuOptions[0]
    
    
#the if statement is js to hide the functions inside
# if True:
#     def takeShot(self, courtLocation):
#         rtg = self.ratings[courtLocation] # will become calculations involving opponent defense and shit
        
#         if randint(1, 100) <= rtg:
#             print("success")
#         else:
#             print("fail")
            
#     def doPass(self):
#         pass
    
#     def doDribbleMove(self):
#         pass
    
#     def doMove(self):
#         pass
    
#     def doDrive(self):
#         pass
    
#     def doPostUp(self):
#         pass
    
#     def setScreen(self):
#         pass
    
#     def doCut_or_Roll(self): #move to the basket after screen or without it
#         pass
    
#     def doPopOut(self): #set up for a jumpshot off a screen
#         pass
    
#     def attemptSteal(self):
#         pass
    
#     def doContest(self):
#         pass

class Game:
    def __init__(self, user1, user2, cpu1, cpu2, difficulty, endScore=21, score = [0, 0]):    
        self.user1, self.user2, self.cpu1, self.cpu2, self.difficulty, self.endScore, self.score = user1, user2, cpu1, cpu2, difficulty, endScore, score
        self.recentActions = []

        
#ones u can choose on offense that only depend on location with the number of times u are asked for another choice before the cpu responds
            # "Pump Fake" : 1, 
            # "Shoot" : 1, 
            # "Layup" : 1, 
            # "Dunk" : 1,  
            # "Pass Fake" : 1, 
            # "Pass" : 1, 
            # "Dribble" : 1, 
            # "Post Up" : 1, 
            # "Move" : 2, 
            # "Call for Screen" : 1, 
            # "Teammate Cut" : 1, 
            # "Drive" : 2,
            # "Back-Out" : 2,
        
        
    def addScore(self, teamNum, amount):
        self.score[teamNum]+=amount
    
    def getOptions(self):
        return self.options
    
    def difficultyChanges(self):
        pass
 
    def chanceCalculations(self, userPlayer, cpuPlayer, offensiveAction, defensiveResponse = None):
        
        match self.recentActions[-1]:
            case "Shoot":
                # if userPlayer.location in spots[0:8]:
                pass
            case "Layup":
                pass
            case "Dunk":
                pass
            case "Pass":
                pass
            case "Dribble":
                pass
            case "Post Up":
                pass
            case "Move":
                pass
            case "Call for Screen":
                pass
            case "Teammate Cut":
                pass
            case "Drive":
                pass
            case "Back-Out":
                pass
            case "Contest":
                pass
            case "Position for Rebound":
                pass
            case "Steal":
                pass
            case "Stay on Defense":
                pass
    
    def determineSuccess(self, chance):
        success = randint(1,100)
        if success < chance:
            return True
        else: 
            return False
    def useTurn(self, possessionType, offensivePlayer, defensivePlayer):
        if possessionType == "Offense":
            if self.user1.onOffense and self.user2.onOffense:
                print(f"You are at {offensivePlayer.location}. Whats your next move? ")
                    
                if offensivePlayer.location in spots[0:8]: #3 and deep 3
                   self.options = ["Pump Fake", "Shoot", "Pass Fake", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
                elif offensivePlayer.location in spots[9:13]: #mid range
                   self.options = ["Pump Fake", "Shoot", "Pass Fake", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
                elif offensivePlayer.location in spots[13:]: #inside paint
                   self.options = ["Pump Fake", "Layup", "Dunk", "Pass Fake", "Pass", "Post Up", "Back-Out"]
                    
                print(self.options)
                self.getOptions()    
                # print(self.options)  #replace with UI
                # userChoice = 2#int(input("Type the number corresponding with the option, left to right starting at 0: \n"))
                # userChoice =self.options[userChoice]
                # if userChoice == "Pump Fake" or userChoice == "Pass Fake":
                #     oRtg = offensivePlayer.basicRatings["Offensive IQ"]
                #     total = oRtg + defensivePlayer.basicRatings["Defensive IQ"]
                #     c = round((oRtg/total) * 100)
                #     print(c)
                #     print(self.determineSuccess(c))
                #     if self.determineSuccess(c):
                #         userChoice = "Shoot"
                # self.recentActions.append(userChoice)
                        
                    
                # if userChoice in ["Move", "Drive", "Back-Out"]:
                #     if userChoice == "Move" or userChoice == "Back-Out":
                #         location_options = spots[0:13]
                #         if offensivePlayer.location in location_options:
                #             location_options.remove(offensivePlayer.location)
                #     elif userChoice == "Drive":
                #         location_options = spots[13:]
                #     print(location_options)
                # userChoice = self.actionRedirect(self.options[userChoice])
                # self.memoryCheck()
                # print(self.recentActions)
                # self.useTurn("Defense", offensivePlayer, defensivePlayer)    
            elif self.cpu1.onOffense and self.cpu2.onOffense:    
                if offensivePlayer.location in spots[0:8]: #3 and deep 3
                   self.cpuOptions = ["Pump Fake", "Shoot", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
                elif offensivePlayer.location in spots[9:13]: #mid range
                   self.cpuOptions = ["Pump Fake", "Shoot", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
                elif offensivePlayer.location in spots[13:]: #inside paint
                   self.cpuOptions = ["Pump Fake", "Layup", "Dunk", "Pass", "Post Up", "Back-Out"]
                cpuChoice = offensivePlayer.makeDecision(self.cpuOptions)
                self.recentActions.append(cpuChoice)
                cpuChoice = self.actionRedirect(cpuChoice)
                self.memoryCheck()
                self.useTurn("Defense", offensivePlayer, defensivePlayer)
                
        elif possessionType == "Defense":
            if self.user1.onDefense and self.user2.onDefense:
                if self.recentActions[-1] in ["Shoot", "Layup", "Dunk"]:
                   self.options = ["Contest", "Stand Ground", "Position for Rebound"] #stand ground means to not bite on what you think might be a pump fake
                elif self.recentActions[-1] in ["Dribble", "Move", "Back-Out", "Drive", "Pump Fake", "Pass Fake"]:
                   self.options = ["Steal", "Stay on Defense"]
                print(self.options)  #replace with UI
                userChoice = 1#int(input("Type the number corresponding with the option, left to right starting at 0: \n"))
                self.recentActions.append(self.options[userChoice])
                userChoice =self.options[userChoice]
                self.memoryCheck()
                self.chanceCalculations(defensivePlayer, offensivePlayer, userChoice, self.recentActions[-2])
            elif self.cpu1.onDefense and self.cpu2.onDefense:
                if self.recentActions[-1] in ["Shoot", "Layup", "Dunk"]:
                   self.cpuOptions = ["Contest", "Stand Ground", "Position for Rebound"] #stand ground means to not bite on what they think might be a pump fake
                elif self.recentActions[-1] in ["Dribble", "Move", "Back-Out", "Drive", "Pump Fake", "Pass Fake"]:
                   self.cpuOptions = ["Steal", "Stay on Defense"]
                cpuChoice = defensivePlayer.makeDecision(self.cpuOptions)
                self.recentActions.append(cpuChoice)
                self.memoryCheck()
                print(self.recentActions)
                self.chanceCalculations(offensivePlayer, defensivePlayer, self.recentActions[-2], cpuChoice)
        
    
    
    
    
    # def useTurn(self, possessionType, offensivePlayer, defensivePlayer):
    #     if possessionType == "Offense":
    #         if self.user1.onOffense and self.user2.onOffense:
    #             print(f"You are at {offensivePlayer.location}. Whats your next move? ")
                    
    #             if offensivePlayer.location in spots[0:8]: #3 and deep 3
    #                self.options = ["Pump Fake", "Shoot", "Pass Fake", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
    #             elif offensivePlayer.location in spots[9:13]: #mid range
    #                self.options = ["Pump Fake", "Shoot", "Pass Fake", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
    #             elif offensivePlayer.location in spots[13:]: #inside paint
    #                self.options = ["Pump Fake", "Layup", "Dunk", "Pass Fake", "Pass", "Post Up", "Back-Out"]
                    
    #             # screen = App.get_running_app().root.get_screen("game")
    #             # screen.makeOptions(self.options)    
    #             print(self.options)  #replace with UI
    #             userChoice = 1#int(input("Type the number corresponding with the option, left to right starting at 0: \n"))
    #             self.recentActions.append(self.options[userChoice])
    #             userChoice = self.actionRedirect(self.options[userChoice])
    #             self.memoryCheck()
    #             print(self.recentActions)
    #             self.useTurn("Defense", offensivePlayer, defensivePlayer)    
    #         elif self.cpu1.onOffense and self.cpu2.onOffense:    
    #             if offensivePlayer.location in spots[0:8]: #3 and deep 3
    #                self.cpuOptions = ["Pump Fake", "Shoot", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
    #             elif offensivePlayer.location in spots[9:13]: #mid range
    #                self.cpuOptions = ["Pump Fake", "Shoot", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
    #             elif offensivePlayer.location in spots[13:]: #inside paint
    #                self.cpuOptions = ["Pump Fake", "Layup", "Dunk", "Pass", "Post Up", "Back-Out"]
    #             cpuChoice = offensivePlayer.makeDecision(self.cpuOptions)
    #             self.recentActions.append(cpuChoice)
    #             cpuChoice = self.actionRedirect(cpuChoice)
    #             self.memoryCheck()
    #             self.useTurn("Defense", offensivePlayer, defensivePlayer)
                
    #     elif possessionType == "Defense":
    #         if self.user1.onDefense and self.user2.onDefense:
    #             if self.recentActions[-1] in ["Shoot", "Layup", "Dunk"]:
    #                self.options = ["Contest", "Stand Ground", "Position for Rebound"] #stand ground means to not bite on what you think might be a pump fake
    #             elif self.recentActions[-1] in ["Dribble", "Move", "Back-Out", "Drive"]:
    #                self.options = ["Steal", "Stay on Defense"]
    #             print(self.options)  #replace with UI
    #             userChoice = 1#int(input("Type the number corresponding with the option, left to right starting at 0: \n"))
    #             self.recentActions.append(self.options[userChoice])
    #             userChoice =self.options[userChoice]
    #             self.memoryCheck()
    #             self.chanceCalculations(defensivePlayer, offensivePlayer, userChoice, self.recentActions[-2])
    #         elif self.cpu1.onDefense and self.cpu2.onDefense:
    #             if self.recentActions[-1] in ["Shoot", "Layup", "Dunk"]:
    #                self.cpuOptions = ["Contest", "Stand Ground", "Position for Rebound"] #stand ground means to not bite on what they think might be a pump fake
    #             elif self.recentActions[-1] in ["Dribble", "Move", "Back-Out", "Drive"]:
    #                self.cpuOptions = ["Steal", "Stay on Defense"]
    #             cpuChoice = defensivePlayer.makeDecision(self.cpuOptions)
    #             self.recentActions.append(cpuChoice)
    #             self.memoryCheck()
    #             print(self.recentActions)
    #             self.chanceCalculations(offensivePlayer, defensivePlayer, self.recentActions[-2], cpuChoice)
        
        
    def memoryCheck(self):
        if len(self.recentActions) >= 7:
            self.recentActions.pop(0)
    
    # def actionRedirect(self, player, chosenOption):
    #     pass
            
    def startGame(self):
        ### might make it a "shoot for ball" where it uses one player from both team's 3 ball + random 3pt spot rating to decide
        self.recentActions.append("Start")
        choice = 0 #randint(0, 1)
        if choice == 0:
            print("You have started with possession of the ball.") #replace with UI
            self.user1.holdingBall = True
            self.user1.guardingBall = False
            self.user2.guardingBall = False
            self.user1.onOffense = True
            self.user2.onOffense = True
            
            self.cpu1.guardingBall = True
            self.user1.holdingBall = False
            self.user2.holdingBall = False
            self.cpu1.onDefense = True
            self.cpu2.onDefense = True
            self.useTurn("Offense", self.user1, self.cpu1)
            # actionL.config(text=f"It is your ball. What will you do? You are at {currentSpot}.") #replace with UI
        else:
            print("The opponent has started with possession of the ball.") #replace with UI
            self.cpu1.holdingBall = True
            self.cpu1.guardingBall = False
            self.cpu2.guardingBall = False
            self.cpu1.onOffense = True
            self.cpu2.onOffense = True
            
            self.user1.guardingBall = True
            self.cpu1.holdingBall = False
            self.cpu2.holdingBall = False
            self.user1.onDefense = True
            self.user2.onDefense = True
            self.useTurn("Offense", self.cpu1, self.user1)
    
    def endGame(self):
        if self.score[0] == self.endScore or self.score[1] == self.endScore:
            if self.score[0] > self.score[1]:
                print(f"You won with a score of {self.score[0]} to {self.score[1]}") #replace with UI
            else:
                print(f"You lost with a score of {self.score[0]} to {self.score[1]}") #replace with UI
            #prompt replay or exit using UI
            self.recentActions.clear()
            
        
            
# u1 = Player("ONE", "Guard")
# u2 = Player("TWO", "Big")   

# c1 = Player("ONE", "Guard")
# c2 = Player("TWO", "Big")

# print(u1.basicRatings)
# print(c1.basicRatings)
# print(u1.points)
# print(user1.ratings)
# print(user1.ratings)
# print(user2.ratings)
# print(user2.ratings)
# print(user2.ratings)


# fullGame = Game(u1, u2, c1, c2, "Easy")
# print(fullGame.score)
# fullGame.startGame()


    

