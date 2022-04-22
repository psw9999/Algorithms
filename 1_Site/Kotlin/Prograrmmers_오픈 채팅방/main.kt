class Solution {
    fun solution(record: Array<String>): Array<String> {
        var users = mutableMapOf<String, String>()
        var result = mutableListOf<String>()
        record.forEach { rec ->
            var temp = rec.split(' ')
            if (temp[0] == "Enter" || temp[0] == "Change") {
                users[temp[1]] = temp[2]
            }
        }
        record.forEach { rec ->
            var temp = rec.split(' ')
            if (temp[0] == "Enter") {
                result.add("${users[temp[1]]}님이 들어왔습니다.")
            }
            else if (temp[0] == "Leave") {
                result.add("${users[temp[1]]}님이 나갔습니다.")
            }
        }
        return result.toTypedArray()
    }
}