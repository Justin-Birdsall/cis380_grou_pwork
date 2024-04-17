'''
Group: Justin Birdsall, Richard Roy
Author: Justin
this is a set cover problem. The universal set is the of all required skills that need to be covered by the company. We are looking for the smallest subset of candidates to COVER ALL skills needed. 

Since the set cover problem is a NP-hard problem, brute forcing the solution is best. Looking at our constraints at most our computation will be of size 2^200 or (1606938044258990275541962092341162602522202993782792835301376) for the subsets
'''
from itertools import combinations

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
        candidate_skills = input().split()
        #get the set of their skills and add it to the candidates for easier processing
        binary_representation = 0
        for skill in candidate_skills:
                binary_representation |= skill_to_bit.get(skill, 0)
        candidates.append(binary_representation)

    # Find the minimum number of candidates needed so set it to inf to do check
    min_candidates = float('inf')
    #start loop at 1 since a subset of 0 would just mean 0 canidates fill the position
    for r in range(1, num_candidates + 1):
        #essentially the thinking is to check if 1 candidate can do this then check if any combination of 2 can cover it and so on
        for subset in combinations(candidates, r):
            #create an empty set and unwrap each tuple to be individual. To get rid of any duplicate skills perform the union and set the covered skills to that value. 
            covered_skills = 0
            for candidate in subset:
                #bitwise or the candidate with covered skills
                covered_skills |= candidate
            #if the binary representation of the subset covers all the skills that means thats the min candidates
            if bin(covered_skills).count('1') == len(required_skills):
                min_candidates = min(min_candidates, r)
    print(min_candidates)


