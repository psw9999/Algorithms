package Algorithms

class main {
    // toInt() 혹은 toDouble 등 형변환을 잘 사용하자
    class Solution {
        fun main(args: Array<String>) {
            val (n,m) = readLine()!!.split(' ').map{it.toInt()}
            val sb = StringBuilder()
            for (i in 0 until m) {
                for (j in 0 until n) {
                    sb.append("*")
                }
                sb.append("\n")
            }
            println(sb)
        }
    }
}