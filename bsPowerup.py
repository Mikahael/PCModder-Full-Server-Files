import bs
import random
import bsUtils 
import bsInternal
import don
import SnoBallz
from bsSpaz import *
import bsSomething

'''
Done by PC231392 / PCModder / PC290717
Full scripts shared to the world.
Do use it well and enjoy it well.
If possible, kindly do give credit to me.
Thanks to all.
100%
'''

defaultPowerupInterval = 8000
gSettingsEnabled = hasattr(bs, "get_settings")

class PowerupMessage(object):    
    def __init__(self,powerupType,sourceNode=bs.Node(None)):
        
        self.powerupType = powerupType
        self.sourceNode = sourceNode

class PowerupAcceptMessage(object):
    """
    category: Message Classes

    Inform a bs.Powerup that it was accepted.
    This is generally sent in response to a bs.PowerupMessage
    to inform the box (or whoever granted it) that it can go away.
    """
    pass

class _TouchedMessage(object):
    pass

class PowerupFactory(object):
    def __init__(self):
        self._lastPowerupType = None

        self.model = bs.getModel("powerup")
        self.modelSimple = bs.getModel("powerupSimple")

        self.texBomb = bs.getTexture("powerupBomb")
        self.texJumpingBomb = bs.getTexture("eggTex3")
        self.texPunch = bs.getTexture("powerupPunch")
        self.texYellowShield = bs.getTexture("coin") 
        self.texKillLaKillBomb = bs.getTexture("black")
        self.texPoisonBomb = bs.getTexture("black")
        self.texSpeedPunch = bs.getTexture("achievementSuperPunch") 
        self.texPandoraBox = bs.getTexture("black")
        self.texMultiBombs = bs.getTexture("logo") 
        self.texFireworkBomb = bs.getTexture("eggTex1") 
        self.texIceBombs = bs.getTexture("powerupIceBombs")
        self.texStickyBombs = bs.getTexture("powerupStickyBombs")
        self.texTpBombs = bs.getTexture("bombStickyColor")
        self.texShield = bs.getTexture("powerupShield")
        self.texImpactBombs = bs.getTexture("powerupImpactBombs")
        self.texHealth = bs.getTexture("powerupHealth")
        self.texLandMines = bs.getTexture("powerupLandMines")
        self.LandMinesModel = bs.getModel("frostyPelvis")
        self.texCurse = bs.getTexture("powerupCurse")
        self.texBalls = bs.getTexture("achievementOutline")
        self.texUnb = bs.getTexture("puckColor")
        self.texDirt = bs.getTexture('nub')
        #beggining of my powerups!!!;-;
        self.texSpeed = bs.getTexture("powerupSpeed")
        self.texAlan = bs.getTexture("agentIconColorMask")
        self.texRDM = bs.getTexture("logo")
        self.RandomCharacter = bs.getTexture("touchArrowsActions")
        self.Troll = bs.getTexture("star")
        self.texmj = bs.getTexture("agentIconColorMask")
        self.texMotion = bs.getTexture("usersButton")
        self.texInvisibility = bs.getTexture("cyborgIcon")
        self.texHiJump = bs.getTexture("buttonJump")
        self.texBallon = bs.getTexture('nextLevelIcon')
        self.texBlock = bs.getTexture('flagColor')
        self.texBox = bs.getTexture('achievementTNT')
        self.texiceImpact = bs.getTexture('bombColorIce')
        self.texGoldenBomb = bs.getTexture('bombColor')
        self.textbomb = bs.getTexture("buttonBomb")
        self.texgluebomb = bs.getTexture("eggTex2")
        self.texweedbomb = bs.getTexture("gameCenterIcon")
        self.texBot = bs.getTexture("achievementFreeLoader")
        self.texFloatingMine = bs.getTexture('achievementMine')
        self.texTouchMe = bs.getTexture('shield')
        self.texcelebrate = bs.getTexture("neoSpazIconColorMask")
        self.texRadius = bs.getTexture("night")
        self.texSleep = bs.getTexture("powerupSleep")
        self.texNight = bs.getTexture("shield")
        self.texSpazBomb = bs.getTexture("neoSpazIcon")
        self.texcurseBomb = bs.getTexture("powerupCurse")
        self.texhealBomb = bs.getTexture("night")
        self.texNightBomb = bs.getTexture("shield")
        self.texknockBomb = bs.getTexture("medalGold")
        self.texspeedBomb = bs.getTexture("achievementGotTheMoves")
        self.texcharacterBomb = bs.getTexture("chestOpenIcon")
        self.texmjBomb = bs.getTexture("menuButton")
        self.textrioBomb = bs.getTexture("star")
        self.texstickyIce = bs.getTexture("crossOutMask")
        self.texstickyIceTrio = bs.getTexture("egg4")
        self.texstickyIceMess = bs.getTexture("gameCenterIcon")
        self.teximpactMess = bs.getTexture("heart")
        self.texStickyMess = bs.getTexture("powerupStickyBombs")
        self.texIcyMess = bs.getTexture("night")
        self.texicyTrio = bs.getTexture("gameCircleIcon")
        self.texWeee = bs.getTexture("night")
        self.texboomBomb = bs.getTexture("achievementOffYouGo")
        self.texTnt = bs.getTexture("tnt")
        self.texName = bs.getTexture("achievementEmpty")
        self.texHighlight = bs.getTexture("tv")
        self.texSpotlight = bs.getTexture("black")
        self.texjumpFly = bs.getTexture("achievementOffYouGo")
        self.texblastBomb = bs.getTexture("achievementCrossHair")
        self.texrevengeBomb = bs.getTexture("achievementOutline")
        self.texSno = bs.getTexture("bunnyColor")
        self.snoModel = bs.getModel("frostyPelvis")
        self.texuse = bs.getTexture("achievementOutline")
        self.texBlackHole = bs.getTexture("circleOutlineNoAlpha")
        self.texSlippery = bs.getTexture("settingsIcon")
        self.texAntiGrav = bs.getTexture("achievementFootballShutout")

        self.healthPowerupSound = bs.getSound("healthPowerup")
        self.powerupSound = bs.getSound("ooh")
        self.powerdownSound = bs.getSound("pixie2")
        self.dropSound = bs.getSound("boxDrop")

        # material for powerups
        self.powerupMaterial = bs.Material()

        # material for anyone wanting to accept powerups
        self.powerupAcceptMaterial = bs.Material()

        # pass a powerup-touched message to applicable stuff
        self.powerupMaterial.addActions(
            conditions=(("theyHaveMaterial",self.powerupAcceptMaterial)),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("message","ourNode","atConnect",_TouchedMessage())))

        # we dont wanna be picked up
        self.powerupMaterial.addActions(
            conditions=("theyHaveMaterial",
                        bs.getSharedObject('pickupMaterial')),
            actions=( ("modifyPartCollision","collide",True)))

        self.powerupMaterial.addActions(
            conditions=("theyHaveMaterial",
                        bs.getSharedObject('footingMaterial')),
            actions=(("impactSound",self.dropSound,0.5,0.1)))

        self._powerupDist = []
        for p,freq in getDefaultPowerupDistribution():
            for i in range(int(freq)):
                self._powerupDist.append(p)

    def getRandomPowerupType(self,forceType=None,excludeTypes=[]):
        """
        Returns a random powerup type (string).
        See bs.Powerup.powerupType for available type values.

        There are certain non-random aspects to this; a 'curse' powerup,
        for instance, is always followed by a 'health' powerup (to keep things
        interesting). Passing 'forceType' forces a given returned type while
        still properly interacting with the non-random aspects of the system
        (ie: forcing a 'curse' powerup will result
        in the next powerup being health).
        """
        t = None
        if forceType: t = forceType
        else:
            if self._lastPowerupType == 'curse': t = 'health'
            else:
                while True:
                    if len(self._powerupDist) > 0:
                        t = self._powerupDist[
                            random.randint(0, len(self._powerupDist)-1)]
                        if t not in excludeTypes:
                            break
                    else: break
        self._lastPowerupType = t if t is not None else "health"
        return t if t is not None else 'pass'

