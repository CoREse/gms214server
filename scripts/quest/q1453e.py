#   [Job Adv] (Lv.100)   Way of the Arch Mage FP / Arch Mage IL / Bishop

heroicPentagon = 4031511
heroicStar = 4031512

sm.setSpeakerID(2081200) # Gritto
sm.sendNext("You have returned.")


sm.sendNext("I will take these tokens of heroism from you, and grant you your 4th job skills.\r\nYou helped a great deal in the fight to come.")

sm.consumeItem(heroicPentagon, 1)
sm.consumeItem(heroicStar, 1)
sm.completeQuestNoRewards(parentID)
chrJobID = sm.getChr().getJob()
sm.jobAdvance(chrJobID+1)
sm.dispose()
