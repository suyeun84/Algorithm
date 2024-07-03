import java.util.*

class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = IntArray(numbers.size){-1}
        var stack = Stack<Pair<Int,Int>>()
        
        for ((index,number) in numbers.withIndex()) {
            while (stack.isNotEmpty() && stack.peek().second < number) {
                val (i, n) = stack.pop()
                answer[i] = number
            }
            stack.push(Pair(index, number))
        }
        
        return answer
    }
}