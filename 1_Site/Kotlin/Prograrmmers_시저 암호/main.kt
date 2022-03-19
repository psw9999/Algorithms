class Solution {
    fun solution(s: String, n: Int): String {
        var sb = StringBuilder()
        for (chr in s) {
            if (chr in 'a'..'z') {
                sb.append(((chr-'a'+n) % 26 + 'a'.toInt()).toChar())
            }
            else if (chr in 'A'..'Z'){
                sb.append(((chr-'A'+n) % 26 + 'A'.toInt()).toChar())
            }else{
                sb.append(" ")
            }
        }
        print(sb)
        return sb.toString()
    }
}