# Dark Hero

medal = 1142344

if sm.canHold(medal):
    sm.chatScript("You have earned a new medal.")
    sm.startQuest(parentID)
    sm.completeQuest(parentID)