from random import *

#### half court is 47 ft away
#### court is 50 wide
#lets make (0,0) the center of the hoop
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
    def __init__(self, playerNum, playerType, name):
        self.playerNum, self.playerType = playerNum, playerType #playerType will not affect shooting ratings
        self.name = name
        self.energyUsed = 0
        self.heatLevel = 0
        
        self.dribbleChain = []
        
        # stats
        self.points = 0
        self.assists = 0
        self.rebounds = 0
        self.steals = 0
        self.blocks = 0
        self.turnovers = 0
        
        self.fga = 0
        self.fgm = 0
        self.three_fga = 0
        self.three_fgm = 0
        
        self.fts = 0 #no actual fts, its just how many times over the limit you were fouled. (5 fouls is the limit)
        self.fouled = 0 # are you a foul baiter
        self.fouls = 0 # keep ur hands to yourself
        
        # player states
        self.postingUp = False # obvious
        self.dribbled = False # whether the ball has been put on the floor or not
        self.pickedUpDribble = False # whether or not a pump fake occured following having put the ball on the floor 
        
        self.midDrive = False # used to determine whether a floater can be done
        # self.midJumpShot = False # used to determine whether a pass out of shot can be done. not sure if i will include this 
        # self.midLayup = False # used to determine whether a pass out of layup can be done or whether the layup can ba altered around the defender. not sure if i will include this
        
        self.faltered = False # did he just falter a little from the dribble but still standing, also used for pump fakes and pass fakes
        self.ankleBroken = False # did he fall over completely
        
        self.pumpFaking = False
        self.hasBeenPumpFaked = False #check whether cpu is able to tell that theyve been pump faked. to be used in their tendency to raise chance of jumping
                                      #or should cpu have no choice and just fall for it?
        
        self.wideOpen = False
        self.doubled = False
        
        self.holdingBall = False
        self.guardingBall = False #the defender on the one holding the ball
        
        self.passing = False
        self.receivingPass = False
        
        self.onOffense = False
        self.onDefense = False
        
        
        self.inPosition = False #for rebound
        
        if self.playerNum == "0":
            self.location = spots[0]
        elif self.playerNum == "1":
            self.location = spots[4]
        elif self.playerNum == "2":
            self.location = spots[5]
        elif self.playerNum == "3":
            self.location = spots[6]
        elif self.playerNum == "4":
            self.location = spots[7]
    
        self.defendedBy = int(self.playerNum) #represents opposing teams playerNum

        
        match self.playerType:
            
            case "Guard": #better dribbling, shorter, 
                self.basicRatings = {
                    # "staminaBonus" : randint(0, 25),   # higher means more energy per game or possession? what if you run out, you die? lmao.
                                                    # or maybe it determines how much energy is used per action and everyone starts out at 0 used.
                                                    # the more you use, the worse your ratings get. but maybe you cant run out? all players just thug it out. 
                                                    # used to prevent spamming dribbling (could also make chance to just drop ball).
                                                    # number could be a percentage of how much less energy is used to do an action. call it staminaBonus instead?
                    "Stamina" : randint(0,100), # how much the rest of the ratings go down as you use more energy points. (idk what the number will mean yet)
                    "Height" : randint(65, 82), #number represents inches. helps shoot over players, on rebounds, and throwing and catching passes.
                    "Strength" : randint(1, 100), #number has to be arbitrary ig. not sure if i want to include this. i will
                    "Hustle" : randint(1, 100), #same with this as strength. i will
                    "Verticality" : randint(15, 50), #num is inches. same as height. basically another boost. guards will typically have a higher one to compensate for lower height
                    
                    "Wide Open" : randint(5, 30), #no one even on you because someone else was double teamed?
                    "Open" : randint(-1, 20),
                    "Contested" : randint(-20, 10),
                    "Heavily Contested" : randint(-30, 1), #double teamed?
                    
                    "StandStill Shot" : randint(-5, 20), #catch and shoot, right off pass or at the start of the possession i guess
                    "Moving Shot" : randint(-20, 20), #after dribble moves
                    
                    "Draw Foul" : randint(1, 30), #higher = better at drawing fouls
                    "Foul" : randint(1, 30), #higher = more likely to foul someone (worse)
                    "Ball Security" : randint(1, 100), #protect against getting stripped
                    # "Heatablility" : randint(45, 55), #how easy to heat up? idek if i want this to be a thing
                    
                    "Interior D" : randint(1, 100), #cutting off drives and cuts after screens
                    "Perimeter D" : randint(1, 100), #prevent ankle breakers and get through screens or switch
                    
                    "Rebound" : randint(1, 100), #or should i do height, hustle, and verticallity?? yah. strength too. this one will be about positioning and technique
                    "Screen" : randint(1, 100), #ability to set screen
                    "Passing" : randint(1, 100), #pass throwing ability
                    "Hands" : randint(1, 100), #pass catching ability, pass stealing ability
                    "Craftiness" : randint(1, 100), #if high enough itll give you a chance to avoid a block mid layup and either readjust layup or pass out

                    #### harder to steal when in post i guess
                    # "Back Down" : randint(45, 55), #in post. should there just be a strength rating for screens, driving, interior D, and post back downs?
                    "Post Fade" : randint(40, 60), #choose over right or left shoulder? no. spin if you want to go the other way. 
                    "Post Hook" : randint(45, 65), #standard center hookshot = kareem hook shot = brunson post floater
                    # "Post Dropstep" : randint(45, 55), no because idk where to put it
                    
                    "Ball Handle" : randint(45, 55), #ability to chain together moves? low rating and doing too many in a row causes turnover. kind of an arbitrary rating ngl
                    "Stepback" : randint(-20, 20), #used in post too
                    "Crossover" : randint(-20, 20),
                    "Between Legs" : randint(-20, 20), #dk if i wanna keep this
                    "Behind the back" : randint(-20, 20), #or this 
                    "Hesitation" : randint(-20, 20),
                    "Spin" : randint(-20, 20), #used in post too
                    "Hopstep" : randint(-20, 20), #used in post too
                    
                    # "Jab Step" : randint(45, 55),
                    
                    "Drive" : randint(1, 100), #used for cuts and ball handler drives. left and right side rating? yes
                    "Drive Left" : randint(-50, 50), #these are basically your dominant hand. you will be weaker in one.
                    "Drive Right" : randint(-50, 50), #they will be treated as bonus percentage. can be negative
                    
                    "Deep" : randint(1, 20),
                    "3" : randint(25, 40),
                    "MidRange" : randint(35, 50),
                    "Inside" : randint(45, 60),
                    
                    "Dunk" : randint(0, 50),
                    "Layup" : randint(1, 50), #layup types? scoop layup, reverse layup, switch hand layup? no
                    "Floater" : randint(1, 50), #only available after drive.
                    
                    "Steal" : randint(1, 100), #pick pocket ability and interception
                    "Block" : randint(1, 100),
                    "Contest" : randint(5, 50), #how good your contest affects the shot
                    
                    "Defensive IQ" : randint(1, 100), #used to detect pump fakes or pass fakes. not sure if it will apply anywhere else. maybe against hesis?
                    "Offensive IQ" : randint(1, 100), #pump fakes or pass fakes believability rating
                                                      #if its successful it will only display as the player shooting or passing, if not it will tell the defender that they are faking a shot/pass   
                }
                
            case "Wing": #idk maybe most balanced?
                pass
            case "Big": #bigger height, better interior D, block, dunk, rebound
                pass
        
        self.hotzones = {
                    "Deep Center" : randint(-30, 30), 
                    "Deep Right Wing" : randint(-30, 30),
                    "Deep Left Wing" : randint(-30, 30), 
                    "Top 3" : randint(-30, 30), 
                    "Right Wing 3" : randint(-30, 30),
                    "Left Wing 3" : randint(-30, 30), 
                    "Right Corner 3" : randint(-30, 30),
                    "Left Corner 3" : randint(-30, 30),
                    "Top Mid" : randint(-30, 30), 
                    "Right Wing Mid" : randint(-30, 30),
                    "Left Wing Mid" : randint(-30, 30), 
                    "Right Corner Mid" : randint(-30, 30),
                    "Left Corner Mid" : randint(-30, 30),
                    "Top Paint" : randint(-30, 30), 
                    "Right Paint" : randint(-30, 30),
                    "Left Paint" : randint(-30, 30),
                }
        
        self.tendencies = {
            "Pump Fake" : 0,
            "Pass Fake" : 0,
            
            "Shoot" : 0,
            "Layup" : 0,
            "Dunk" : 0,
            "Post Up" : 0,
            "Post Action" : 0,
            "Exit Post" : 0, 
            "Post Fade" : 0,
            "Post Hook" : 0,
            "Post Moves" : 0,
            
            "Dribble" : 0,
            "Stepback" : 0,
            "Crossover" : 0,
            "Between Legs"  : 0,
            "Behind the back" : 0, 
            "Hesitation" : 0, 
            "Shimmy" : 0, 
            "Spin" : 0, 
            "Hopstep" : 0,
            
            "Pass" : 0,
            "Teammate Cut" : 0,
            "Call for Screen" : 0,
             
            "Move" : 0,
            "Back-Out" : 0,
            
            "Drive" : 0,
            "Drive Left" : 0,
            "Drive Right" : 0,
            
            # "Back Down" : 0, still dk how to do this one
            
            "Contest" : 0,
            "Stand Ground" : 0,
            "Position for Rebound" : 0,
            
            "Steal" : 0,
            "Stay on Defense" : 0
        }
        
    def makeTendencies(self): #for making cpu tendencies based on its ratings
        pass
    
    def makeOverall(self):
        pass
 
    def reset(self):
        if self.playerNum == "0":
            self.location = spots[0]
        elif self.playerNum == "1":
            self.location = spots[4]
        elif self.playerNum == "2":
            self.location = spots[5]
        elif self.playerNum == "3":
            self.location = spots[6]
        elif self.playerNum == "4":
            self.location = spots[7]
            
        self.postingUp = False 
        self.dribbled = False 
        self.pickedUpDribble = False
        self.midDrive = False 
        # self.midJumpShot = False
        # self.midLayup = False
        self.faltered = False 
        self.ankleBroken = False
        self.pumpFaking = False
        self.hasBeenPumpFaked = False
        self.wideOpen = False
        self.doubled = False
        self.holdingBall = False
        self.guardingBall = False
        self.onOffense = False
        self.onDefense = False
        self.defendedBy = int(self.playerNum)
        self.inPosition = False
        self.passing = False
        self.receivingPass = False
        
