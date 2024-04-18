# Authors: Richard Roy & Justin Birdsall
import time

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
                
            

def branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list, agents_dict, num_agents, starttime):
    if time.time() - starttime >= 9.5:
        return best_solution
    if bin(group_skills).count('1') >= num_required_skills:
        return group_size, group
    if agents_list == []:
        return num_agents + 1, group
    
    #check if remaining agents can cover the remaining skills
    #if not, return num_agents + 1
    possible_coverage = group_skills
    
    # recursive case
    # include agent
    # use logic here later
    include_group_skills = group_skills | agents_list[0]

    # don't include agents that don't contribute to the required skills
    # don't think this will be triggered because of the remove_subset function
    if include_group_skills == group_skills:
        return branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list[1:], agents_dict, num_agents, starttime)
    # include agent, exclude later
    new_group = group.copy()
    new_group.append(list(agents_dict.values()).index(agents_list[0]))
    if bin(include_group_skills).count('1') >= num_required_skills:
        best_solution = group_size + 1, new_group
    include = branching(best_solution, num_required_skills, include_group_skills, group_size + 1, new_group, agents_list[1:], agents_dict, num_agents, starttime)
    possible_coverage = group_skills
    for agent in agents_list[1:]:
        possible_coverage |= agent
    if bin(possible_coverage).count('1') < num_required_skills:
        exclude = num_agents + 1, group
    else:
        # exclude agent
        exclude = branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list[1:], agents_dict, num_agents, starttime)
    
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
    
    # exclude agents that are a subset of other agents
    agents_binary = remove_subset(agents_binary)
    group = []
    all_optimized_agents = []
    for agent in agents_binary:
        all_optimized_agents.append(list(agents_dict.keys())[list(agents_dict.values()).index(agent)])
    best_solution = (len(agents_binary), all_optimized_agents)

    ret = branching(best_solution, num_required_skills, 0, 0, group, agents_binary, agents_dict, num_candidate_agents, start_time)
    ret1 = ret[1]
    ret1.sort()
    print(ret[0])
    #unwrapped = [int for int in ret1]
    print(" ".join(str(int) for int in ret1))