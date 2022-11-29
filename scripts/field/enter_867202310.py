# id 867202310 (Abrup Basin : Skuas), field 867202310
sm.lockInGameUI(True, False)
sm.forcedFlip(True)
sm.spawnNpc(9400580, 640, -240)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400582, 600, -220)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face4#If the Fembris have been seen at the edge of Windsleep Forest... ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#We should prepare for an attack. ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face4#But we have no idea how much time we have! ")
sm.setParam(57)
sm.sendSay("#bThen we need to assume we have no time. ")
sm.setParam(37)
sm.sendSay("#face0#The ballistas have been completed, and we're finishing up on the catapults. They should be ready... soon. ")
sm.setParam(57)
sm.sendSay("#bWeapons like that will be a huge help. ")
sm.setParam(37)
sm.sendSay("#face0#The biggest task left is to finish repairing the walls.")
sm.forcedFlip(True)
sm.sendDelay(300)
sm.forcedMove(False, 100)
sm.moveNpcByTemplateId(9400580, False, 60, 70)
sm.moveNpcByTemplateId(9400582, False, 60, 70)
sm.sendDelay(900)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.spawnNpc(9400580, 1380, -520)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400582, 1340, -520)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.spawnNpc(9400600, 1560, -530)
sm.showNpcSpecialActionByTemplateId(9400600, "summon", 0)
sm.spawnNpc(9400604, 1650, -530)
sm.showNpcSpecialActionByTemplateId(9400604, "summon", 0)
sm.spawnNpc(9400604, 1720, -530)
sm.showNpcSpecialActionByTemplateId(9400604, "summon", 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.sendDelay(500)
sm.flipNpcByTemplateId(9400600, True)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400600, True, 50, 50)
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendNext("Ah, #h0#. Back from the friendly hunt with Chief Gurnardson and the lot? How did you fare? ")
sm.setParam(57)
sm.sendSay("#bJust fine. We gathered plenty of meat, enough that we shouldn't have to worry for awhile. ")
sm.setParam(37)
sm.sendSay("Glad to hear it! ")
sm.setParam(57)
sm.sendSay("#bHowever... ")
sm.setParam(37)
sm.sendSay("I don't like the sound of that... ")
sm.sendDelay(1000)
sm.setParam(57)
sm.sendNext("#bOn our way back, we found some Fembris at the edge of the forest. We're concerned that might mean... ")
sm.setParam(37)
sm.sendSay("...That an attack is coming. ")
sm.setParam(57)
sm.sendSay("#bYes. It could mean we don't have much time left. ")
sm.sendSay("#bThe monsters that hit Kaptafel seemed to be led by the Fembris. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#The same thing happened at Svarti. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Then we'd best hurry. ")
sm.setParam(57)
sm.sendSay("#bHow far along are the wall repairs? ")
sm.setParam(37)
sm.sendSay("We'll be finished soon enough. We've sent some of our men to help with the catapults, and others are out on patrol, so we're a touch short-handed. ")
sm.setParam(57)
sm.sendSay("#bLet me help out. ")
sm.spawnNpc(9400586, 1260, -520)
sm.showNpcSpecialActionByTemplateId(9400586, "summon", 0)
sm.spawnNpc(9400588, 1220, -520)
sm.showNpcSpecialActionByTemplateId(9400588, "summon", 0)
sm.spawnNpc(9400601, 1180, -520)
sm.showNpcSpecialActionByTemplateId(9400601, "summon", 0)
sm.spawnNpc(9400592, 1140, -520)
sm.showNpcSpecialActionByTemplateId(9400592, "summon", 0)
sm.spawnNpc(9400598, 1100, -520)
sm.showNpcSpecialActionByTemplateId(9400598, "summon", 0)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("Perhaps I can help as well. ")
sm.setInnerOverrideSpeakerTemplateID(9400588) # Ullan
sm.sendSay("Me too! ")
sm.setInnerOverrideSpeakerTemplateID(9400601) # Elva
sm.sendSay("Count me in. ")
sm.setParam(57)
sm.sendSay("#bHow did you all show up at once? ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400588) # Ullan
sm.sendSay("Chief Gurnardson's going around telling everyone. ")
sm.sendSay("He said Slaka saw a Fembris and wet his pants, so everyone needs to help out so he doesn't have to be scared anymore! ")
sm.setParam(57)
sm.sendSay("#bUgh... Not the motivation I was hoping for...")
sm.spawnNpc(9400590, 1560, -520)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400597, 1610, -520)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#...Let me help, too. ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#That's the spirit! Build those walls up high and strong, so the Fembris can't get through! Heh heh. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("We'll be finished in no time with all this help. ")
sm.sendSay("We should do this by stations. Sanaan can move the building stones from here to there, and Gurnardson can carry them down the stairs to Ullan... ")
sm.sendSay("And #h0# can take them from the lot up to the wall. ")
sm.setParam(57)
sm.sendSay("#bSounds good, Chief Birna. And thank you all for coming out to help. Let's get it done! ")
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "Right on... ", 2000, 1, 0, 0, 0, 4, 9400590, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "Heh, this is nothing!", 2000, 1, 0, 0, 0, 4, 9400597, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "I'm happy we're all working together.", 2000, 1, 0, 0, 0, 4, 9400586, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "Yessir! ", 2000, 1, 0, 0, 0, 4, 9400588, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "You got it.", 2000, 1, 0, 0, 0, 4, 9400601, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "Just say the word!", 2000, 1, 0, 0, 0, 4, 9400604, 4878499)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.startQuest(64127)
sm.warp(867202311)