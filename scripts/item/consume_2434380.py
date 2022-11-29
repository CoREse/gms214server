# Cygnus Knights Palanquin Mount 90-Day Coupon  |  (2434380)
if sm.getSkillByItem() == 0:# Check whether item has an vehicleID stored,  0 if false.
    sm.chat("An Error occurred whilst trying to find the mount.")
elif sm.hasSkill(sm.getSkillByItem()):
    sm.chat("You already have the 'Cygnus Knights Palanquin' mount.")
else:
    sm.consumeItem()
    sm.giveSkill(sm.getSkillByItem())
    sm.chat("Successfully added the 'Cygnus Knights Palanquin' mount.")
sm.dispose()
