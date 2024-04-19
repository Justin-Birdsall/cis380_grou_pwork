# Authors: Richard Roy & Justin Birdsall
import time
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
#print(sys.getrecursionlimit())

def remove_subset(agents):
    # remove agents that are a subset of another agent
    agents.sort(reverse=True)
    for agent in agents:
        for other_agent in agents:
            if agents.index(agent) == agents.index(other_agent):
                break
            if agent | other_agent == other_agent:
                agents.remove(agent)
                return remove_subset(agents)
            elif agent | other_agent == agent:    
                agents.remove(other_agent)
                return remove_subset(agents)
    return agents
                
            
def branching_iterative(best_solution, num_required_skills, group_skills, group_size, group, agents_list, agents_dict, starttime):
    
def branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list, agents_dict starttime):
    # time limit, reduce this
    if time.time() - starttime >= 5: #we have 10 seconds, but not sure how long it will take to recurse back
        print("Time limit reached")
        print("returning: ", best_solution)
        return best_solution
    # continuously update best solution as we prune the tree
    if bin(group_skills).count('1') >= num_required_skills:
        print("All required skills covered, updating best solution")
        print(f"best_solution: {best_solution}")
        best_solution = (group_size, group)
    # base case: no longer possible to cover all required skills, ret best solution(prev)
    else:
        print("Not all required skills covered")
        print("returning: ", best_solution)
        return best_solution
    # base case: no more agents to check, end of tree
    if agents_list == []:
        print("No more agents")
        print("returning: ", best_solution)
        return best_solution
    
    
    # include head agent, do nothing, depricate agents list
    print(f"include first, best_solution: {best_solution}")
    include = branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list[1:], agents_dict, starttime)
    print(f"include: {include}")
    new_group = group.copy()
    new_group.append(list(agents_dict.values()).index(agents_list[0]))
    
    # exclude head agent, remove from group, depricate agents list
    
    exclude_group = group
    print(f"_group: {exclude_group}")
    exclude_group.remove(list(agents_dict.values()).index(agents_list[0]))
    print(f"group: {exclude_group}")
    
    possible_coverage = 0#group_skills
    exclude_group_skills = 0
    for agent in exclude_group:
        exclude_group_skills |= agents_dict[agent]
    possible_coverage = exclude_group_skills
    if len(agents_list) > 1:
        print(f"agents_list: {agents_list}")
        for agent in agents_list[1:]:
            possible_coverage |= agent
    print(f"exclude_group_skills: {bin(exclude_group_skills)}")
    print(f"possible_coverage: {bin(possible_coverage)}")
        
    
    # if excluding the agent doesn't cover all required skills, don't exclude
    if bin(possible_coverage).count('1') < num_required_skills:
        print("returning include: ", best_solution)
        return include
    else:
        # exclude agent
        exclude_group_size = group_size - 1
        exclude = branching(best_solution, num_required_skills, exclude_group_skills, exclude_group_size, exclude_group, agents_list[1:], agents_dict, starttime)
        #exclude = branching(best_solution, num_required_skills, exclude_group_skills, group_size, group, agents_list[1:], agents_dict, num_agents, starttime)
    print("returning exclude include: ", exclude if exclude[0] < include[0] else include)
    return exclude if exclude[0] < include[0] else include
        
if __name__ == "__main__":
    start_time = time.time()
    
    input_line = input().split()
    num_candidate_agents = int(input_line[0])
    num_required_skills = int(input_line[1])
    candidate_agents = []

    # pairs of lines
    for _ in range(num_candidate_agents):
        #line 1 is num of skills they know
        #line 2 is the skills they know space separated
        #we don't really care about line 1, we just want line 2 in a list
        input()
        candidate_agents.append([skill for skill in input().split()])
    

    # goal: find smallest number of agents that can cover all the required skills
    
    # method: store skills in binary form, all skills = 111111, none = 000000, last skill = 100000, etc.

    # convert required skills to binary for each agent
    possible_skills = []
    for agent in candidate_agents:
        for skill in agent:
            if skill not in possible_skills:
                possible_skills.append(skill)

    possible_coverage = 0
    agents_binary = []
    agents_dict = {}
    original_index = 0
    for agent in candidate_agents:
        agent_binary = 0
        for skill in agent:
            agent_binary |= 1 << possible_skills.index(skill)
        # no repeated skill sets
        if agent_binary not in agents_binary:
            agents_binary.append(agent_binary)
            agents_dict[original_index] = agent_binary
        original_index += 1
    for skill in possible_skills:
        possible_coverage |= 1 << possible_skills.index(skill)
    
    # exclude agents that are a subset of other agents
    agents_binary = remove_subset(agents_binary)
    group = []
    all_optimized_agents = []
    for agent in agents_binary:
        all_optimized_agents.append(list(agents_dict.keys())[list(agents_dict.values()).index(agent)])
    best_solution = (len(agents_binary), all_optimized_agents)
    
    for agent in agents_binary:
        possible_coverage |= agent

    # testing starting with full group and taking away agents
    #group = [i for i in range(num_candidate_agents)]
    #print all inputs for branching
    print(f"best_solution: {best_solution}")
    print(f"num_required_skills: {num_required_skills}")
    print(f"group_skills: {bin(possible_coverage)}")
    print(f"group_size: {len(all_optimized_agents)}")
    print(f"group: {all_optimized_agents}")
    print(f"agents_list: {agents_binary}")
    print(f"agents_dict: {agents_dict}")
    print(f"num_agents: {num_candidate_agents}")
    print(f"start_time: {start_time}")
    ret = branching(best_solution, num_required_skills, possible_coverage, len(all_optimized_agents), all_optimized_agents, agents_binary, agents_dict, num_candidate_agents, start_time)
    #ret = branching(best_solution, num_required_skills, 0, 0, group, agents_binary, agents_dict, num_candidate_agents, start_time)
    ret1 = ret[1]
    ret1.sort()
    print("Solution:")
    print(ret[0])
    #unwrapped = [int for int in ret1]
    #print(" ".join(str(int) for int in ret1))
    print(ret[1])
    #print(ret1)