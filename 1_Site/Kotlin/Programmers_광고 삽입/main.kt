class Solution {
    fun solution(play_time: String, adv_time: String, logs: Array<String>): String {
        val play_time = play_time.split(":").map{it.toInt()}
        val temp = adv_time.split(":").map{it.toInt()}
        val DP = Array(play_time[0] * 3600 + play_time[1] * 60 + play_time[2]+1){0}
        val adv_time = temp[0] * 3600 + temp[1] * 60 + temp[2] - 1

        logs.forEach { log ->
            val (temp1, temp2) = log.split("-").map{it.split(":").map{it.toInt()}}
            val startTime = temp1[0] * 3600 + temp1[1] * 60 + temp1[2]
            val endTime = temp2[0] * 3600 + temp2[1] * 60 + temp2[2]
            DP[startTime]++
            DP[endTime]--
        }

        var cnt : Long = DP[0].toLong()
        var maxV : Long = DP[0].toLong()
        var result = "00:00:00"
        for (i in 1 until DP.size) {
            DP[i] += DP[i-1]
            cnt += DP[i]
            if (i >= adv_time) {
                if (cnt > maxV) {
                    maxV = cnt
                    var startTime = i - adv_time
                    val hour : Int = startTime / 3600
                    val minute : Int = (startTime % 3600) / 60
                    val second : Int = (startTime % 60)
                    result = String.format("%02d:%02d:%02d", hour, minute, second)
                }
                cnt -= DP[i-adv_time]
            }
        }
        return result
    }
}