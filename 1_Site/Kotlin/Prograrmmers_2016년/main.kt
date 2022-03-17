class Solution {
    fun solution(x: Int): Boolean {
        var temp = x.toString()
        var hisad : Int = 0
        for (i in 0..(temp.length)-1) {
            hisad += temp[i].toString().toInt()
        }
        if (x%hisad == 0) {
            return true
        }else{
            return false
        }
    }
}