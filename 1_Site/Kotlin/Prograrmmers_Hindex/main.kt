import kotlin.math.*
class Solution {
    fun solution(citations: IntArray): Int {
        var citations = citations.sorted()
        var temp = min(citations.size, citations.last())

        citations.forEachIndexed { i, citation ->
            if (citation >= temp) {
                return temp
            }
            temp--
        }
        return temp
    }
}