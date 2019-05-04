class Solution {
    private int[] coins;
    private int[] memo;
    
    public int numCoins(int amount) {
        if (amount == 0)
            return 0;
        
        if (memo[amount] == 0) {
            int minNumCoins = -1;
            
            for (int coin : coins)
                
                if (amount - coin >= 0) {
                    int currNumCoins = 1 + numCoins(amount - coin);
                    
                    if (currNumCoins == 0)
                        continue;
                    
                    else if (minNumCoins == -1)
                        minNumCoins = currNumCoins;
                    
                    else
                        minNumCoins = Math.min(currNumCoins, minNumCoins);
                }
            
            memo[amount] = minNumCoins;
        }
        
        return memo[amount];
    }
    
    public int coinChange(int[] coins, int amount) {
        this.coins = coins;
        this.memo = new int[amount + 1];
        return numCoins(amount);
    }
}
