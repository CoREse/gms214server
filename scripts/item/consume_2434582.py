# Mystical Butterflies Mount 30-Day Coupon  |  (2434582)
if sm.getSkillByItem() == 0:# Check whether item has an vehicleID stored,  0 if false.
    sm.chat("An Error occurred whilst trying to find the mount.")
elif sm.hasSkill(sm.getSkillByItem()):
    sm.chat("You already have the 'Mystical Butterflies' mount.")
else:
    sm.consumeItem()
    sm.giveSkill(sm.getSkillByItem())
    sm.chat("Successfully added the 'Mystical Butterflies' mount.")
sm.dispose()