class Team: 
    def __init__(self, *players):
        self.players = list(players)
        self.teamSize = len(players)
        
        self.onOffense = False
        self.onDefense = False
        
        self.ballHandler = None #self.players[0]
        self.onBallDefender = None #self.players[0]
        
        self.currentChoice = ""
        
        self.playerDict = {}
        
    def update(self):
        if self.onOffense and not self.onDefense:    
            for player in self.players:
                player.onOffense = True
                player.onDefense = False
                
                player.guardingBall = False
                
                if player.holdingBall:
                    self.ballHandler = player
        elif self.onDefense and not self.onOffense:    
            for player in self.players:
                player.onOffense = False
                player.onDefense = True  
                player.holdingBall = False
                
                if player.guardingBall:
                    self.onBallDefender = player   

class Game:
    def __init__(self, team1, team2, difficulty, statObj,  realPlayers = 1):    
        self.difficulty, self.statObj = difficulty, statObj
        self.team1, self.team2 = team1, team2
        self.realPlayers = realPlayers             
          
        self.tempOptions = [] #REMOVE THIS AFTER          
                
        self.passing = True
        self.passingOptions = []
        self.tempChoiceHold = ""
        
        self.targetPlayer = team1.players[1] #default but it changes obv when you choose a player to pass to
        
        self.gameText = "Loading..."

        if self.team1.teamSize and self.team2.teamSize == 1:
            print("Team moves disabled")
            self.passing = False
            
        if self.team1.teamSize != self.team2.teamSize:
            print("Teams are not the same size.")
            # raise error
            # return this to react somehow
         
        # self.playerMatchups = {}
        # for p1, p2 in zip(self.team1.players, self.team2.players):
        #     self.playerMatchups[p1] = p2
            
    def startPossession(self, beginning = True, startTeam = None, allowDoubleTeam = True):
        for p1, p2 in zip(self.team1.players, self.team2.players):
            p1.doubled = False
            p2.doubled = False
        
        if beginning: #start of game
            # randomPlayer1 = randint(1, self.team1.TeamSize)   i was gonna make a "shoot for it"
            # randomPlayer2 = randint(1, self.team2.TeamSize)   idk if ill ever do that in the end
            startTeam = 1#randint(1, 2)
            
        if startTeam == 1:
            self.team1.onOffense = True
            self.team1.onDefense = False
            
            self.team2.onOffense = False 
            self.team2.onDefense = True 
            
            if beginning:
                self.team1.players[0].holdingBall = True
                self.team2.players[0].holdingBall = False
                
                self.team1.players[0].guardingBall = False
                self.team2.players[0].guardingBall = True
                        
            otherTeamNum = 2
            
        if startTeam == 2:
            self.team2.onOffense = True
            self.team2.onDefense = False
            
            self.team1.onOffense = False 
            self.team1.onDefense = True   
            
            if beginning:
                self.team2.players[0].holdingBall = True
                self.team1.players[0].holdingBall = False
                
                self.team2.players[0].guardingBall = False
                self.team1.players[0].guardingBall = True
                
            otherTeamNum = 1
            
        self.team1.update()
        self.team2.update()
        
        if allowDoubleTeam:
            self.makeOptions(otherTeamNum, False, None, None, True) # start of a normal possession
        else:
            self.makeOptions(startTeam) # off a steal or a pass to a wide open player
            
               
    def cpuTendencies(self, cpuOptions):
        # allTendencies = []
        # for op in cpuOptions:
        #     tendency = self.team2.onBallDefender.basicRatings[op]
        #     allTendencies.append(tendency)   
        # return allTendencies 
        cpuChoice = choice(cpuOptions)
        # self.cpuCurrentChoice = cpuChoice
        self.team2.currentChoice = cpuChoice
        print(f"CPU chose {cpuChoice}")
        self.handleInput(cpuChoice, 2)
            
    def outputOutcome(self):
        return self.gameText    
        
        # case "Pump Fake"
        # case "Pass" | "Pass Fake" | "Drive" | "Dribble" | "Post Moves":
        #     options = ["Steal", "Stay on Defense", "Double Team"]
        # case "Drive Left" | "Drive Right":
        #     options = ["Left", "Center", "Right"] #offensive's left = defender's right
        # case "Call for Screen":
        #     options = ["Go Over", "Go Under", "Switch"]     
        
    def calcDribble(self, offensivePlayer, defender):
        handleRtg = offensivePlayer.basicRatings["Ball Handle"]   
        perD = defender.basicRatings["Perimeter D"] 
        dribbleLen = len(offensivePlayer.dribbleChain)    
        
        
        
    def calcRebound(self, team, otherTeam):
        oReboundRtgs = []
        dReboundRtgs = []
        
        oReaches = []
        dReaches = []
        
        for player in team.players:
            rbRtg = player.basicRatings["Rebound"]
            handRtg = player.basicRatings["Hands"]
            strengthRtg = player.basicRatings["Strength"]
            height = player.basicRatings["Height"]
            vert = player.basicRatings["Verticality"]
            hustleRtg = player.basicRatings["Hustle"]
            
            oReaches.append(height+vert)
            
            chance = rbRtg * .3 + handRtg * .2 + strengthRtg * .2  + hustleRtg * .3 
            
            if player.inPosition:
                chance += 10
            
            oReboundRtgs.append(chance)
            
            
        for player in otherTeam.players:
            rbRtg = player.basicRatings["Rebound"]
            handRtg = player.basicRatings["Hands"]
            strengthRtg = player.basicRatings["Strength"]
            height = player.basicRatings["Height"]
            vert = player.basicRatings["Verticality"]
            hustleRtg = player.basicRatings["Hustle"]
            
            dReaches.append(height+vert)
            
            chance = rbRtg * .3 + handRtg * .2 + strengthRtg * .2  + hustleRtg * .3 
            
            if player.inPosition:
                chance += 10
            
            dReboundRtgs.append(chance)
        
        avgO = sum(oReboundRtgs)/len(oReboundRtgs)
        avgD = sum(dReboundRtgs)/len(dReboundRtgs)
        
        if avgO > avgD:
            oReboundRtgs = [rtg + 5 for rtg in oReboundRtgs] 
        elif avgO < avgD:
            dReboundRtgs = [rtg + 5 for rtg in dReboundRtgs] 
            
        maxOReach = max(oReaches)
        maxDReach = max(dReaches)
        
        if maxOReach > maxDReach:
            oReboundRtgs[oReaches.index(maxOReach)] += 10
        elif maxOReach < maxDReach:
            dReboundRtgs[dReaches.index(maxDReach)] += 10
        
        allPlayers = team.players + otherTeam.players
        allChances = oReboundRtgs + dReboundRtgs
        # allReaches = oReaches + dReaches
        
        # for c, p  in enumerate(allPlayers):
        #     print(p.name, allChances[c], allReaches[c])
        
        resultingPlayer = choices(allPlayers, weights=allChances)[0]
        if resultingPlayer in allPlayers[0:team.teamSize]:
            resultingTeam = team
            resultingTeamNum = 1
            resultingOtherTeam = otherTeam
        elif resultingPlayer in allPlayers[otherTeam.teamSize:]:
            resultingTeam = otherTeam
            resultingTeamNum = 2
            resultingOtherTeam = team

        return resultingPlayer, resultingTeamNum, resultingTeam, resultingOtherTeam
                
    def calcFoul(self, ballHandler, defender,  offensiveTeamNum, defendingTeamNum, extra = 1,):
        drawFoulRtg = ballHandler.basicRatings["Draw Foul"]
        foulRtg = defender.basicRatings["Foul"]
        chance = (drawFoulRtg/100) * (foulRtg/100) * extra
        if ballHandler.doubled:
            chance += 10
        result = self.determineSuccess(chance)
        if result:
            self.statObj.fouls[defendingTeamNum - 1] += 1
            self.checkFouls(defendingTeamNum, offensiveTeamNum)
            defender.fouls += 1
            ballHandler.fouled += 1
        
        return result
    
    def checkFouls(self, teamNum, otherTeamNum):
        if self.statObj.fouls[teamNum - 1] >= 5:
             self.statObj.addScore(otherTeamNum - 1, 1)
             print("Excessive Fouling. One point to the other team.")
             print(self.statObj.score)
        else:
            print(self.statObj.fouls[teamNum - 1])
        
    def chanceCalc(self, offensiveAction, defensiveAction, ballHandler, defender, teamNum, otherTeamNum):
        # finalChance = 0 #can only be removed once all done but its fine to stay
        foulPresent = False
        shotBlocked = False
        ballStolen = False
        
        bonus = 1
        #need a normal "did a dribble move" bonus. because players do dribbles to get into a shooting rhythm as well and not only in hopes of dropping someone
        if defender.faltered:
            bonus = 1.1   
        if defender.ankleBroken:
            bonus = 1.2
        
        ostrengthRtg = ballHandler.basicRatings["Strength"]
        dStrengthRtg = defender.basicRatings["Strength"]
        
        oStamina = ballHandler.basicRatings["Stamina"] #offensive player
        dStamina = defender.basicRatings["Stamina"] #defensive player
        
        oHeight = ballHandler.basicRatings["Height"] #offensive player
        dHeight = defender.basicRatings["Height"] #defensive player 
        
        oVert = ballHandler.basicRatings["Verticality"] #offensive player
        dVert = defender.basicRatings["Verticality"] #defensive player
        
        match offensiveAction:
            case "Teammate Cut": #ballHandler refers to the cutting player
                match defensiveAction:
                    case "Stay on Defense":
                        intDef = defender.basicRatings["Interior D"]
                        driveRtg = ballHandler.basicRatings["Drive"]
                        
                        total = driveRtg + intDef
                        finalChance = (driveRtg/total) * 100
                        
                        result = self.determineSuccess(finalChance)
                    case "Watch":
                        result = True
                        
                if result:  
                    locNum = randint(13, 15)
                    location = spots[locNum]
                    
                    ballHandler.location = location
                    if not ballHandler.wideOpen:
                        defender.location = location
                    print(f"{ballHandler.name} has moved to {ballHandler.location}.")
                    self.makeOptions(teamNum)
                else:
                    print("Unable to cut through the defense.")
                    self.makeOptions(teamNum)
                
            case "Pump Fake":
                match defensiveAction:
                    case "Contest":
                        print("???")
                        defender.faltered = True
                        print("Fell for the pump fake?")
                        self.makeOptions(teamNum)
                    case "Stand Ground":
                        print("No effect.")
                        self.makeOptions(teamNum)
                    case "Position for Rebound":
                        print("Fell for it? Left to position for rebound.")
                        defender.inPosition = True
                        ballHandler.wideOpen = True

                ballHandler.pumpFaking = False
            
            case "Pass Fake":
                match defensiveAction:
                    case "Steal":
                        print("???")
                        defender.faltered = True
                        print("Fell for the pass fake?")
                        self.makeOptions(teamNum)
                    case "Stay on Defense":
                        print("No effect.")
                        self.makeOptions(teamNum)
                
                ballHandler.pumpFaking = False
                    
            case "Shoot" | "Post Fade" | "Post Hook" | "Floater" | "Layup" | "Dunk":
                if ballHandler.pumpFaking or defender.hasBeenPumpFaked:
                    if defensiveAction in ["Contest", "Verticality", "Block"]:
                        defender.faltered = True
                        print("Fell for the pump fake.")
                        ballHandler.pumpFaking = False
                        defender.hasBeenPumpFaked = False
                        self.makeOptions(teamNum)
                    # else: #?    
                else:
                    if (ballHandler.pickedUpDribble and ballHandler.dribbled) or (not ballHandler.pickedUpDribble and not ballHandler.dribbled):
                        shotTypeRtg = ballHandler.basicRatings["StandStill Shot"]
                    elif not ballHandler.pickedUpDribble and ballHandler.dribbled:
                        shotTypeRtg = ballHandler.basicRatings["Moving Shot"]
                        
                    shooterSpotRtg = ballHandler.hotzones[ballHandler.location]
                    
                    if ballHandler.location in spots[0:2]:
                        shotDist = "Deep"
                        amount = 3
                    elif ballHandler.location in spots[3:8]:
                        shotDist = "3" # yes post 3s allowed unlike in modern 2Ks
                        amount = 3
                    elif ballHandler.location in spots[8:13]:
                        shotDist = "MidRange" # floater only here
                        amount = 2
                    elif ballHandler.location in spots[13:]:
                        shotDist = "Inside"  # post hook, layup, and dunk can only be done here
                        amount = 2
                    
                    shotDistRtg = ballHandler.basicRatings[shotDist]    
                        
                    finalChance = shotDistRtg * (1 + shotTypeRtg/100) * (1 + shooterSpotRtg/100) * bonus  
                    
                    if not ballHandler.postingUp:
                        difHeight = oHeight - dHeight
                        if abs(difHeight) < 5:
                            difHeight = 0 # the difference is negligible and has no effect on the shot 
                        finalChance *= (1+difHeight/100) 
                        
                        if ballHandler.location in spots[13:]:
                            difVert = oVert - dVert
                            if abs(difVert) < 5:
                                difVert = 0 # the difference is negligible and has no effect on the shot 
                            finalChance *= (1+difVert/100) 
                    
                    try: #if its a post fade, post hook, layup, dunk, or floater, add that rating
                            extraRtg = ballHandler.basicRatings[offensiveAction] 
                            finalChance *= (1+extraRtg/100)
                    except: # error raised if offensiveAction ends up just being Shoot. can be ignored because there is no extra rating here then
                        pass 
                            
                    match defensiveAction:
                        case "Contest" | "Verticality" | "Block":
                            oContestedRtg = ballHandler.basicRatings["Contested"]
                            dContestRtg = defender.basicRatings["Contest"]
                            finalChance *= (1 + oContestedRtg/100) 
                            finalChance *= (1 - dContestRtg/100)  
                            
                            extra = 1.5
                            
                            blkRtg = defender.basicRatings["Block"]
                            if defensiveAction != "Block":
                                blkRtg *= .5 
                                extra = 1
                                
                            foulPresent = self.calcFoul(ballHandler, defender, teamNum, otherTeamNum, extra)
                            
                            shotBlocked = self.determineSuccess(blkRtg)
                        case "Stand Ground":
                            oOpenRtg = ballHandler.basicRatings["Open"]
                            finalChance *= (1 + oOpenRtg/100)
                        case "Position for Rebound" | "Give Up":
                            if defensiveAction == "Position for Rebound":
                                defender.inPosition = True
                            oWideOpenRtg = ballHandler.basicRatings["Wide Open"]
                            finalChance *= (1 + oWideOpenRtg/100) 
                        case "Intentionally Foul":
                            foulPresent = True
                            
                            ballHandler.fouled += 1
                            defender.fouls += 1
                            
                            finalChance *= .1
                            
                            difStrength = ostrengthRtg - dStrengthRtg
                            finalChance += difStrength
                    
                    if ballHandler.doubled:
                        finalChance -= 20
                        if finalChance < 1:
                            finalChance == 1
                    
                    if shotBlocked:
                        finalChance = 0
                        defender.blocks += 1
                        print("Shot blocked.")
                        
                    result = self.determineSuccess(finalChance) 
                    if result:
                        print(f"Ball went through hoop. Make-it, Take-it, ball at {spots[0]}")
                        
                        self.statObj.addScore(teamNum - 1, amount)
                        ballHandler.points += amount
                        
                        ballHandler.fgm += 1
                        ballHandler.fga += 1
                        
                        if amount == 3:
                            ballHandler.three_fgm += 1
                            ballHandler.three_fga += 1
                            self.statObj.three_fgm[teamNum - 1] += 1
                            self.statObj.three_fga[teamNum - 1] += 1
                            
                        self.statObj.fgm[teamNum - 1] += 1
                        self.statObj.fga[teamNum - 1] += 1
                        
                        # if assisted:
                        #     self.
                        
                        if foulPresent:
                            print("And one.")
                            self.statObj.addScore(teamNum - 1, 1)
                            ballHandler.points += 1
                            ballHandler.fouled += 1
                            defender.fouls += 1
                            self.statObj.fouls[otherTeamNum - 1] += 1

                        for player in self.team1.players:
                            player.reset()
                        for player in self.team2.players:
                            player.reset()
                            
                        self.startPossession(False, teamNum, True)
                        
                    else:
                        if foulPresent:
                            print(f"Foul. Ball at {spots[0]}")
                            
                            for player in self.team1.players:
                                player.reset()
                            for player in self.team2.players:
                                player.reset()
                            
                            self.startPossession(False, teamNum, True)
                        else:
                            print("Ball did not go through hoop.")
                            
                            ballHandler.fga += 1
                            if amount == 3:
                                ballHandler.three_fga += 1
                                self.statObj.three_fga[teamNum - 1] += 1
                            self.statObj.fga[teamNum - 1] += 1
                            
                            reboundResult = self.calcRebound(self.team1, self.team2)
                            reboundingPlayer = reboundResult[0]
                            reboundingTeamNum = reboundResult[1]
                            resultingTeam = reboundResult[2]
                            resultingOtherTeam = reboundResult[3]
                            
                            reboundingPlayer.rebounds += 1
                            ballHandler.holdingBall = False
                            defender.guardingBall = False
                            reboundingPlayer.holdingBall = True
                            newDefender = resultingOtherTeam.players[int(reboundingPlayer.defendedBy)]
                            newDefender.guardingBall = True
                             
                            
                            resultingTeam.ballHandler = reboundingPlayer
                            resultingOtherTeam.onBallDefender = newDefender
                            
                            self.statObj.rebounds[reboundingTeamNum - 1] += 1
                            
                            if reboundingTeamNum == teamNum:
                                print(f"Offensive Rebound by {reboundingPlayer.name}. They are at {reboundingPlayer.location}.")
                                for player in resultingTeam.players:
                                    player.doubled = False
                                    player.midDrive = False
                                    player.postingUp = False
                            else:
                                for player in self.team1.players:
                                    player.reset()
                                for player in self.team2.players:
                                    player.reset()
                                                        
                            self.startPossession(False, reboundingTeamNum, True)
                    defender.faltered = False
                    defender.ankleBroken = False                                
            case "Pass":
                if ballHandler.pumpFaking or defender.hasBeenPumpFaked:
                    if defensiveAction == "Steal":
                        defender.faltered = True
                        print("That was a pass fake.")
                        ballHandler.pumpFaking = False
                        defender.hasBeenPumpFaked = False
                        self.makeOptions(teamNum)
                else:
                    passRtg = ballHandler.basicRatings["Passing"]
                    otHandRtg = self.targetPlayer.basicRatings["Hands"] # the player who is receiving the pass's ability to catch it

                    match defensiveAction:
                        
                        case "Steal":
                            dStealRtg = defender.basicRatings["Steal"]
                            dHandRtg = defender.basicRatings["Hands"] # the player stealing it's ability to intercept

                            oChance = passRtg + otHandRtg
                            dChance = dStealRtg + dHandRtg
                            
                            if ballHandler.doubled:
                                dChance += 20
                            total = oChance + dChance
                            stealChance = (dChance/total) * 100
                            ballStolen = self.determineSuccess(stealChance)
                            
                        case "Stay on Defense" | "Give Up":
                            pass
                    
                    if ballStolen:
                        print("Pass intercepted.")
                        defender.holdingBall = True
                        defender.guardingBall = False
                        ballHandler.holdingBall = False
                        ballHandler.guardingBall = True
                        
                        
                        self.startPossession(False, otherTeamNum, False)
                        
                    else:
                        if defender.faltered:
                            bonus = 10
                        else:
                            bonus = 0
                        finalChance = passRtg + otHandRtg + bonus
                        if finalChance >= 100:
                            finalChance = 99
                        
                        if ballHandler.doubled:
                            finalChance -= 20
                            if finalChance < 1:
                                finalChance == 1
                        
                        result = self.determineSuccess(finalChance)
                        if result:
                            
                            ballHandler.holdingBall = False
                            defender.guardingBall = False
                            self.targetPlayer.holdingBall = True
                            self.targetPlayer.receivingPass = True
                            
                            print(f"Pass successful. {self.targetPlayer.name} has the ball at {self.targetPlayer.location}.")
                            
                            if self.targetPlayer.wideOpen:
                                self.startPossession(False, teamNum, False)
                            else:
                                self.startPossession(False, teamNum, True)
                                
                        else:
                            print("Pass slipped through teammates fingers and went out-of-bounds.")
                            defender.holdingBall = True
                            defender.guardingBall = False
                            ballHandler.holdingBall = False
                            ballHandler.guardingBall = True
                            
                            self.startPossession(False, otherTeamNum, True)   
                        defender.faltered = False
                        defender.ankleBroken = False
                        
            case "Drive Left" | "Drive Right" | "Dribble" | "Post Moves":
                intDef = defender.basicRatings["Interior D"]
                perDef = defender.basicRatings["Perimeter D"]
                
                if offensiveAction in ["Dribble", "Post Moves"]:
                    getLatestDribble = ballHandler.dribbleChain[-1]
                    specificDribbleRtg = ballHandler.basicRatings[getLatestDribble]
                    
                    dribbleRtg = ballHandlingRtg * (1 + specificDribbleRtg/100)
                
                if offensiveAction in ["Drive Left", "Drive Right"]:
                    direction = offensiveAction
                    driveRtg = ballHandler.basicRatings["Drive"] * ballHandler.basicRatings[direction]
                ballHandlingRtg = ballHandler.basicRatings["Ball Handle"]
                ballSecRtg = ballHandler.basicRatings["Ball Security"]
                                                    
                
                match defensiveAction:
                    case "Steal":
                        dStealRtg = defender.basicRatings["Steal"]
                        
                        foulPresent = self.calcFoul(ballHandler, defender, teamNum, otherTeamNum)
                        
                        total = ballSecRtg + dStealRtg
                        stealChance = (dStealRtg/total) * 100
                        ballStolen = self.determineSuccess(stealChance)
                                                
                        if not ballStolen:
                            intDef -= 20
                            perDef -= 20
                            
                    case "Stay on Defense":    
                        pass
                    
                if offensiveAction != "Dribble":
                    if offensiveAction in ["Drive Left", "Drive Right"]:
                        total = driveRtg + intDef
                    else:
                        total = dribbleRtg + intDef
                else:
                    total = dribbleRtg + perDef
                    
                if offensiveAction in ["Drive Left", "Drive Right"]:
                    finalChance = (driveRtg/total) * 100
                else:    
                    finalChance = (dribbleRtg/total) * 100
                
                if ballStolen:
                    print(f"Ball stripped and stolen by {defender.name}.")
                    defender.holdingBall = True
                    defender.guardingBall = False
                    ballHandler.holdingBall = False
                    ballHandler.guardingBall = True
                    
                    self.startPossession(False, otherTeamNum, False)
                
                else:   
                    if defender.faltered:
                        finalChance += 10 #bonus
                     
                    if defensiveAction == "Give Up":
                        finalChance = 99
                                                                        
                    result = self.determineSuccess(finalChance)
                    if offensiveAction in ["Drive Left", "Drive Right"]:
                        if result:    
                            self.makeOptions(teamNum, True, offensiveAction)
                        else:
                            print("Unable to drive through the defense.")
                            self.makeOptions(teamNum)
                    else:
                        if result:
                            # it adds a rhythm bonus to next action, but also then calculates if the defender 
                            # falters or even has their ankles broken
                            self.makeOptions(teamNum)
                        else:
                            ballHandler.dribbleChain.clear()
                            dHandRtg = defender.basicRatings["Hands"]
                            o = ballSecRtg + ballHandlingRtg
                            craftinessRtg = ballHandler.basicRatings["Craftiness"]
                            pickUpChance = o - dHandRtg
                            keepDribble = o + craftinessRtg - dHandRtg
                            possibleOutcomes = ["Turnover", "Picked Up Dribble", "Keep Dribbling"]
                            outcome = choices(possibleOutcomes, weights=[dHandRtg, pickUpChance, keepDribble])[0]
                            match outcome:
                                case "Turnover":
                                    pass
                                case "Picked Up Dribble":
                                    ballHandler.pickedUpDribble = True
                                case "Keep Dribbling":
                                    self.makeOptions(teamNum)
                             # fumble the ball and a further calculation to determine whether it leads to
                                 # a turnover, a picked up dribble, or in best case: you get to keep dribbling
                    defender.faltered = False
                    defender.ankleBroken = False
                    
            case "Call for Screen":
                match defensiveAction:
                    case "Go Over":
                        pass
                    case "Go Under":
                        pass
                    case "Switch":
                        pass  
            # case "":
            #     match defensiveAction:
            #         case "":
            #             pass  
              
    def makeOptions(self, team = 1, isSecondAction = False, firstAction = None, offensiveAction = None, beforeOffenseAction = False):
        if team == 1:
            team = self.team1
            otherTeam = self.team2
        elif team == 2:
            team = self.team2
            otherTeam = self.team1 
        else:
            print(f"Team number: {team}")
            print("Not a team number")

        if beforeOffenseAction and self.passing:
            print(f"{otherTeam.ballHandler.name} has the ball at {otherTeam.ballHandler.location}.")
            options = ["Single Coverage", "Double Team"]            
        else:    
            # for p1, p2 in zip(team.players, otherTeam.players):
            #     if p1.holdingBall:
            #         print(p1.name)
            #         team.ballHandler = p1
            #     if p2.guardingBall:
            #         print(p2.name)
            #         otherTeam.onBallDefeder = p2
                        
            # print(team.ballHandler.name)
            # print(otherTeam.onBallDefender.name)
            
            # otherTeam.players[team.ballHandler.defendedBy].guardingBall = True
            
            if not isSecondAction:
                if team.onOffense:
                    print(f"{team.ballHandler.name} at {team.ballHandler.location}:")
                    if not team.ballHandler.postingUp:
                        if team.ballHandler.location in spots[0:13]: #deep 3, normal 3, mid range
                            options = ["Pump Fake", "Shoot", "Pass Fake", "Pass", "Dribble", "Post Up", "Move", "Call for Screen", "Teammate Cut", "Drive"]
                            if team.ballHandler.wideOpen:
                                options.remove("Call for Screen")
                            if team.ballHandler.doubled:
                                options.remove("Move")
                                options.remove("Call for Screen")
                        elif team.ballHandler.location in spots[13:]: #inside paint
                                options = ["Pump Fake", "Layup", "Dunk", "Pass Fake", "Pass", "Post Up", "Teammate Cut", "Back-Out"]
                    else:
                        if team.ballHandler.location in spots[0:13]: #deep 3, normal 3, mid range
                            options = ["Pump Fake", "Post Fade", "Pass Fake", "Pass", "Post Moves", "Exit Post", "Call for Screen", "Teammate Cut"]#, "Back Down"] 
                            if team.ballHandler.wideOpen:
                                options.remove("Call for Screen")
                        elif team.ballHandler.location in spots[13:]: #inside paint
                            options = ["Pump Fake", "Post Fade", "Post Hook", "Layup", "Dunk", "Pass Fake", "Pass", "Post Moves", "Exit Post", "Teammate Cut"]
                    
                    if team.ballHandler.pickedUpDribble:
                        #no movement allowed 
                        for option in ["Move", "Back-Out", "Call for Screen", "Drive", "Back Down", "Dribble", "Post Moves"]:
                            try:
                                options.remove(option)
                                print(f"{option} removed")
                            except:
                                print(f"{option} not present")
                        else:
                            pass #movement allowed
                    
                    if team.ballHandler.midDrive and team.ballHandler.location in spots[8:13]: # mid range
                            options = ["Floater", "Stop Drive", "Continue Drive"] 
                            # this triggers if you choose to drive to the mid range. basically can choose to do a floater,
                            # stop where you chose to drive and see options,
                            # or change your mind and keep driving
                    
                    if team.ballHandler.basicRatings["Dunk"] == 0:
                        try:
                            options.remove("Dunk") #you cant dunk lil bro
                        except:
                            pass
                    
                    # if team.ballHandler.midJumpShot:
                    #     options = ["Pass", "No Change"]
                    # if team.ballHandler.midLayup:
                    #     options = ["Change Layup Type", "Pass", "No Change"]
                    
                elif team.onDefense:
                    match offensiveAction:
                        case "Shoot" | "Post Fade" | "Post Hook" | "Pump Fake" | "Floater": # need to pass whether the cpu sees shoot or pump fake into the tendencies func so that it can actually be used to fool the cpu
                            options = ["Contest", "Stand Ground", "Position for Rebound"]
                            if otherTeam.ballHandler.wideOpen:
                                options = ["Give Up", "Late Contest", "Position for Rebound"]
                            if team == self.team2 and self.realPlayers == 1:
                                if team.onBallDefender.hasBeenPumpFaked:
                                    options = ["Contest"]
                        case "Layup" | "Dunk":
                            options = ["Verticality", "Block", "Stand Ground", "Intentionally Foul"] #foul increases chance they miss. they might still make it if stat is good enough and strength is high enough
                                                                                                    #side note should i add a hard foul to every situation js cuz idk lol
                            if otherTeam.ballHandler.wideOpen:
                                options = ["Give Up"]
                            if team == self.team2 and self.realPlayers == 1:
                                if team.onBallDefender.hasBeenPumpFaked:
                                    options = ["Verticality", "Block"]
                        case "Pass" | "Pass Fake" :
                            options = ["Steal", "Stay on Defense"]
                            if otherTeam.ballHandler.wideOpen:
                                options = ["Give Up"]
                            if team == self.team2 and self.realPlayers == 1:
                                if team.onBallDefender.hasBeenPumpFaked:
                                    options = ["Steal"]
                        case "Drive Left" | "Drive Right" | "Dribble" | "Post Moves":
                            options = ["Steal", "Stay on Defense"]
                            if otherTeam.ballHandler.wideOpen:
                                options = ["Give Up", "Get Back on Defense"]
                        case "Call for Screen":
                            options = ["Go Over", "Go Under", "Switch"]  
                
                    if team.onBallDefender.faltered:
                        # need to pass some sort of positive effect to the offense's next move
                        for option in ["Block", "Steal", "Go Over"]:
                            try:
                                options.remove(option)
                                print(f"{option} removed")
                            except:
                                pass 
                    
                    if team.onBallDefender.ankleBroken:
                        # need to pass some sort of bigger positive effect to the offense's next move
                        overallDefensiveAbility = team.onBallDefender.basicRatings["Hustle"] + team.onBallDefender.basicRatings["Interior D"] + team.onBallDefender.basicRatings["Perimeter D"] + team.onBallDefender.basicRatings["Defensive IQ"]
                        if overallDefensiveAbility > 200 and team.onBallDefender.energyUsed < 50:
                            options = ["Give Up", "Recover"]
                        else:
                            options = ["Give Up"]

                    # if team == self.team2 and self.realPlayers == 1:
                    #     if team.onBallDefender.hasBeenPumpFaked:
                    #         options = ["Contest"] #make it easier for me and player. the cpu has to contest if their ratings falsly show them "shoot" when its a pump fake.
                
                if not self.passing: # no teammates
                    for option in ["Pass Fake", "Pass", "Call for Screen", "Teammate Cut"]:
                        try:
                            options.remove(option)
                            print(f"{option} removed")
                        except:
                            pass
                            
                
                # if team.ballHandler.wideOpen:
                #     for option in ["Contest", "Stand Ground", "Verticality", "Block", "Intentionally Foul", "Steal"]
                            
            else:
                match firstAction:
                    case "Pass" | "Call for Screen" | "Teammate Cut" | "Double Team":
                        options = []
                        team.playerDict = {}
                        for player in team.players:
                            team.playerDict[f"{player.name} (at {player.location})"] = player
                        optionsSTR = list(team.playerDict.keys())
                        optionsOBJ = list(team.playerDict.values())
                        
                        if firstAction != "Double Team":
                            removeableOption = team.ballHandler
                        else:
                            removeableOption = team.onBallDefender
                        
                        for i, option in enumerate(optionsOBJ):
                            if option != removeableOption:
                                options.append(optionsSTR[i])
                        self.passingOptions = options
                    case "Dribble" | "Post Moves":
                        if not team.ballHandler.postingUp:
                            options = ["Stepback", "Crossover", "Between Legs", "Behind the back", "Hesitation", "Spin", "Hopstep"]
                        else:
                            options = ["Stepback", "Shimmy", "Spin", "Hopstep"] #shimmy = hesitation
                    case "Move" | "Back-Out":
                        options = spots[0:13]
                        try:
                            options.remove(team.ballHandler.location) #remove own player location as a choice
                        except:
                            pass
                        for player in team.players:
                            try:
                                options.remove(player.location) #remove choices where other teammates are at
                            except:
                                continue
                    case "Drive":
                        options = ["Drive Left", "Drive Right"]
                    case "Drive Left" | "Drive Right":
                        if team.ballHandler.location in spots[0:8]:
                            options = spots[8:]
                        elif team.ballHandler.location in spots[8:13]:
                            options = spots[13:]
                        for player in team.players:
                            try:
                                options.remove(player.location) #remove choices where other teammates are at
                            except:
                                continue
                    case "Continue Drive":
                        options = spots[13:] 
                        for player in team.players:
                            try:
                                options.remove(player.location) #remove choices where other teammates are at
                            except:
                                continue  
                    # case "Layup":
                    #     options = ["Fingerroll", "Scoop", "Reverse"]
        
        self.tempOptions = options   
        print("")                         
        for i, option in enumerate(options, 0):
            print(i, option)
        print("")                         
        if team == self.team2:
            self.cpuTendencies(options)
        else:
            return options
        
    def handleInput(self, choice, teamNum = 1):
        if teamNum == 1:
            team = self.team1
            otherTeamNum = 2
            otherTeam = self.team2
        elif teamNum == 2:
            team = self.team2
            otherTeamNum = 1
            otherTeam = self.team1
        
        match choice:
            #offense            
            case "Pass" | "Call for Screen" | "Teammate Cut" | "Dribble"| "Post Moves" | "Move" | "Back-Out" | "Drive" | "Continue Drive":#| "Layup":
                if self.tempChoiceHold not in ["Dribble", "Post Moves"]:
                    team.ballHandler.dribbleChain.clear()
                if choice in ["Pass", "Call for Screen", "Drive", "Teammate Cut"]:
                    self.tempChoiceHold = choice 
                self.makeOptions(teamNum, True, choice)
                
                
            case "Shoot" | "Dunk" | "Floater" | "Post Fade" | "Post Hook" | "Drive Left" | "Drive Right":#| "Layup":#| "Back Down":
                team.ballHandler.dribbleChain.clear()
                team.currentChoice = choice
                self.makeOptions(otherTeamNum, False, None, choice)
            case "Pump Fake" | "Pass Fake":
                team.ballHandler.dribbleChain.clear()
                oRtg = team.ballHandler.basicRatings["Offensive IQ"] # if i ever do multiplayer ill need to do something about this being team1 instead of like a general team variable. think i figured it out
                total = oRtg + otherTeam.onBallDefender.basicRatings["Defensive IQ"]
                c = round((oRtg/total) * 100)
                result = self.determineSuccess(c)
                if result:
                    if self.realPlayers == 1 and otherTeam == self.team2:
                        self.team2.onBallDefender.hasBeenPumpFaked = True
                        
                    team.ballHandler.pumpFaking = True
                    if choice == "Pump Fake":
                        if team.ballHandler.location in spots[0:13]:
                            if not team.ballHandler.postingUp:
                                newChoice = "Shoot" # have to specifically return this to react
                            else:
                                newChoice = "Post Fade"
                        elif team.ballHandler.location in spots[13:]:
                            if not team.ballHandler.postingUp:
                                newChoice = "Layup" # have to specifically return this to react
                            else:
                                newChoice = "Post Hook"
                        team.currentChoice = newChoice
                        
                    elif choice == "Pass Fake":
                        newChoice = "Pass"
                        team.currentChoice = newChoice
                        print("CPU is passing")
                else:
                    team.ballHandler.pumpFaking = False
                    newChoice = choice
                    team.currentChoice = newChoice
                    print("Clearly faking a shot or pass")
                self.makeOptions(otherTeamNum, False, None, newChoice)
            case "Stop Drive":
                team.ballHandler.midDrive = False
                self.makeOptions(teamNum)
            case "Post Up":
                team.ballHandler.dribbleChain.clear()
                team.ballHandler.postingUp = True
                self.makeOptions(teamNum)
            case "Exit Post":
                team.ballHandler.dribbleChain.clear()
                team.ballHandler.postingUp = False
                self.makeOptions(teamNum)


            case p if p in self.passingOptions: # for passing. it will be in the format f"{option.name} (at {option.location})" so this needs some fixing
                self.targetPlayer = team.playerDict[p]  
                self.passingOptions.clear()
                team.currentChoice = self.tempChoiceHold
                self.tempChoiceHold = ""
                
                if team.currentChoice == "Double Team":
                    otherTeam.ballHandler.doubled = True
                    self.targetPlayer.location = otherTeam.ballHandler.location
                    playerNum = int(self.targetPlayer.playerNum)
                    openPlayerIndex = otherTeam.players[playerNum].defendedBy
                    openPlayer = otherTeam.players[openPlayerIndex]
                    openPlayer.wideOpen = True
                    print(f"{openPlayer.name} is wide open at {openPlayer.location}.")
                    
                    self.makeOptions(otherTeamNum)
                elif team.currentChoice == "Teammate Cut":
                    cutDefendingPlayerIndex = self.targetPlayer.defendedBy
                    cutDefendingPlayer = otherTeam.players[cutDefendingPlayerIndex]
                    
                    if self.targetPlayer.wideOpen:
                        defensiveAction = "Watch"
                    else:
                        defensiveAction = "Stay on Defense"

                        
                    self.chanceCalc("Teammate Cut", defensiveAction, self.targetPlayer, cutDefendingPlayer, teamNum, otherTeamNum)
                    
                else:    
                    self.makeOptions(otherTeamNum, False, None, team.currentChoice)
                    
                    
            case d if d in ["Stepback", "Crossover", "Between Legs", "Behind the back", "Shimmy", "Hesitation", "Spin", "Hopstep"]: 
                team.ballHandler.dribbled = True
                team.ballHandler.dribbleChain.append(d)
                team.currentChoice = "Dribble" 
                self.makeOptions(otherTeamNum, False, None, "Dribble")
            case s if s in spots: #move/back-out and drive once you got through defender
                team.ballHandler.dribbled = True
                team.ballHandler.dribbleChain.clear() 
                team.ballHandler.location = choice
                otherTeam.onBallDefender.location = choice
                if self.tempChoiceHold == "Drive":
                    team.ballHandler.midDrive = True
                    print(f"Drove to {choice}.")
                else:
                    print(f"Moved to {choice}")
                self.tempChoiceHold = ""
                self.makeOptions(teamNum)
                
            # defense
            case "Recover":
                team.onBallDefender.energyUsed += 30
                chance = team.onBallDefender.basicRatings["Hustle"] * .6 + team.onBallDefender.basicRatings["Interior D"] * .15 + team.onBallDefender.basicRatings["Perimeter D"] *.15 + team.onBallDefender.basicRatings["Defensive IQ"] * .1
                result = self.determineSuccess(chance)
                if result:
                    team.onBallDefender.energyUsed += 5
                    team.onBallDefender.ankleBroken = False
                    team.onBallDefender.faltered = True
                    self.makeOptions(teamNum)
                else:
                    team.onBallDefender.energyUsed += 10
                    team.currentChoice = "Give Up"
                    # team.onBallDefender.ankleBroken = True # stays true, js put ts here so you know
                    self.chanceCalc(otherTeam.currentChoice, team.currentChoice, otherTeam.ballHandler, team.onBallDefender, otherTeamNum, teamNum)
            case "Late Contest" | "Get Back on Defense":
                team.onBallDefender.energyUsed += 15
                chance = team.onBallDefender.basicRatings["Hustle"]
                result = self.determineSuccess(chance)
                if result:
                    otherTeam.ballHandler.wideOpen = False
                    if choice == "Late Contest":
                        team.onBallDefender.location = otherTeam.ballHandler.location
                        team.currentChoice = "Contest"
                    else:
                        team.currentChoice = "Stay on Defense"
                else:
                    team.currentChoice = "Give Up"
                for player in otherTeam.players:
                    player.doubled = False
                self.chanceCalc(otherTeam.currentChoice, team.currentChoice, otherTeam.ballHandler, team.onBallDefender, otherTeamNum, teamNum)
            case "Single Coverage":
                for player in otherTeam.players:
                    player.doubled = False
                self.makeOptions(otherTeamNum)
            case "Double Team":# | "Position for Rebound": #this is if i want to make rebounding another choice thing. basically the ball can bounce wherever and you try to predict that. sounds like too much work tbh. yah nah
                self.tempChoiceHold = choice
                self.makeOptions(teamNum, True, choice)
            case "Contest" | "Stand Ground" | "Position for Rebound" | "Verticality" | "Block" | "Steal" | "Stay on Defense" | "Go Over" | "Go Under" | "Switch" | "Give Up":
                team.currentChoice = choice
                self.chanceCalc(otherTeam.currentChoice, team.currentChoice, otherTeam.ballHandler, team.onBallDefender, otherTeamNum, teamNum)
        
    
    # maybe run plays: iso clear out, teammate get open for 3?      
    
    # successful back down just gives a boost in the next shot attempt? i was gonna make it take you to center paint since the option is only there 
    # for inside paint but remembered I removed that spot.
    # maybe ill change it to bump. bump a couple times for separation and shoot with a bonus if it was successful. either that or its gone.
            
    def determineSuccess(self, chance):
        success = randint(1,100)
        if success < chance:
            return True
        else: 
            return False        
            
    def endGame(self):
        if self.statObj.score[0] == self.statObj.endScore or self.statObj.score[1] == self.statObj.endScore:
            if self.statObj.score[0] > self.statObj.score[1]:
                print(f"You won with a score of {self.statObj.score[0]} to {self.statObj.score[1]}") #replace with UI
            else:
                print(f"You lost with a score of {self.statObj.score[0]} to {self.statObj.score[1]}") #replace with UI
            #prompt replay or exit using UI
            # self.recentActions.clear()
            
    def run(self):
        self.startPossession()
        while True:
            i = int(input("Choose: "))
            self.handleInput(self.tempOptions[i])
            
            
