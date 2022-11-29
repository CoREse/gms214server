package net.swordie.ms.loaders.containerclasses;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

/**
 * @author Sjonnie
 * Created on 7/23/2018.
 */
@Entity
@Table(name = "monster_collection_session_rewards")
public class MonsterCollectionSessionRewardInfo implements Serializable {
    @Id
    private int region;
    @Id
    private int session;
    private int rewardID;
    private int quantity;

    public int getRegion() {
        return region;
    }

    public void setRegion(int region) {
        this.region = region;
    }

    public int getSession() {
        return session;
    }

    public void setSession(int session) {
        this.session = session;
    }

    public int getRewardID() {
        return rewardID;
    }

    public void setRewardID(int rewardID) {
        this.rewardID = rewardID;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}

