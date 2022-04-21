import kotlin.math.*

class Solution {
    fun solution(s: String): Int {
        var result = s.length

        for (i in 1..(s.length/2)) {
            var start = 0
            var end = i-1
            var temp = s.slice(start..end)
            var cnt = 1
            var size = s.length
            while (end+i < s.length) {
                start = start+i
                end = end+i
                if (temp == s.slice(start..end)) {
                    cnt++
                    size -= i
                }
                else {
                    if (cnt > 1) size += cnt.toString().length
                    temp = s.slice(start..end)
                    cnt = 1
                }
            }
            if (cnt > 1) size += cnt.toString().length
            result = min(result, size)
        }
        return result
    }
}