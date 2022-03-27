import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (H,W) = br.readLine().split(' ').map{it.toInt()}

    repeat(H) {
        var count = -101
        println(br.readLine()!!.map{
            count++
            if(it == 'c') count = 0
            max(count, -1)
        }.joinToString(" "))

    }
}