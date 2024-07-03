import java.util.*

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0
        val q = LinkedList<Pair<Int, Int>>()
        var idx = 0
        for (priority in priorities) {
            q.add(Pair(idx, priority))
            idx += 1
        }
        while(q.isNotEmpty()) {
            val current = q.remove()
            val (index, priority) = current
            
            if (q.any{it.second > priority}) {
                q.add(current)
            } else {
                answer += 1
                if (index == location) {
                    return answer
                }
            }
        }
        return answer
    }
}