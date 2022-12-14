# id 64084 ([MONAD: The First Omen] Local Villagers), field 867201760
sm.createQuestWithQRValue(parentID, "chk1=1;chk2=1")
sm.lockInGameUI(True, False)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bBe careful when climbing up! ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face1#Thanks, #h0#! ")
sm.sendDelay(2000)
sm.sendNext("#face5#Ahh! Are you serious?! ")
sm.sendSay("#face5#Ugh... I'm coming. ")
sm.spawnNpc(9400580, 1630, 440)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.sendDelay(1000)
sm.sendNext("#face5#You should have warned me! ")
sm.sendSay("#face3#It was too dark for me to see what it was. The moment I realized it was a Jellyrash, I almost lost my grip! ")
sm.sendSay("#face0#Bleh! Thanks... I guess. ")
sm.setParam(57)
sm.sendSay("#bI'm sorry! There really wasn't anything else rope-like around here. ")
sm.setParam(37)
sm.sendSay("#face1#It's okay. It was a bit... sticky, but it got the job done. ")
sm.sendSay("#face1#Anyway! The important thing is... ")
sm.sendSay("#face1#This hole must have been dug by someone! That means someone's living nearby, right? ")
sm.sendSay("#face2#It could be the old lady's cabin. Let's go look for it! ")
sm.flipNpcByTemplateId(9400580, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400580, False, 200, 100)
sm.sendDelay(3000)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(parentID)
sm.warp(867201800)
