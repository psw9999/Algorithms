package Algorithms

class main {
    fun solution(phone_number: String): String {
        var result = StringBuilder("")
    for(i in 0..(phone_number.length-5)) {
        result.append('*')
    }
    result.append(phone_number.substring(phone_number.length-4..phone_number.length-1))
    return result.toString()
}
}