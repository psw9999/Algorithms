package Algorithms

class main {
    // toInt() 혹은 toDouble 등 형변환을 잘 사용하자
    class Solution {
        fun solution(arr: IntArray): Double {
            var total : Double = arr.sum().toDouble()
            return (total/arr.size) as Double
        }
    }
}