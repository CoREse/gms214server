# id 3556 (What's in a Name), field 270000000
sm.setSpeakerID(2140006) # Amnesiac Temple Keeper
sm.sendNext("You're back! I have so much to tell you!\r\n")
sm.setParam(2)
sm.sendSay("\r\n\r\n\r\n#bListen. I'm sorry but... There's just nothing else I can...#k")
sm.setParam(0)
sm.sendSay("I think the Tinglebrain Potion worked! I keep getting glimpses of my past... I remember following a masked man when he was battling monsters. I THINK I hid some kind of map in this big library. I feel like... I feel like all my memories will return soon. I even remember my name!\r\n")
sm.setParam(2)
sm.sendSay("\r\n\r\n\r\nﾡﾡ#bThat's great! So... tell me your name already!#k")
sm.setParam(0)
sm.sendSay("A-are you sure?")
sm.lockInGameUI(True, False)
sm.sendDelay(3000)
sm.lockInGameUI(False, True)
sm.sendNext("It's weird to say it after all this time... M-my name is #e#bKao#k#n! That's me. That's who I was...\r\n\r\n#fUI/UIWindow2.img/QuestIcon/4/0#\r\n\r\n\r\n#fUI/UIWindow2.img/QuestIcon/8/0# 2290200 exp\r\n")
sm.createQuestWithQRValue(18418, "B=32973")
sm.warp(270020200)