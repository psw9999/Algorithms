class Solution {
    fun solution(s: String): IntArray {
        var result = intArrayOf()
        var s_map = mutableMapOf<Int,Int>()
        var s = s

        s = s.slice(1..s.length-3)
        var s_list = s.replace("{","").split("},")

        s_list.forEach { temp ->
            var t = temp.split(",").map{it.toInt()}
            for (i in t) {
                s_map[i] = s_map.getOrDefault(i,0) + 1
            }
        }

        s_map = s_map.toSortedMap(compareByDescending{s_map[it]!!})

        return s_map.keys.toIntArray()
    }
}