import kotlin.math.*

class Solution {
    fun solution(s: String): String {
        var numbers : List<Int> = s.split(' ').map{it.toInt()}

        return "${numbers.minOrNull()} ${numbers.maxOrNull()}"
    }
}