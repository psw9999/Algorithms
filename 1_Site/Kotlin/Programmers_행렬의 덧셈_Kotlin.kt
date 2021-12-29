class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = Array<IntArray>(arr1.size){i->IntArray(arr1[i].size)}
        for (i in arr1.indices) {
            for (j in arr1[i].indices) {
                answer[i][j] = arr1[i][j] + arr2[i][j]
            }
        }
        return answer
    }
}