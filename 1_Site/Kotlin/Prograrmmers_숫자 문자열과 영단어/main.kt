class Solution {
    fun solution(s: String): Int {
        var result = s
        val numbers = mapOf<String,String>(
            "zero" to "0",
            "one" to "1",
            "two" to "2",
            "three" to "3",
            "four" to "4",
            "five" to "5",
            "six" to "6",
            "seven" to "7",
            "eight" to "8",
            "nine" to "9")
// 내 풀이
//        val numbers_key = numbers.keys
//        val numbers_value = numbers.values
//
//        for(str in s) {
//            sb.append(str)
//            if (numbers_key.contains(sb.toString())) {
//                result.append(numbers[sb.toString()])
//                sb.setLength(0)
//            }
//            else if (numbers_value.contains(sb.toString())) {
//                result.append(sb)
//                sb.setLength(0)
//            }
//        }

        for ((k,v) in numbers) {
            result = result.replace(k,v)
        }

        return result.toInt()
    }
}