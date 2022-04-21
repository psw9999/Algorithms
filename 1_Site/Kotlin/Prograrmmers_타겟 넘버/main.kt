class Solution {
    fun solution(numbers: IntArray, target: Int): Int {
        var result = 0
        fun dfs(index : Int, total : Int) {
            if (index == numbers.size) {
                if (total == target) result++
                return
            }
            dfs(index+1,total+numbers[index])
            dfs(index+1,total-numbers[index])
        }
        dfs(0,0)
        return result
    }
}