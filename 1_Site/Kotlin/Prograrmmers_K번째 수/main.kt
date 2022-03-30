class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        return mutableListOf<Int>().apply {
            commands.forEach{
                add(array.slice((it[0]-1)..(it[1]-1)).sorted().get(it[2]-1))
            }
        }.toIntArray()
    }
}