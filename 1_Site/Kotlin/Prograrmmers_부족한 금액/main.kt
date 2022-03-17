class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var total = 0L
        for (i in 1..count) {
            total += price * i
        }
        if (money >= total) {
            return 0
        }else{
            return total - money
        }
    }
}