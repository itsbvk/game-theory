from .client import Client
import asyncio
import numpy as np
import time

class Team_17_Bot(Client):
    def __init__(self):
        super().__init__()
        self.name = "17"  # Your Bot's Name
        # Your Initialization Code Here
        self.lastBid = {} # {auctionId:[]}
        self.startTime = -1
        self.enemies_max_value = 1.001
        self.enemies_prev_bids = {}
        self.enemys_multiplier = 1.125

    def randConstGen(self,latestBid):
        if 1-latestBid < 0.5:
            return np.random.uniform(0,0.2)
        else:
            return np.random.uniform(0,0.1)
    
    async def start(self, auction_id):
        await super().start(auction_id)
        self.startTime = time.time()
        starting_bid = np.random.uniform(0.1,0.3)
        self.lastBid[auction_id] = starting_bid
        await super().submit_bid(auction_id, starting_bid)
        
        

    async def receive_bid(self, auction_id, bid_value):

        await super().receive_bid(auction_id, bid_value)

        try:
            enemys_prev_bid = self.enemies_prev_bids[-1]
            
            self.enemies_prev_bids[auction_id].append(bid_value)
            enemies_current_multiplier = bid_value/enemys_prev_bid
            if enemies_current_multiplier > 1.125:
                self.enemies_max_value = 
        except:
            self.enemies_prev_bids[auction_id] = [bid_value]
        
        
        print('Received 17\'s bid')
        # Your code for receiving bids
        # print(self.bids)
        last = self.lastBid[auction_id]
        currTStamp = time.time()
        # if abs(30 - (currTStamp-self.startTime)) < 5 and self.bids[-1] > 0.5 and self.startTime > 0:
        #     new_bid = min(1- pow(10,-5),bid_value*1.125+0.3)
        #     if new_bid > last:
        #         self.bids.append(new_bid)
        #         await super().submit_bid(auction_id, new_bid)
        
        if bid_value < 1.25:

            

            if bid_value > 1 and bid_value > self.enemies_max_value:
                self.enemies_max_value = bid_value
            
            new_bid = min(max(last*np.random.uniform(1.125,1.3)+self.randConstGen(last), bid_value*np.random.uniform(1.125,1.3)+0.05),np.random.uniform(self.enemies_max_value,self.enemies_max_value+np.random.uniform(0.1,0.2)))
            if new_bid > last:
                
	            self.lastBid[auction_id] = new_bid
	            await super().submit_bid(auction_id, new_bid)
        # elif bid_value > 1 and bid_value > self.enemies_max_value:
        #     self.enemies_max_value = bid_value
        # pass

    async def end_auction(self, auction_id):
        await super().end_auction(auction_id)
        # Your code for ending auction
