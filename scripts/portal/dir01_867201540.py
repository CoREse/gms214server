# id 2 (dir01), field 867201540
sm.sendDelay(250)
sm.forcedMove(True, 150)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bIt seems too steep... to go down... ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#The wind is blowing on that side again! I think we just need to jump down to that tree. ")
sm.setParam(57)
sm.sendNext("#bAlika... are you going to be all right? ")
sm.setParam(37)
sm.sendSay("#face1#I'll just hang onto your back, #h0#! ")
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(64078, "chk1=2")
