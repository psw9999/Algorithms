class Solution {
    val queryMap = mutableMapOf<String, MutableList<Int>>()
    fun solution(info: Array<String>, query: Array<String>): IntArray {
        var result = mutableListOf<Int>()
        info.forEach{dfs("", 0, it.split(" "))}
        for ((k,v) in queryMap) {
            queryMap[k]!!.sort()
        }
        query.forEach{ q ->
            val temp = q.replace(" and ","").split(" ")
            result.add(search(temp[0],temp[1].toInt()))
        }
        return result.toIntArray()
    }

    fun dfs(key : String, depth : Int, info : List<String>) {
        if (depth == 4) {
            if (queryMap.contains(key)) queryMap[key]?.add(info[depth].toInt())
            else queryMap[key] = mutableListOf<Int>(info[depth].toInt())
            return
        }
        dfs("$key-", depth+1, info)
        dfs("$key${info[depth]}", depth+1, info)
    }

    fun search(key : String, score : Int) : Int {
        if(!queryMap.contains(key)) return 0
        var left = 0
        var right = queryMap[key]!!.size - 1
        while (left <= right) {
            var mid = (left + right) / 2
            if(queryMap[key]!![mid] < score) left = mid + 1
            else right = mid - 1
        }
        return queryMap[key]!!.size - left
    }
}