import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()
    val M = br.readLine().toInt()
    val steal : List<Int> = br.readLine().split(' ').map{it.toInt()}.sorted()
    var result = 0

    var left = 0
    var right = N-1

    while (left < right) {
        var total = steal[left] + steal[right]

        if (total == M) {
            left++
            right--
            result++
        }
        else if (total < M) {
            left ++
        }
        else {
            right--
        }
    }

    println(result)
}