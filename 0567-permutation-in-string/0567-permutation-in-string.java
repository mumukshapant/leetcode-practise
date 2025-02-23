class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int m= s1.length(); 
        int n= s2.length(); 

        if(m >n) 
            return false; 


        int[] freq1= new int[26] ;
        int[] freq2 = new int[26]; 

        for(int i=0;i<m ;i++){
            freq1[s1.charAt(i)-'a'] ++; 
            freq2[s2.charAt(i) - 'a']++;
        }
        if(Arrays.equals(freq1,freq2))
            return true; 

        for(int i=m ; i<n; i++){
            freq2[s2.charAt( i-m ) -'a'] -- ; 
            freq2[s2.charAt(i)-'a'] ++; 

            if(Arrays.equals(freq1,freq2))
                return true; 

        }
        return false; 
        
    }
}