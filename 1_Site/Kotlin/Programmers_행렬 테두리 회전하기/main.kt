import kotlin.math.*

class Solution {
    fun solution(rows: Int, columns: Int, queries: Array<IntArray>): IntArray {
        var result = mutableListOf<Int>()
        val graph = Array(rows){r->
            Array(columns){c->
                ((r*columns)+c+1)
            }
        }

        fun rotate(y1 : Int, x1 : Int, y2 : Int, x2 : Int) {
            var temp1 = graph[y1][x1]
            var temp2 = -1
            var minV = temp1

            // top
            for (i in x1 until x2) {
                temp2 = graph[y1][i+1]
                graph[y1][i+1] = temp1
                temp1 = temp2
                minV = min(minV, temp1)
            }
            // left
            for (i in y1 until y2) {
                temp2 = graph[i+1][x2]
                graph[i+1][x2] = temp1
                temp1 = temp2
                minV = min(minV, temp1)
            }
            // bottom
            for (i in x2 downTo (x1+1)) {
                temp2 = graph[y2][i-1]
                graph[y2][i-1] = temp1
                temp1 = temp2
                minV = min(minV, temp1)
            }
            // right
            for (i in y2 downTo (y1+1)) {
                temp2 = graph[i-1][x1]
                graph[i-1][x1] = temp1
                temp1 = temp2
                minV = min(minV, temp1)
            }
            minV = min(minV, temp1)
            result.add(minV)
        }

        queries.forEach { query ->
            val (y1,x1,y2,x2) = query.map{it -> it - 1}
            rotate(y1,x1,y2,x2)
        }

        return result.toIntArray()
    }
}