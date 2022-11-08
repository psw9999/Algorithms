import java.io.*

data class Dictionary(
    val count: Int,
    val length: Int,
    val word: String
)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = System.out.bufferedWriter()
    val (N, M) = br.readLine().split(' ').map { it.toInt() }
    val words = hashMapOf<String, Int>()
    val queue = mutableListOf<Dictionary>()

    repeat(N) {
        val word = br.readLine()
        if (word.length >= M) {
            //words[word] = words.getOrDefault(word, 0) + 1
            words.merge(word, 1, Integer::sum)
        }
    }

    for ((word, count) in words.entries) {
        queue.add(
            Dictionary(
                count = count,
                length = word.length,
                word = word
            )
        )
    }
    queue.sortWith(compareBy<Dictionary> { -it.count }.thenByDescending { it.length }.thenBy { it.word })
    for (dictionary in queue) {
        bw.write("${dictionary.word}\n")
    }
    bw.flush()
    bw.close()
}

//더 나은 선택지
//import java.io.BufferedReader
//import java.io.BufferedWriter
//import java.io.InputStreamReader
//import java.io.OutputStreamWriter
//import java.util.*
//
//fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
//    val bw = BufferedWriter(OutputStreamWriter(System.`out`))
//    val tmp = readLine().split(' ')
//    val n = tmp[0].toInt()
//    val min = tmp[1].toInt()
//
//    val map = HashMap<String, Int>()
//    repeat(n) {
//        val line = readLine()
//        if(line.length >= min)
//            map[line] = map.getOrDefault(line, 0) + 1
//    }
//    val set = TreeSet<Word>()
//    for(i in map) {
//        set.add(Word(i.key, i.value))
//    }
//
//    for(i in set) {
//        bw.write("${i.spell}\n")
//    }
//    bw.flush()
//}
//
//data class Word(val spell : String, val cnt : Int) : Comparable<Word>{
//    override fun compareTo(other: Word): Int =
//        if(cnt == other.cnt) {
//            if (spell.length == other.spell.length)
//                spell.compareTo(other.spell)
//            else
//                other.spell.length - spell.length
//        } else
//            other.cnt - cnt
//}
