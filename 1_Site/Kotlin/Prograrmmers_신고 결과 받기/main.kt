class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        var reportCount = mutableMapOf<String,Int>()
        var reported_dict : MutableMap<String, MutableList<String>> =
            mutableMapOf<String,MutableList<String>>().apply {
                id_list.forEach {
                    put(it,mutableListOf<String>())
                    reportCount[it] = 0
                }
            }

        var report = report.toSet()
        report.forEach {
            var (user1, user2) = it.split(' ')
            reported_dict[user2]!!.add(user1)
        }

        reported_dict.filter{
            it.value.size >= k
        }.forEach {
            for (v in it.value) {
                reportCount[v] = reportCount[v]!! + 1
            }
        }

        return reportCount.values.toIntArray()
    }
}