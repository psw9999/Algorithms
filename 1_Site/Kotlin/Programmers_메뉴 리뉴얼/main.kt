class Solution {
    fun solution(orders: Array<String>, course: IntArray): Array<String> {
        var courses = mutableMapOf<String,Int>()

        fun makeCombination(order : String, target : Int, temp : String, cur : Int, start : Int){
            if (cur == target) {
                courses[temp] = courses.getOrDefault(temp, 0) + 1
            }
            else {
                for (i in start until order.length) {
                    makeCombination(order, target, temp+order[i], cur+1, i+1)
                }
            }
        }

        orders.forEach { order->
            val temp = order.split("").sorted()
            course.forEach { count ->
                if (order.length >= count) {
                    makeCombination(temp.joinToString(""), count, "", 0,0)
                }
            }
        }

        var result = mutableMapOf<Int, Pair<Int, MutableList<String>>>()

        for ((k,v) in courses) {
            if (v == 1) continue
            var temp = result.getOrDefault(k.length, Pair(0,mutableListOf()))
            if (v > temp.first) {
                result[k.length] = Pair(v, mutableListOf(k))
            }
            else if (v == temp.first) {
                result[k.length]!!.second.add(k)
            }
        }

        var answer = mutableListOf<String>()
        for ((k,v) in result) {
            v.second.forEach {
                answer.add(it)
            }
        }

        return answer.sorted().toTypedArray()
    }

}