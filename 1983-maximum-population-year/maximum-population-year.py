class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        births = sorted(log[0] for log in logs)
        deaths = sorted(log[1] for log in logs)

        i, j = 0, 0
        cur_pop = 0
        max_pop = 0
        best_year = 0

        while i < len(births):
            if births[i] < deaths[j]:
                cur_pop += 1
                if cur_pop > max_pop:
                    max_pop = cur_pop
                    best_year = births[i]
                i += 1
            else:
                cur_pop -= 1
                j += 1

        return best_year