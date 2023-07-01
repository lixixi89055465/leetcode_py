def process(param, end, add, times, del1, start, param1, param2):
    pass


def miinCoins1(add,times,del1,start,end):
    if start>end:
        return -1
    return process(0,end,add,times,del1,start,
                   end*2,((end-start)/2)*add)

