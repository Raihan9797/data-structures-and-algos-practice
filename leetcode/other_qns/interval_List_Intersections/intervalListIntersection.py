class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f_ptr = 0
        s_ptr = 0
        res = []
        
        while f_ptr < len(firstList) and s_ptr < len(secondList):
            f_start = firstList[f_ptr][0]
            f_end = firstList[f_ptr][1]
            
            s_start = secondList[s_ptr][0]
            s_end = secondList[s_ptr][1]
            
            if f_start > s_end:
                print('skip')
                s_ptr +=1
                continue
            if s_start > f_end:
                print('skip2')
                f_ptr += 1
                continue
            #print(f_start, f_end)
            #print(s_start, s_end)
            
            # compare starts: biggest start is the interval start
            # tbh no need to compare, the criteria for moving is based on the ends
            # not the starts! so just use max()
            itv_start = max(f_start, s_start)
            #if f_start >= s_start:
            #    itv_start = f_start
            #    #f_ptr += 1
            #else:
            #    itv_start = s_start
            #    #s_ptr += 1
            #print('start itv', itv_start)
            
            # compare ends: smallest end is the interval end
            # also increment the pointer!
            if f_end <= s_end:
                itv_end = f_end
                f_ptr +=1
            else:
                itv_end = s_end
                s_ptr += 1
            print('ans: ', itv_start, itv_end)
            res.append([itv_start, itv_end])
            
            # covers the case where f and s are not connected at all
            # this case results in the starts being bigger than the end
            # ie not an actual interval
            #if (itv_start > itv_end):
            #    continue
            #else:
            #    res.append([itv_start, itv_end])
            
            
        return res