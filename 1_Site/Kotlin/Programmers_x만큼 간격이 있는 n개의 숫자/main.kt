class Solution {
    fun solution(x: Int, n: Int): LongArray {
        var answer = mutableListOf<Long>()
        var start : Long = x.toLong()
        for (i in 0..n-1) {
            answer.add(start)
            start += x
        }
        return answer.toLongArray()
    }
}