# Witch's Broomstick Mount 30-Day Coupon  |  (2431496)
if sm.getSkillByItem() == 0:# Check whether item has an vehicleID stored,  0 if false.
    sm.chat("An Error occurred whilst trying to find the mount.")
elif sm.hasSkill(sm.getSkillByItem()):
    sm.chat("You already have the 'Witch's Broomstick' mount.")
else:
    sm.consumeItem()
    sm.giveSkill(sm.getSkillByItem())
    sm.chat("Successfully added the 'Witch's Broomstick' mount.")
sm.dispose()
