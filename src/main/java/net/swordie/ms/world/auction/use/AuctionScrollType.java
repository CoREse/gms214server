package net.swordie.ms.world.auction.use;

import net.swordie.ms.client.character.items.Item;
import net.swordie.ms.world.auction.AuctionEnum;

/**
 * @author Sjonnie
 * Created on 1/18/2019.
 */
public enum AuctionScrollType implements AuctionEnum {
    All,
    ArmorAcc, // both
    Weapon,
    EnchancementPot, // both
    CleanSlateSoulWeapon, // both
    Pet,
    Misc,
    Flame
    ;

    public static AuctionEnum getByVal(int val) {
        return val >= 0 && val < values().length ? values()[val] : All;
    }

    @Override
    public AuctionEnum getSubByVal(int val) {
        return null;
    }

    @Override
    public boolean isMatching(Item item) {
        return false;
    }}
