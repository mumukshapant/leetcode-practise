class Solution {
    // youtube: https://www.youtube.com/watch?v=E9qHRcQXmDk
// bekar problem. DO AGAIN
    public String decodeString(String s) {
        Stack<String> st=new Stack<>(); 
        for(int i=0;i<s.length();i++){
            String ch=s.charAt(i)+"";
            if(!ch.equals("]")) st.push(ch);
            else{
                String str="";
                while(!st.isEmpty() && !st.peek().equals("[")){
                    str+=st.pop();
                }
               
                st.pop();
                String times="";
                while(!st.isEmpty() && Character.isDigit(st.peek().charAt(0))){
                    times=st.pop()+times;
                }
                st.push(str.repeat(Integer.valueOf(times)));
                
            }
        }
        StringBuilder temp=new StringBuilder();
        while(!st.isEmpty()){
            temp.append(st.pop());
        }
        temp.reverse();
        return new String(temp);
    }
}