import kotlin.math.*

class Solution {
    fun solution(numbers: IntArray, hand: String): String {
        var result = StringBuilder()
        val keyPad = mapOf(
            1 to Pair(0,0),
            2 to Pair(0,1),
            3 to Pair(0,2),
            4 to Pair(1,0),
            5 to Pair(1,1),
            6 to Pair(1,2),
            7 to Pair(2,0),
            8 to Pair(2,1),
            9 to Pair(2,2),
            '*' to Pair(3,0),
            0 to Pair(3,1),
            '#' to Pair(3,2)
        )

        var left = keyPad['*']!!
        var right = keyPad['#']!!

        for (number in numbers) {
            when(number) {
                1,4,7 -> {
                    result.append("L")
                    left = keyPad[number]!!
                }
                3,6,9 -> {
                    result.append("R")
                    right = keyPad[number]!!
                }
                else -> {
                    var key = keyPad[number]!!

                    val leftDiff = key.let{left!!.distance(it)}
                    val rightDiff = key.let{right!!.distance(it)}

                    if (leftDiff > rightDiff) {
                        result.append("R")
                        right = key
                    }
                    else if (rightDiff > leftDiff) {
                        result.append("L")
                        left = key
                    }
                    else {
                        if (hand == "right") {
                            result.append("R")
                            right = key
                        } else {
                            result.append("L")
                            left = key
                        }
                    }
                }
            }
        }

        return result.toString()
    }

    fun Pair<Int,Int>.distance(pair : Pair<Int,Int>) : Int {
        return abs(this.first - pair.first) + abs(this.second - pair.second)
    }
}