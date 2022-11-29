# Napoleon Coupon  |  (2430341)
if sm.getSkillByItem() == 0:# Check whether item has an vehicleID stored,  0 if false.
    sm.chat("An Error occurred whilst trying to find the mount.")
elif sm.hasSkill(sm.getSkillByItem()):
    sm.chat("You already have the 'Napolean' mount.")
else:
    sm.consumeItem()
    sm.giveSkill(sm.getSkillByItem())
    sm.chat("Successfully added the 'Napolean' mount.")
sm.dispose()