class Stats:
    def __init__(self, team1, team2, endScore = 21):
        self.team1, self.team2 = team1, team2
        
        self.score = [0, 0]
        self.endScore = endScore
        
        self.assists = [0, 0]
        self.rebounds = [0, 0]
        self.steals = [0, 0]
        self.blocks = [0, 0]
        self.turnovers = [0, 0]
        
        self.fga = [0, 0]
        self.fgm = [0, 0]
        self.three_fga = [0, 0]
        self.three_fgm = [0, 0]
        
        self.fts = [0, 0]
        self.fouls = [0, 0]
        
        
    def addScore(self, teamNum, amount):
        self.score[teamNum] += amount
        print(self.score)
        
    # def addToOtherStat(self, teamNum, stat):
    #     match stat:
    #         case "Assist":
    #             self.assists[teamNum] += 1
    #         case "Rebounds":
    #             self.rebounds[teamNum] += 1
    #         case "Steals":
    #             self.steals[teamNum] += 1
    #         case "Blocks":
    #             self.blocks[teamNum] += 1
    #         case "Turnovers":
    #             self.turnovers[teamNum] += 1
    #         case "FGA":
    #             self.fga[teamNum] += 1
    #         case "FGM":
    #             self.fgm[teamNum] += 1
    #         case "3FGA":
    #             self.three_fga[teamNum] += 1
    #         case "3FGM":
    #             self.three_fgm[teamNum] += 1
    #         case "FTS":
    #             self.fts[teamNum] += 1
    #         case "Fouls":
    #             self.fouls[teamNum] += 1
                