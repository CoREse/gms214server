# id 867202683 (Abrup Basin : Shrelephant Habitat), field 867202683
sm.lockInGameUI(True, False)
sm.spawnNpc(9400609, -600, -150)
sm.showNpcSpecialActionByTemplateId(9400609, "summon", 0)
sm.spawnNpc(9400597, -1060, 50)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.spawnNpc(9400590, -400, 50)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bWhat's that? ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#An Eyeful? What's it doing way out here? ")
sm.setParam(57)
sm.sendSay("#bWe need to follow it! ")
sm.forcedMove(False, 300)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/eyeeyeportal", 128)
sm.sendDelay(1000)
sm.blind(True, 255, 240, 240, 240, 1300)
sm.sendDelay(1600)
sm.completeQuestNoCheck(64158)
sm.completeQuestNoCheck(64121)
sm.lockInGameUI(False, True)
sm.warp(867201690)
