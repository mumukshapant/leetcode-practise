class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n==1 : 
            return s 
        pq= [(-freq, ch) for ch, freq in Counter(s).items() ]
        heapify(pq)
        res=[] 

        while (pq): 
            freq1, ch1 = heappop(pq)

            #?????
            if not res or ch1!=res[-1]: 
                res.append(ch1)
                if freq1+1 !=0 : #coz negative)
                    heappush(pq,(freq1+1, ch1)) #reducing the freq
            else: 
                if not pq: 
                    return ''
                
                freq2,ch2 = heappop(pq)
                res.append(ch2)

                if freq2+1!=0 : #means it still exists, so we reduce freq
                    heappush(pq,(freq2+1,ch2))
                # ?? 
                heappush(pq,(freq1,ch1))
        return ''.join(res)

