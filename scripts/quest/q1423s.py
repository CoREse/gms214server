# 1423 - [Job Adv] (Lv.30) Path of the Bandit

darkMarble = 4031013
job = "Bandit"
monster = "Swamp Monster"

sm.setSpeakerID(1052001) # Dark Lord
sm.sendNext("You wish to become a #b"+ job +"#k?\r\n\r\n"
            "A #b"+ job +"#k is specialised in short range attacks and use #bdaggers#k to defeat their enemies."
            "There are many useful skills you can acquire.")

# start of custom
response = sm.sendAskYesNo("Are you sure you wish to become a #b" + job + "#k?")

if response:
    sm.completeQuestNoRewards(parentID)
    sm.jobAdvance(420) # Bandit
    sm.sendSayOkay("Alright! You have now become a #b" + job + "!")
else:
    sm.sendSayOkay("Speak to me again and I can explain the two paths to you once more.")

sm.dispose()
# end of custom

# sm.sendNext("Before I teach you the ways of the "+ job +", you will have to accomplish a very difficult test. "
#                                                         "I will warp you into a special map, in which I require you to defeat #b"+ monster +"#k "
#                                                         "and return 30 #i"+ str(darkMarble) +"##z"+ str(darkMarble) +"#s to me.")
#
# response = sm.sendAskYesNo("Once you enter the map, you #rcannot#k return without the #b#t"+ str(darkMarble) +"#s#k, if you die you will lose your experience.\r\n"
#                                                                                                    "Are you ready?")
#
# if response:
#     sm.warp(910370000, 0) # Thief Test Site
#     sm.startQuestNoCheck(parentID)
# else:
#     sm.sendSayOkay("You cannot be a Rogue forever. You #bwill#k have to face up to the test.\r\n"
#                    "Talk to me when you are ready.")
# sm.dispose()
