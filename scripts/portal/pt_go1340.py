# id 1 (next), field 867201320
sm.lockInGameUI(True, False)
sm.spawnNpc(9400580, -372, 440)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400595, -245, 440)
sm.showNpcSpecialActionByTemplateId(9400595, "summon", 0)
sm.setMapTaggedObjectVisible("ribbon02", True, 0, 0)
sm.sendDelay(500)
sm.showNpcSpecialActionByTemplateId(9400580, "ribbon", -1)
sm.sendDelay(2000)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bAlika? What are you doing? We have to go before the sun sets.")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face1#Hold on a second. It's easy to get lost in the forest, so I want to mark the path we traveled.")
sm.sendDelay(500)
sm.resetNpcSpecialActionByTemplateId(9400580)
sm.setMapTaggedObjectVisible("ribbon03", True, 0, 0)
sm.sendDelay(1000)
sm.sendNext("#face1#There! Let's go! ")
sm.lockInGameUI(False, True)
sm.warp(867201340)