def getDefaultPowerupDistribution(all=False):
    if gSettingsEnabled: settings = bs.get_settings()
    else: settings = {}
    powerups_all = {'tripleBombs': 3, 
                    'iceBombs': 3, 
                    'punch': 3, 
                    'impactBombs': 2, 
                    'shield': 2, 
                    'landMines': 2,
                    'stickyBombs': 3, 
                    'health': 2, 
                    'curse': 1, 
                    'yellowShield': 1, 
                    'speedPunch': 1, 
                    'fireworkBombs': 2, 
                    'killLaKillBombs': 2,
                    'jumpingBombs': 1, 
                    'tpBombs': 1,
                    'poisonBombs': 0, #does not work, am too lazy to fix it
                    'pandoraBox': 1, 
                    'unbreakable': 1, 
                    'dirtBombs': 1,
                    'speed': 1,  #new powerup start
                    'alan': 2,
                    'rdm': 2,
                    'randomCharacter': 1,
                    'troll': 2,
                    'mj': 2,
                    'impactMess': 2,
                    'Motion': 2,
                    'invisibility': 2,
                    'hijump': 2,
                    'ballon': 2,
                    'BlockPowerup': 1,
                    'iceImpact': 2,
                    'goldenBomb': 2,
                    'tbomb': 2,
                    'weedbomb': 2,
                    'gluebomb': 2,
                    'bot': 2,
                    'celebrate': 2,
                    'FloatingMine': 2,
                    'TouchMe': 2,
                    'radius': 2,
                    'sleep': 2,
                    'night': 2,
                    'spazBomb': 2,
                    'curseBomb': 2,
                    'healBomb': 2,
                    'nightBomb': 2,
                    'revengeBomb': 2,
                    'blastBomb': 2,
                    'knockBomb': 2,
                    'speedBomb': 2,#shockwave actually.
                    'characterBomb': 2,
                    'mjBomb': 2,
                    'trioBomb': 2,
                    'stickyIce': 2,
                    'stickyIceTrio': 2,
                    'stickyIceMess': 2,
                    'stickyMess': 2,
                    'icyMess': 2,
                    'icyTrio': 2,
                    'weee': 2,
                    'tnt': 2,
                    'use': 2,
                    'name': 0,#a bug so no enable
                    'highlight': 2,
                    'spotlight': 0,#dont turn on xd
                    'boomBomb': 2,
                    'jumpFly': 2,
                    'snoball': 2,
                    'antiGrav': 2,
                    'BlackHole': 2,
                    'Box': 2,
                    'Slippery': 2,
                    'multiBombs': 1}
    exclude_powerups = settings.get("exclude_powerups", [])
    active_powerups = powerups_all.keys()
    if not all:
        if settings.get("disable_powerups", False): active_powerups = []
        elif len(exclude_powerups) > 0: active_powerups = [i for i in powerups_all if i not in exclude_powerups]
    return tuple([(i) if i[0] in active_powerups else (i[0], 0) for i in powerups_all.items()])

