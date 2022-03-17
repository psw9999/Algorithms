import kotlin.math.*

class Solution {
    fun solution(n: Int, m: Int): IntArray {
        var gcmV = gcm(n,m)

        return intArrayOf(gcmV,lcm(n,m,gcmV))
    }
    fun gcm(a : Int, b : Int) : Int {
        var maxV : Int = max(a,b)
        var minV : Int = min(a,b)

        if (minV == 0) {
            return maxV
        }else{
            return gcm(minV, maxV % minV)
        }
    }

    fun lcm(a : Int, b : Int, gcmV : Int) : Int {
        return (a * b) / gcmV
    }
}