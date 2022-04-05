import kotlin.collections.ArrayDeque
import kotlin.math.*

class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        var result = 100
        var nodes = Array(n+1){mutableListOf<Int>()}

        repeat(wires.size) {
            var (first, second) = wires[it]
            nodes[first].add(second)
            nodes[second].add(first)
        }

        repeat(wires.size) {
            var (first, second) = wires[it]
            var temp = bfs(first, second, wires, nodes)
            result = min(result, abs((n - temp) - temp))
        }
        return result
    }

    fun bfs(root : Int, ban : Int, wires : Array<IntArray>, nodes : Array<MutableList<Int>>) : Int {
        var queue = ArrayDeque<Int>().apply {
            add(root)
        }
        var visited = Array(nodes.size){false}
        visited[root] = true
        visited[ban] = true
        var count = 1

        while(!queue.isEmpty()) {
            var node = queue.removeFirst()
            nodes[node].forEach {
                if(!visited[it]) {
                    queue.add(it)
                    visited[it] = true
                    count++
                }
            }
        }

        return count
    }
}