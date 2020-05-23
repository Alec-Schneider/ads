from ads.core.streaming import stream_aggs
#import multiprocessing as mp

def agg(chunk):
    return chunk.groupby('Team').agg({'HR': ['sum','mean', 'std'],
                                      '2B': ['sum','mean', 'std']})

if __name__ == '__main__':
    nonpoolaggs = stream_aggs(r'C:\Users\Alec\MyPython\Baseball\data\2019\2019Standard.csv', agg)
    print(nonpoolaggs.head(20))
    poolaggs = stream_aggs(r'C:\Users\Alec\MyPython\Baseball\data\2019\2019Standard.csv', agg)
    print(nonpoolaggs.head(20))
    print((nonpoolaggs != poolaggs).sum())