class Powerup(bs.Actor):
    def __init__(self,position=(0,1,0), powerupType='tripleBombs', expire=True):
        
        bs.Actor.__init__(self)
        factory = self.getFactory()

        if gSettingsEnabled: settings = bs.get_settings()
        else: settings = {}

        self.powerupType = powerupType;
        self._powersGiven = False
        if powerupType == 'tripleBombs': tex = factory.texBomb; name = 'TripleBombs'
        elif powerupType == 'multiBombs': tex = factory.texMultiBombs; name = 'MultiBombs'
        elif powerupType == 'punch': tex = factory.texPunch; name = 'Gloves'
        elif powerupType == 'speedPunch':tex = factory.texSpeedPunch; name = 'Gloves 2.0'
        elif powerupType == 'fireworkBombs':tex = factory.texFireworkBomb; name = 'FireWorks'
        elif powerupType == 'killLaKillBombs': tex = factory.texKillLaKillBomb; name = 'KillAll'
        elif powerupType == 'poisonBombs': tex = factory.texPoisonBomb; name = 'PoisonBomb'
        elif powerupType == 'pandoraBox': tex = factory.texPandoraBox; name = 'PandoraBox'
        elif powerupType == 'yellowShield': tex = factory.texYellowShield; name = 'YellowShield'
        elif powerupType == 'jumpingBombs': tex = factory.texJumpingBomb; name = 'JumpingBomb'
        elif powerupType == 'tpBombs': tex = factory.texTpBombs; name = 'TPBomb'
        elif powerupType == 'iceBombs': tex = factory.texIceBombs; name = 'IcyBombs'
        elif powerupType == 'impactBombs': tex = factory.texImpactBombs; name = 'ImpactBombs'
        elif powerupType == 'landMines': tex = factory.texLandMines; name = 'LandMines'
        elif powerupType == 'stickyBombs': tex = factory.texStickyBombs; name = 'StickyBombs'
        elif powerupType == 'shield': tex = factory.texShield; name = 'Bubble'
        elif powerupType == 'health': tex = factory.texHealth; name = 'Health'
        elif powerupType == 'curse': tex = factory.texCurse; name = 'Pls Touch Me'
        elif powerupType == 'unbreakable': tex = factory.texUnb; name = 'Unbreakable'
        elif powerupType == 'dirtBombs': tex = factory.texDirt; name = 'DirtBomb'
        elif powerupType == 'speed': tex = factory.texSpeed # new powerups begin
        elif powerupType == 'alan': tex = factory.texAlan; name = 'Boss'
        elif powerupType == 'rdm': tex = factory.texRDM; name = 'RandomBomb'
        elif powerupType == 'randomCharacter': tex = factory.RandomCharacter; name = 'Random Char'
        elif powerupType == 'troll': tex = factory.Troll; name = 'FunPack'
        elif powerupType == 'mj': tex = factory.texmj; name = 'MJ'
        elif powerupType == 'impactMess': tex = factory.teximpactMess; name = 'ImpactMess'
        elif powerupType == 'Motion': tex = factory.texMotion; name = 'Motion'
        elif powerupType == 'invisibility': tex = factory.texInvisibility; name = 'Invisibile'
        elif powerupType == 'hijump': tex = factory.texHiJump; name = 'Hi-Jump'
        elif powerupType == 'ballon': tex = factory.texBallon; name = 'Ballon'
        elif powerupType == 'BlockPowerup': tex = factory.texBlock; name = 'Block'
        elif powerupType == 'iceImpact': tex = factory.texiceImpact; name = 'IceImpact'
        elif powerupType == 'goldenBomb': tex = factory.texGoldenBomb; name = 'BlastyBomb'
        elif powerupType == 'tbomb': tex = factory.textbomb; name = 'TBomb'
        elif powerupType == 'gluebomb': tex = factory.texgluebomb; name = 'Broken Glue'
        elif powerupType == 'weedbomb': tex = factory.texweedbomb; name = 'WeedBomb'
        elif powerupType == 'bot': tex = factory.texBot; name = 'Buddy Bot'
        elif powerupType == 'celebrate': tex = factory.texcelebrate; name = 'Celebrate'
        elif powerupType == 'FloatingMine': tex = factory.texFloatingMine; name = 'LandMines'
        elif powerupType == 'TouchMe': tex = factory.texTouchMe; name = 'TouchMe'
        elif powerupType == 'radius': tex = factory.texRadius; name = 'Radius'
        elif powerupType == 'sleep': tex = factory.texSleep; name = 'Sleepy'
        elif powerupType == 'night': tex = factory.texNight; name = 'NiteNite'
        elif powerupType == 'spazBomb': tex = factory.texSpazBomb; name = 'SpazBomb'
        elif powerupType == 'curseBomb': tex = factory.texcurseBomb; name = 'CurseBomb'
        elif powerupType == 'characterBomb': tex = factory.texcharacterBomb; name = 'CharBomb'
        elif powerupType == 'mjBomb': tex = factory.texmjBomb; name = 'MJBomb'
        elif powerupType == 'trioBomb': tex = factory.textrioBomb; name = 'ImpactTrio'
        elif powerupType == 'speedBomb': tex = factory.texspeedBomb; name = 'ShockWave'
        elif powerupType == 'healBomb': tex = factory.texhealBomb; name = 'HealthBomb'
        elif powerupType == 'nightBomb': tex = factory.texNightBomb; name = 'AtomBomb'
        elif powerupType == 'revengeBomb': tex = factory.texrevengeBomb; name = 'RevengeBomb'
        elif powerupType == 'blastBomb': tex = factory.texblastBomb; name = 'blastBomb'
        elif powerupType == 'knockBomb': tex = factory.texknockBomb; name = 'KnockBomb'
        elif powerupType == 'stickyIce': tex = factory.texstickyIce; name = 'StickyIce'
        elif powerupType == 'stickyIceTrio': tex = factory.texstickyIceTrio; name = 'StickyIceTrio'
        elif powerupType == 'stickyIceMess': tex = factory.texstickyIceMess; name = 'StickyIceMess'
        elif powerupType == 'stickyMess': tex = factory.texStickyMess; name = 'StickyMess'
        elif powerupType == 'icyMess': tex = factory.texIcyMess; name = 'IcyMess'
        elif powerupType == 'icyTrio': tex = factory.texicyTrio; name = 'IcyTrio'
        elif powerupType == 'weee': tex = factory.texWeee; name = 'Health'
        elif powerupType == 'tnt': tex = factory.texTnt; name = 'TNT'
        elif powerupType == 'boomBomb': tex = factory.texboomBomb; name = 'KaboomBomb'
        elif powerupType == 'name': tex = factory.texName; name = 'NewName'
        elif powerupType == 'highlight': tex = factory.texHighlight; name = 'HighLight'
        elif powerupType == 'spotlight': tex = factory.texSpotlight; name = 'Spotlight'
        elif powerupType == 'jumpFly': tex = factory.texjumpFly; name = 'FlyJump'
        elif powerupType == 'use': tex = factory.texuse; name = 'FlyBomb'
        elif powerupType == "antiGrav": tex = factory.texAntiGrav; name = 'AntiGrav'
        elif powerupType == "BlackHole": tex = factory.texBlackHole; name = 'BlackHole'
        elif powerupType == "Slippery": tex = factory.texSlippery; name = 'LuckyBlock'
        elif powerupType == "Box": tex = factory.texBox; name = 'Box'
        elif powerupType == 'snoball':
            tex = factory.texSno
            mod = factory.snoModel
            name = "shieldBall"
        elif powerupType == 'pass': return
        else: raise Exception("invalid powerupType: "+str(powerupType))

        if len(position) != 3: raise Exception("expected 3 floats for position")
        
        if powerupType == 'poisonBombs':
            refScale = (0,3,0)
            ref = 'soft'
        elif powerupType == 'pandoraBox':
            ref = 'soft'
            refScale = (1,1,1)
        elif powerupType == 'dirtBombs':
            ref = 'soft'
            refScale = (1, 0.4, 0.16)
        else:
            refScale = [0.95]
            ref = 'powerup'
        self.node = bs.newNode('prop',
            delegate=self,
            attrs={'body':'box',
                   'position':position,
                   'model':factory.model,
                   'lightModel':factory.modelSimple,
                   'shadowSize':0.48,
                   'colorTexture':tex,
                   'reflection':ref,
                   'reflectionScale':refScale,
                   'materials':(factory.powerupMaterial, bs.getSharedObject('objectMaterial'))})
        prefixAnim = {0: (1, 0, 0), 250: (1, 1, 0), 250 * 2: (0, 1, 0), 250 * 3: (0, 1, 1), 250 * 4: (1, 0, 1),
                      250 * 5: (0, 0, 1), 250 * 6: (1, 0, 0)}
        color = (0,0,1)
                   
        if don.powerupName:
            m = bs.newNode('math', owner=self.node, attrs={'input1': (0, 0.7, 0), 'operation': 'add'})
            self.node.connectAttr('position', m, 'input2')
            self.nodeText = bs.newNode('text',
                                       owner=self.node,
                                       attrs={'text': str(name),
                                              'inWorld': True,
                                              'shadow': 1.0,
                                              'flatness': 1.0,
                                              'color': color,
                                              'scale': 0.0,
                                              'hAlign': 'center'})
            m.connectAttr('output', self.nodeText, 'position')
            bs.animate(self.nodeText, 'scale', {0: 0, 140: 0.016, 200: 0.01})
            bs.animateArray(self.nodeText,'color',3,{0:(0,0,2),500:(0,2,0),1000:(2,0,0),1500:(2,2,0),2000:(2,0,2),2500:(0,1,6),3000:(1,2,0)},True)
            bs.emitBGDynamics(position=self.nodeText.position, velocity=self.node.position, count=200, scale=1.4, spread=2.01, chunkType='sweat')
                                
        if don.shieldOnPowerUps:
            self.nodeShield = bs.newNode('shield', owner=self.node, attrs={'color': color,
                                                                           'position': (
                                                                               self.node.position[0],
                                                                               self.node.position[1],
                                                                               self.node.position[2] + 0.5),
                                                                           'radius': 1.2})
            self.node.connectAttr('position', self.nodeShield, 'position')
            bsUtils.animateArray(self.nodeShield, 'color', 3, prefixAnim, True)
            
        if don.discoLights:
            self.nodeLight = bs.newNode('light',
                                        attrs={'position': self.node.position,
                                               'color': color,
                                               'radius': 0.2,
                                               'volumeIntensityScale': 0.5})
            self.node.connectAttr('position', self.nodeLight, 'position') 
            bsUtils.animateArray(self.nodeLight, 'color', 3, prefixAnim, True)
            bs.animate(self.nodeLight, "intensity", {0:1.0, 1000:1.8, 2000:1.0}, loop = True)
            bs.gameTimer(8000,self.nodeLight.delete)  
            
        if don.powerupTimer:
            self.powerupHurt = bs.newNode('shield', owner=self.node, attrs={'color':(1,1,1), 'radius':0.1, 'hurt':1, 'alwaysShowHealthBar':True})
            self.node.connectAttr('position',self.powerupHurt, 'position')
            bs.animate(self.powerupHurt, 'hurt', {0:0, defaultPowerupInterval-1000:1})
        bs.gameTimer(defaultPowerupInterval-1000, bs.Call(self.do_delete))
        
        curve = bs.animate(self.node,"modelScale",{0:0,140:1.6,200:1})
        bs.gameTimer(200, curve.delete)

        if expire:
            bs.gameTimer(defaultPowerupInterval-2500,
                         bs.WeakCall(self._startFlashing))
            bs.gameTimer(defaultPowerupInterval-1000,
                         bs.WeakCall(self.handleMessage, bs.DieMessage()))

    @classmethod
    def getFactory(cls):
        activity = bs.getActivity()
        if activity is None: raise Exception("no current activity")
        try: return activity._sharedPowerupFactory
        except Exception:
            f = activity._sharedPowerupFactory = PowerupFactory()
            return f

    def _startFlashing(self):
        if self.node.exists(): 
            self.node.flashing = True

    def do_delete(self):
        if self.node is not None and self.node.exists():
            if hasattr(self, "light") and self.light.exists(): 
                bs.animate(self.light, "radius", {0:0.078, 100:0})
                bs.gameTimer(100, self.light.delete)
            if hasattr(self, "powerupHurt") and self.powerupHurt.exists():
                bs.gameTimer(100, self.powerupHurt.delete)
                bs.gameTimer(100,self.nodeLight.delete)
        
    def handleMessage(self, msg):
        self._handleMessageSanityCheck()

        if isinstance(msg, PowerupAcceptMessage):
            factory = self.getFactory()
            if self.powerupType == 'health':
                bs.playSound(factory.healthPowerupSound, 3,
                             position=self.node.position)
            bs.playSound(factory.powerupSound, 3, position=self.node.position)
            self._powersGiven = True
            self.handleMessage(bs.DieMessage())

        elif isinstance(msg, _TouchedMessage):
            if not self._powersGiven:
                node = bs.getCollisionInfo("opposingNode")
                if node is not None and node.exists():
                    bs.gameTimer(100,self.nodeLight.delete)
                    if self.powerupType == 'snoball':
                        spaz = node.getDelegate()
                        SnoBallz.snoBall().getFactory().giveBallz(spaz)
                        self._powersGiven = True
                        self.handleMessage(bs.DieMessage())
                    elif self.powerupType == 'TouchMe':
                        p = node.positionForward
                        self._powersGiven = True
                        self.handleMessage(bs.DieMessage())
                        bsSomething.Something((p[0],p[1]+2,p[2])).autoRetain()  
                    elif self.powerupType == 'BlackHole':
                        p = node.positionForward
                        self._powersGiven = True
                        self.handleMessage(bs.DieMessage())
                        bsSomething.BlackHole((p[0],p[1]+2,p[2])).autoRetain()  
                    elif self.powerupType == 'Slippery':
                        p = node.positionForward
                        self._powersGiven = True
                        self.handleMessage(bs.DieMessage())
                        bsSomething.MagicSpell((p[0],p[1]+2,p[2])).autoRetain()  
                    elif self.powerupType == 'Box':
                        self._powersGiven = True
                        self.handleMessage(bs.DieMessage())
                        node.handleMessage(bs.PowerupMessage(powerupType = 'Box'))
                    else:
                        node.handleMessage(PowerupMessage(self.powerupType, sourceNode=self.node))

        elif isinstance(msg, bs.DieMessage):
            if self.node.exists():
                if (msg.immediate): self.node.delete()
                else:
                    curve = bs.animate(self.node, "modelScale", {0:1,100:0})
                    bs.gameTimer(100, self.node.delete)

        elif isinstance(msg ,bs.OutOfBoundsMessage):
            self.handleMessage(bs.DieMessage())

        elif isinstance(msg, bs.HitMessage):
            if msg.hitType == 'punch':
                if self.powerupType == 'curse':
                    bs.Blast(position=self.node.position, velocity=(0,0,0), blastRadius=1,blastType="normal", sourcePlayer=None, hitType='explosion',hitSubType='normal').autoRetain()
                    self.handleMessage(bs.DieMessage())
                elif self.powerupType == 'health':
                    bs.Blast(position=self.node.position, velocity=(0,0,0), blastRadius=1,blastType="normal", sourcePlayer=None, hitType='explosion',hitSubType='normal').autoRetain()
                    self.handleMessage(bs.DieMessage())
            else:
                self.handleMessage(bs.DieMessage())
        else:
            bs.Actor.handleMessage(self, msg)
