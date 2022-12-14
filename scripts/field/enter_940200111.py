# id 940200111 (Hidden Street : Elluel), field 940200111
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.spawnNpc(3003274, 40, -150)
sm.showNpcSpecialActionByTemplateId(3003274, "summon", 0)
sm.spawnNpc(3003278, -110, -140)
sm.showNpcSpecialActionByTemplateId(3003278, "summon", 0)
sm.spawnNpc(3003275, -205, -150)
sm.showNpcSpecialActionByTemplateId(3003275, "summon", 0)
sm.spawnNpc(3003276, -350, -150)
sm.showNpcSpecialActionByTemplateId(3003276, "summon", 0)
sm.spawnNpc(3003277, -280, -150)
sm.showNpcSpecialActionByTemplateId(3003277, "summon", 0)
sm.spawnNpc(3003279, 5, -320)
sm.showNpcSpecialActionByTemplateId(3003279, "summon", 0)
sm.spawnNpc(3003280, -210, -320)
sm.showNpcSpecialActionByTemplateId(3003280, "summon", 0)
sm.spawnNpc(3003270, 80, -145)
sm.showNpcSpecialActionByTemplateId(3003270, "summon", 0)
sm.spawnNpc(3003282, 55, -320)
sm.showNpcSpecialActionByTemplateId(3003282, "summon", 0)
sm.spawnNpc(3003281, -270, -320)
sm.showNpcSpecialActionByTemplateId(3003281, "summon", 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003276) # Philius
sm.sendNext("Stay safe, Your Majesty.")
sm.setInnerOverrideSpeakerTemplateID(3003278) # Mercedes
sm.sendSay("Thank you, Philius. Thank you everyone...")
sm.setInnerOverrideSpeakerTemplateID(3003276) # Philius
sm.sendSay("The coming battle will be difficult on everyone alike, you, your friends and your people. We will do the best we can during your absence.")
sm.setInnerOverrideSpeakerTemplateID(3003281) # Deet
sm.sendSay("Your Majesty!")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face0#...")
sm.setFieldGrey(GreyFieldType.Field, True)
sm.blind(True, 50, 0, 0, 0, 1300)
sm.sendDelay(1600)
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendNext("#face2#(...I have a bad feeling about this. What if she doesn't come back?! This could be the last time we ever see her!)")
sm.sendSay("#face2#(...I have to go with her! I'll fight too! Even if I'm not any good at archery...)")
sm.setFieldGrey(GreyFieldType.Field, False)
sm.blind(True, 1, 255, 255, 255, 200)
sm.blind(False, 0, 0, 0, 0, 1300)
sm.sendDelay(1600)
sm.moveNpcByTemplateId(3003274, True, 25, 160)
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendNext("#face0#I will fight by your side! Take me with you to the battlefield!")
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 134951238, 0, 0)
sm.sendSay("#face0#I want to help! Please let me come with you!")
sm.setInnerOverrideSpeakerTemplateID(3003281) # Deet
sm.sendSay("I want to fight too!")
sm.setInnerOverrideSpeakerTemplateID(3003275) # Danika
sm.sendSay("No Deet, you're too young! ...Your Majesty.")
sm.setInnerOverrideSpeakerTemplateID(3003278) # Mercedes
sm.sendSay("Thank you both, but you must remain behind. It is my duty as your ruler to protect you, not the other way around. Trust in me and watch over Elluel while I am away.")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face0#...")
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendSay("#face3#(Mercedes...)")
sm.blind(True, 255, 0, 0, 0, 250)
sm.sendDelay(250)
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(940200112)
