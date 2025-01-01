#0/1 Knapsack Dynamic Programming

'''
The grid was a i x j grid
ith row = the price
jth column = the weight

GRID:


va w  0, 1, 2, 3, 4, 5, 6, 7
(1)1 [0, 1, 1, 1, 1, 1, 1, 1]
(4)3 [0, 1, 1, 4, 5, 5, 5, 5]
(5)4 [0, 1, 1, 4, 5, 6, 6, 6]
(7)5 [0, 1, 1, 4, 5, 7, 8, 9]

We check bottom right [i][j] then go [i-1][j] and check where it stops, then
go [i][j-wt[i]] and go check up again

In this grid example, the answer is

4(5)
3(4)
= 7 weight, $9

if (j < wt[i]){
        T[i][j] = T[i-1][j]}
else {
        T[i][j] = max(val[i] + T[i-1][j-wt[j], T[i-1][j])
}
'''

def knapSack(W,wt,val,n):
        if n == 0 or W == 0:
                return 0

        if wt[n-1] > W:
                return knapSack(W, wt,val, n-1)

        else:
                return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

def main():
        profit = [60, 100, 120]
        weight = [10, 20, 30]
        W = 50
        n = len(profit)
        print(knapSack(W, weight, profit, n))

if __name__ == "__main__":
        main()
