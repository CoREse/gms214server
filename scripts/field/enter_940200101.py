# id 940200101 (Hidden Street : Twilight Training Grounds), field 940200101
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1000, 0, -5, -450)
sm.spawnNpc(3003270, -250, -20)
sm.showNpcSpecialActionByTemplateId(3003270, "summon", 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1500)
sm.sendDelay(1000)
sm.zoomCamera(4000, 1000, 4000, -5, 160)
sm.sendDelay(500)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/arrow0", 200)
sm.sendDelay(500)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/arrow1", 200)
sm.sendDelay(500)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/arrow2", 200)
sm.sendDelay(100)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendNext("#face1#Yah!")
sm.sendSay("#face2#Hiya!")
sm.moveNpcByTemplateId(3003270, False, 320, 160)
sm.sendDelay(3000)
sm.moveNpcByTemplateId(3003270, True, 5, 160)
sm.sendNext("#face2#Argh! There's no use!")
sm.sendSay("#face3#...As much as I practice, I'll never get it right. If only I was gifted like Athena... Then...")
sm.sendSay("#face3#Ugh...")
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.resetNpcSpecialActionByTemplateId(3003270)
sm.showNpcSpecialActionByTemplateId(3003270, "sleep", -1)
sm.zoomCamera(0, 2000, 0, 0, 260)
sm.sendDelay(500)
sm.zoomCamera(3000, 2000, 3000, 90, 260)
sm.sendDelay(3000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(940200102)
