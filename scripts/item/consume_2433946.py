# Penguin Pack Mount Permanent Coupon  |  (2433946)
if sm.getSkillByItem() == 0:# Check whether item has an vehicleID stored,  0 if false.
    sm.chat("An Error occurred whilst trying to find the mount.")
elif sm.hasSkill(sm.getSkillByItem()):
    sm.chat("You already have the 'Penguin Pack' mount.")
else:
    sm.consumeItem()
    sm.giveSkill(sm.getSkillByItem())
    sm.chat("Successfully added the 'Penguin Pack' mount.")
sm.dispose()
