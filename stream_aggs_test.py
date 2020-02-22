from ads.core.streaming import stream_aggs
import multiprocessing as mp

def agg(chunk):
    return chunk.groupby('Team').agg({'HR': ['mean', 'std'],
                                      '2B': ['mean', 'std']})

if __name__ == '__main__':
    nonpoolaggs = stream_aggs(r'C:\Users\afs95\MyPython\Baseball\data\2019\2019Standard.csv', agg)
    print(nonpoolaggs.head(20))
    poolaggs = stream_aggs(r'C:\Users\afs95\MyPython\Baseball\data\2019\2019Standard.csv', agg, pool=mp.Pool(processes=4))
    print(nonpoolaggs.head(20))
    print((nonpoolaggs == poolaggs).sum())