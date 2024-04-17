'''
Group: Justin Birdsall, Richard Roy
Author: Justin 
this is a set cover problem. The universal set is the of all required skills that need to be covered by the company. We are looking for the smallest subset of candidates to COVER ALL skills needed. 

Brute forcing this set cover problem doesn't keep us underneath the time limit. By implementing a branch and bound method to our thinking of finding the minimum set of candidates that have the skills. To do this we can sort on input using a heapq taking some of ricks original thinking and combining it with mine may help reduce those times  
'''
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

    print(min_candidates)