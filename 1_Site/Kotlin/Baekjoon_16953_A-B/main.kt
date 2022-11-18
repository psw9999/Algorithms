import java.io.*
import java.util.ArrayDeque

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (A,B) = br.readLine().split(' ').map{ it.toLong() }

    val queue = ArrayDeque<Pair<Int, Long>>()
    queue.add(Pair(1, A))

    while (queue.isNotEmpty()) {
        val (cnt, value) = queue.removeFirst()

        if (value == B) {
            println("$cnt")
            return
        }

        val t1 = value * 2
        if (t1 <= B) {
            queue.add(Pair(cnt+1, t1))
        }

        val t2 = (value * 10) + 1
        if (t2 <= B) {
            queue.add(Pair(cnt+1, t2))
        }

    }

    println("-1")

}
