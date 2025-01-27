class Solution {
    public int findCircleNum(int[][] isConnected) {

        int n = isConnected.length;
        boolean[] visited= new boolean[n]; 
        int count = 0;

        // agar koi node visited NAHI hai, that means count++. kyuki DFS is not able to
        // reach there & it is another province.

        for (int i = 0; i < n; i++) {

                    if (!visited[i]) {
                        count++;
                        dfs(isConnected, i, visited);

                    }                
            }

        return count;

    }

    private void dfs(int[][] isConnected, int node, boolean[] visited) {

        int n = isConnected.length;
        for(int i=0;i<n;i++){
            if(isConnected[node][i]==1 && !visited[i]){
                visited[i]=true; 
                dfs(isConnected, i, visited);

            }
        }

    }
}
