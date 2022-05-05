import kotlin.collections.ArrayDeque
import kotlin.math.*

data class Content(val dir : Int, val x: Int, val y: Int, val cost: Int)

class Solution {
    fun solution(board: Array<IntArray>): Int {
        var result = Integer.MAX_VALUE
        val move = arrayOf(Pair(1,0),Pair(0,1),Pair(-1,0),Pair(0,-1))
        val visited = Array(4){Array(board.size){i->Array(board[i].size){Integer.MAX_VALUE}}}
        for (i in 0..3) {
            visited[i][0][0] = 0
        }

        val queue = ArrayDeque<Content>()
        if (board[0][1] != 1) {
            queue.add(Content(0,1,0,100))
            visited[0][0][1] = 100
        }
        if (board[1][0] != 1) {
            queue.add(Content(1,0,1,100))
            visited[1][1][0] = 100
        }

        while (queue.isNotEmpty()) {
            //val (dir,x,y,cost) = queue.removeFirst().map{it}
            //println("$dir,$x,$y,$cost")
            val content = queue.removeFirst()
            with(content) {
                for ((i, mv) in move.withIndex()) {
                    val dx = x + mv.first
                    val dy = y + mv.second
                    var temp = cost
                    if (dx < 0 || dy < 0 || dx >= board.size || dy >= board.size) continue
                    if (board[dy][dx] == 1) continue
                    if (move[dir].first == mv.first*-1 && move[dir].second == mv.second*-1) continue

                    if (dir == i) temp += 100
                    else temp += 600

                    if (visited[i][dy][dx] > temp) {
                        visited[i][dy][dx] = temp
                        queue.add(Content(i,dx,dy,temp))
                    }
                }
            }
        }

        for (i in 0..3) {
            result = min(result,visited[i][board.size-1][board.size-1])
        }
        return result
    }
}