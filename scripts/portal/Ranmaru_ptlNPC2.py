# Ranmaru entry NPC

from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type, Cooldown, Hour String

destinations = [
    ["Normal", 120, 807300210, 20, EventType.Ranmaru, 64800000, 18],
    ["Chaos", 240, 807300110, 20, EventType.CRanmaru, 129600000, 36],
]

runsPerDay = 1

if sm.getFieldID() == 807300100:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    dialog = "Do you want to head to '#bSecret Altar#k' to fight \r\n#bMori Ranmaru#k?\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##bGo to Secret Altar (%s Mode) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#Never mind."
    response = sm.sendSay(dialog)

    if sm.getParty() is None:
        sm.sendSayOkay("Please create a party before going in.")
        sm.dispose()

    elif not sm.isPartyLeader():
        sm.sendSayOkay("Please have your party leader talk to me if you wish to face #bMori Ranmaru#k.")
        sm.dispose()

    elif sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        timeUntilReset = sm.getTimeUntilEventReset(destinations[response][4])
        sm.sendNext("You or one of your party member has already attempted facing \r\n#bMori Ranmaru#k within the past " + str(destinations[response][6]) + " Hours.\r\n You have " + timeUntilReset + " left on your cooldown.")
        sm.dispose()

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(BossConstants.RANMARU_TIME)
            sm.addCooldownTimeForParty(destinations[response][4], destinations[response][5])
        else:
            sm.sendSayOkay("One or more party members are lacking the prerequisite entry quests, or are below level #b%d#k." % destinations[response][1])
else:
    if sm.sendAskYesNo("Are you sure you want to leave the battlefield?"):
        sm.warpInstanceOutParty(807300100)