import kotlin.collections.ArrayDeque

class Solution {
    val move = arrayOf(Pair(1,0),Pair(0,1),Pair(-1,0),Pair(0,-1))

    fun solution(places: Array<Array<String>>): IntArray {
        var result: IntArray = intArrayOf(1,1,1,1,1)
        for (index in places.indices) {
            val place = places[index]
            val graph = Array(5){i->place[i].split("").slice(1..5)}

            var flag = true
            for (i in 0 until graph.size) {
                for (j in 0 until graph[i].size) {
                    if (graph[i][j] == "P") {
                        flag = bfs(graph, j, i)
                        if (!flag) break
                    }
                }
                if(!flag) {
                    result[index] = 0
                    break
                }
            }
        }
        return result
    }
    fun bfs(graph : Array<List<String>>, startX : Int, startY : Int) : Boolean {
        // 비용,x,y
        var queue = ArrayDeque<Triple<Int,Int,Int>>()
        var visited = Array(5){Array(5){false}}
        visited[startY][startX] = true
        queue.add(Triple(0,startX,startY))
        while (queue.isNotEmpty()) {
            val (cost,x,y) = queue.removeFirst()
            if (cost == 2) continue
            for ((mx,my) in move) {
                var dx = x + mx
                var dy = y + my
                if (dx < 0 || dx >= 5 || dy < 0 || dy >= 5) continue
                if (visited[dy][dx]) continue
                if (graph[dy][dx] == "X") continue
                if (graph[dy][dx] == "P") return false
                visited[dy][dx] = true
                queue.add(Triple(cost+1,dx,dy))
            }
        }
        return true
    }
}