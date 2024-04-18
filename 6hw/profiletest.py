import heapq
import cProfile

if __name__ == "__main__":
    # Input parsing for the number of candidates and skills 
    num_candidates, num_skills = map(int, input().split())
    required_skills = set(input().split())
    #create a dict that has what that required skill is for quick lookup.
    skill_to_bit = {skill: 1 << i for i, skill in enumerate(required_skills)}

    #initialize a data structure and loop through all of the given candidates
    candidates = []
    for _ in range(num_candidates):
        num_candidate_skills = int(input())
        candidate_skills = set(input().split())
        #get the set of their skills and add it to the candidates for easier processing
        binary_representation = 0
        for skill in candidate_skills:
            binary_representation |= skill_to_bit.get(skill, 0)
        candidates.append((binary_representation, len(candidate_skills)))

    # Find the minimum number of candidates needed so set it to inf to do check
    min_candidates = float('inf')
    #initialize the priority queue with the initial solution (no candidates selected, no skills covered, cost = 0)
    pq = [(0, 0, 0)]  

    def run_algorithm():
        global min_candidates
        while pq:
            #pop the partial solution with the lowest cost
            cost, covered_skills, num_selected = heapq.heappop(pq)
            #if the current cost is already greater than the minimum candidates found so far, skip
            if cost >= min_candidates:
                continue
            #check if the current solution covers all required skills
            if covered_skills == (1 << num_skills) - 1:
                min_candidates = min(min_candidates, num_selected)
                break
            #explore the next candidate
            for candidate in candidates:
                new_covered_skills = covered_skills | candidate[0]
                new_cost = num_selected + 1
                #add the new partial solution to the priority queue if it has the potential to improve the upper bound
                if new_covered_skills != covered_skills and new_cost < min_candidates:
                    heapq.heappush(pq, (new_cost, new_covered_skills, new_cost))

    cProfile.run('run_algorithm()', sort='cumulative')
    print(min_candidates)