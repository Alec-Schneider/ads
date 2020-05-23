import pandas as pd
from ads.baseball.advanced import (bbwgt, hbpwgt, wgt1b, wgt2b, 
                                    wgt3b, hrwgt, lgwOBA, wOBA_scale)


class Fangraphs(pd.DataFrame):
    """
    class that inherits a DataFrame object of Fangraphs data
    """
    @property
    def _constructor(self):
        return Fangraphs

    def wOBA(self):
        """
        parameters
        ------------
        row: row of a DataFrame object
            row must contain BB, HBP, 1B, 2B, 3B, HR, AB, SF, and IBB
    
        return
        ------------
            weighted on base average given a player's stats
        """
        self.bbwgt = bbwgt 
        self.hbpwgt = hbpwgt 
        self.wgt1b = wgt1b
        self.wgt2b = wgt2b
        self.wgt3b = wgt3b
        self.hrwgt = hrwgt
        
        return ((self.bbwgt * self['BB'] + self.hbpwgt * self['HBP'] + self.wgt1b * self['1B'] + self.wgt2b * self['2B']
                 + self.wgt3b * self['3B'] + self.hrwgt * self['HR']) / (self['AB'] + self['BB'] - self['IBB'] + self['SF'] + self['HBP']))


    def wRAA(self):
        """
        parameters
        ------------
        row: row of a DataFrame object
            row must contain the calculated wOBA and also PA
    
        return
        ------------
            weighted runs above average
        """
        self.lgwOBA = lgwOBA
        self.wOBA_scale = wOBA_scale
        woba = self.wOBA()

        return ((woba - self.lgwOBA) /self.wOBA_scale) * self['PA']