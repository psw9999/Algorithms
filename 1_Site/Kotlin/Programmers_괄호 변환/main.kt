class Solution {
    fun solution(p: String): String {
        var answer = strStack(p)
        return answer
    }

    fun strStack(p: String) : String {
        if (p.length == 0) return ""
        var u = StringBuilder().append(p[0])
        var v = StringBuilder().append(p.slice(1 until p.length))
        var result = ""
        var cnt = 1

        for (i in 1 until p.length) {
            if (p[0] == p[i]) {
                cnt++
            }
            else{
                cnt--
            }
            u.append(p[i])
            v.deleteCharAt(0)
            if (cnt == 0) break
        }
        if (p[0] == '(') {
            u.append(strStack(v.toString()))
            result = u.toString()
        }
        else{
            var temp = "(" + strStack(v.toString()) + ")"
            u.deleteCharAt(0)
            u.deleteCharAt(u.length-1)
            for (i in u.indices) {
                if (u[i] == '(') u[i] = ')'
                else u[i] = '('
            }
            result = temp + u.toString()
        }

        return result
    }
}