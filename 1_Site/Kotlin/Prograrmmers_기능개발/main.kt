import kotlin.collections.ArrayDeque

class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var progresses = ArrayDeque<Int>(progresses.toList())
        var speeds = ArrayDeque<Int>(speeds.toList())
        var result = mutableListOf<Int>()

        while (progresses.isNotEmpty()) {
            var temp = 100 - progresses[0]
            var remainder : Int = temp / speeds[0]
            if ((temp % speeds[0]) != 0) remainder++

            for (i in progresses.indices) {
                progresses[i] += (speeds[i] * remainder)
            }

            var count = 0
            for (i in progresses.indices) {
                if (progresses[0] >= 100) {
                    count++
                    progresses.removeFirst()
                    speeds.removeFirst()
                }
                else break
            }
            result.add(count)
        }
        return result.toIntArray()
    }
}