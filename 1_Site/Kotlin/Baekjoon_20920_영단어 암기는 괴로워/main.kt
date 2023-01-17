import java.io.*
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = System.out.bufferedWriter()

    val (N, M) = br.readLine().split(' ').map { it.toInt() }
    val map = hashMapOf<String, Int>()
    val words = TreeSet<Word>()

    repeat(N) {
        val word = br.readLine()
        if (word.length >= M) {
            map[word] = map.getOrDefault(word, 0) + 1
        }
    }

    for ((key, value) in map) {
        words.add(Word(key, value))
    }

    for (word in words) {
        bw.write("${word.spelling}\n")
    }
    bw.flush()
}

data class Word(val spelling: String, val count: Int) : Comparable<Word> {
    override fun compareTo(other: Word): Int =
        if (count == other.count) {
            if (spelling.length == other.spelling.length) {
                spelling.compareTo(other.spelling)
            } else {
                other.spelling.length - spelling.length
            }
        } else {
            other.count - count
        }
}