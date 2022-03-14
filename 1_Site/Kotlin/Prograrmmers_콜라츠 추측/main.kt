class Solution {
    fun solution(num: Int): Int {
        var cnt : Int = 0
        var num : Long = num.toLong()
        while (cnt < 501) {
            if (num == 1L) {
                return cnt
            }
            if (num%2 == 0L) {
                num = num / 2
            }else{
                num = (num * 3) + 1
            }
            cnt+=1
        }
        return -1
    }
}