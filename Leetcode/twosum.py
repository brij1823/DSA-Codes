class Solution(object):
    def twoSum(self, num, target):
        twosum = {}
        index = {}
        counter = 0
        for i in num:
            try:
                twosum[i] = twosum[i]+1
                index[i].append(counter)
            except:
                twosum[i] = 1
                index[i] = []
                index[i].append(counter)
            counter = counter + 1
        for i in num:
            twosum[i] = twosum[i]-1
            try:
                if(twosum[target-i]>0):
                    if(i == target-i):
                        return [index[i][0],index[i][1]]
                    else:
                        return [index[i][0],index[target-i][0]]
            except:
                continue