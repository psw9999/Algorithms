import kotlin.math.*
class Solution {
    var result = 0
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        var answer: Int = -1
        val visited = Array<Boolean>(dungeons.size){false}
        dfs(k, dungeons, visited, 0)
        return result
    }
    fun dfs(piro : Int, dungeons : Array<IntArray>, visited : Array<Boolean>, cnt : Int) {
        result = max(result, cnt)
        for ((index, dungeon) in dungeons.withIndex()) {
            if (visited[index]) continue
            if (dungeon[0] > piro) continue
            visited[index] = true
            dfs(piro-dungeon[1], dungeons, visited, cnt+1)
            visited[index] = false
        }
    }
}