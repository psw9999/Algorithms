import java.util.*

class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var stack = Stack<Int>()
        var result = 0
        moves.forEach {
            for (i in board.indices) {
                if (board[i][it-1] == 0) continue
                if (stack.isNotEmpty() && stack.peek() == board[i][it-1]) {
                    result += 2
                    stack.pop()
                }else{
                    stack.push(board[i][it-1])
                }
                board[i][it-1] = 0
                break
            }
        }
        return result
    }
}