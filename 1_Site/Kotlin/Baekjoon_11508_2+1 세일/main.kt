import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()
    val products = IntArray(N)
    //val products = mutableListOf<Int>()

    repeat(N) { i ->
        products[i] = br.readLine().toInt()
    }

    var result = 0
    products.sortDescending()
    for ((i,product) in products.withIndex()) {
        if (((i+1) % 3) != 0) result += product
    }

    println(result)
}
