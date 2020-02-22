import pandas as pd

class BRef(pd.DataFrame):
    """
    Class for a dataframe object (specifically from basketball reference)
    and does various manipulations
    """

    @property
    def _constructor(self):
        return BRef

    def drop_headers(self):
        """
        Drop rows in the data that duplicates of the header
        specific issue to Basketball Reference
        """
        drop = self.columns

        for num, row in self.iterrows():
            if row[0] in drop:
                self.drop(num, axis=0, inplace=True)
        for col in self.columns:
            if 'Unnamed' in col:
                self.drop(col, axis=1, inplace=True)

    def remove_dup_players(self, ident, col, keep_on):
        rks = []
        dups = []
        for i in self[ident]:
            if i not in rks:
                rks.append(i)
            else:
                dups.append(i)
        for i in dups:
            for num, row in self.iterrows():
                if row[ident] == i:
                    if not row[col] == keep_on:
                        self.drop(num, axis=0, inplace=True)

    def leader_dict(self, stats):
        """Create dict of {stat column: (index of highest, index of lowest)"""
        maxmin = {}
        for i in stats:
            maxmin[i] = (self[i].idxmax(), self[i].idxmin())
        return maxmin