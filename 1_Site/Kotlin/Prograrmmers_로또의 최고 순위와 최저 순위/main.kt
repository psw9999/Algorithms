class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var sameCnt : Int = lottos.filter{win_nums.contains(it)}.size
        var zeroCnt : Int = lottos.filter{it==0}.size

        return intArrayOf(
            7 - sameCnt - zeroCnt, 7 - sameCnt
        ).map{if(it > 6) 6 else it}.toIntArray()

    }
}