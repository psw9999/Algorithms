import kotlin.math.*

class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        var result = mutableListOf<Int>()
        var parkingMap = mutableMapOf<String, Int>()
        var usingTimeMap = mutableMapOf<String, Int>()

        // 레코드 체크
        records.forEach{ record ->
            val (temp, num, status) = record.split(" ").map{it}
            val temp2 = temp.split(":")
            val time = (temp2[0].toInt() * 60) + temp2[1].toInt()
            if (status == "IN") {
                parkingMap[num] = time
            }
            else {
                usingTimeMap[num] = usingTimeMap.getOrDefault(num, 0) + (time - parkingMap[num]!!)
                parkingMap[num] = -1
            }
        }

        // 출차 여부 확인
        val lastTime = (23*60) + 59
        for ((k,v) in parkingMap) {
            if (v != -1) {
                usingTimeMap[k] = usingTimeMap.getOrDefault(k, 0) + (lastTime - parkingMap[k]!!)
            }
        }

        usingTimeMap = usingTimeMap.toSortedMap()
        // 주차 요금 계산
        for ((k,v) in usingTimeMap) {
            if (v <= fees[0]) {
                result.add(fees[1])
            }
            else {
                var temp = v - fees[0]
                var remain : Int = temp / fees[2]
                if ((temp % fees[2]) != 0) remain += 1
                result.add(fees[1] + (fees[3] * remain))
            }
        }

        return result.toIntArray()
    }
}