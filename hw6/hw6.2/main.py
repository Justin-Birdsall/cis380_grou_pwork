# Authors: Richard Roy & Justin Birdsall
import time

def remove_subset(agents):
    # remove agents that are a subset of another agent
    #temp_agents = agents
    #temp_agents.sort(reverse=True)
    agents.sort(reverse=True)
    for agent in agents:
        for other_agent in agents:
            #if agent == other_agent:
            if agents.index(agent) == agents.index(other_agent):
                break
            #if agents[agent] | agents[other_agent] == agents[other_agent]:
            if agent | other_agent == other_agent:
                agents.remove(agent)
                return remove_subset(agents)
            #elif agents[agent] | agents[other_agent] == agents[agent]:
            elif agent | other_agent == agent:    
                agents.remove(other_agent)
                return remove_subset(agents)
    return agents
                
            

def branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list, agents_dict, num_agents, starttime):
    if time.time() - starttime >= 9.5:
        #return group_size, group
        return best_solution
    #if required_skills == bin(0):
    #    return 0
    #if required_skills == group_skills:
    #    return group_size, group
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
    #print(agents_list[0])
    include_group_skills = group_skills | agents_list[0]
    #print(f"include: {bin(include_group_skills)}")
    #print(f"exclude: {bin(group_skills)}")

    # don't include agents that don't contribute to the required skills
    # don't think this will be triggered because of the remove_subset function
    if include_group_skills == group_skills:
        return branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list[1:], agents_dict, num_agents, starttime)
    # include agent, exclude later
    #group.append(agents_dict[agents_list[0]])
    #group.append(list(agents_dict.values()).index(agents_list[0]))
    new_group = group.copy()
    new_group.append(list(agents_dict.values()).index(agents_list[0]))
    #print("test", group)
    if bin(include_group_skills).count('1') >= num_required_skills:
        best_solution = group_size + 1, new_group
    include = branching(best_solution, num_required_skills, include_group_skills, group_size + 1, new_group, agents_list[1:], agents_dict, num_agents, starttime)
    #new_possible_coverage = possible_coverage
    possible_coverage = group_skills
    for agent in agents_list[1:]:
        possible_coverage |= agent
    #if possible_coverage != required_skills:
    #    exclude = num_agents + 1
    print(bin(possible_coverage).count('1'))
    if bin(possible_coverage).count('1') < num_required_skills:
        #exclude = group_size + 1, group
        exclude = num_agents + 1, group
    else:
        #group.pop()
        #group.remove(list(agents_dict.values()).index(agents_list[0]))
        #group = group[:-1]
        #group.pop()
        print("test2", group)
        #group_size -= 1
        exclude = branching(best_solution, num_required_skills, group_skills, group_size, group, agents_list[1:], agents_dict, num_agents, starttime)
    
    #return (exclude, group) if exclude[0] < include[0] else (include, group.append(list(agents_dict.values()).index(agents_list[0])))
    #print(f"include: {include}")
    #print(f"exclude: {exclude}")
    return exclude if exclude[0] < include[0] else include
    #return include
        
    # exclude agent

if __name__ == "__main__":
    start_time = time.time()
    
    input_line = input().split()
    num_candidate_agents = int(input_line[0])
    num_required_skills = int(input_line[1])
    #required_skills = [skill for skill in input().split()]
    candidate_agents = []

    # pairs of lines
    for _ in range(num_candidate_agents):
        #line 1 is num of skills they know
        #line 2 is the skills they know space separated
        #we don't really care about line 1, we just want line 2 in a list
        input()
        candidate_agents.append([skill for skill in input().split()])
        #candidate_agents.append([])
    

    # goal: find smallest number of agents that can cover all the required skills
    
    # method: store skills in binary form, all skills = 111111, none = 000000, last skill = 100000, etc.

    # convert required skills to binary for each agent
    # padding with 0s to make sure all agents have the same number of skills (num_required_skills)
    #required_skills_binary = 0
    #for skill in required_skills:
    #for skill in range(num_required_skills):
    #    required_skills_binary |= 1 << skill
    
        
    #    required_skills_binary |= 1 << required_skills.index(skill)
    #print(bin(required_skills_binary))
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
        #agent_binary = bin(bin(0) for _ in range(num_required_skills))
        #agent_binary = f"{0:0{num_required_skills}b}"
        for skill in agent:
            #agent_binary |= 1 << required_skills.index(skill)
            #possible_coverage |= 1 << required_skills.index(skill)
            agent_binary |= 1 << possible_skills.index(skill)
            
        #agent_binary |= agent_binary & required_skills_binary
        
        # no repeated skill sets
        if agent_binary not in agents_binary:
            agents_binary.append(agent_binary)
            agents_dict[original_index] = agent_binary
        original_index += 1

    #might do this while getting agents
    # exclude agents that are a subset of other agents
    #temp_agents = agents_binary
    #temp_agents.sort(reverse=True)
    #for agent in temp_agents:
    #    for other_agent in temp_agents:
    #        if agent
    
    # exclude agents that are a subset of other agents
    agents_binary = remove_subset(agents_binary)
    group = []
    all_optimized_agents = []
    for agent in agents_binary:
        all_optimized_agents.append(list(agents_dict.keys())[list(agents_dict.values()).index(agent)])
    best_solution = (len(agents_binary), all_optimized_agents)

    ret = branching(best_solution, num_required_skills, 0, 0, group, agents_binary, agents_dict, num_candidate_agents, start_time)
    #print(f'{ret[0], "\n", ret[1]}')
    ret1 = ret[1]
    ret1.sort()
    print(ret[0])
    #print(int for int in ret1)
    #unwrapped = [int for int in ret1]
    print(" ".join(str(int) for int in ret1))
    #for agent in agents_binary:
    #    print(bin(agent))

    #print()
    #print(bin(required_skills_binary))

    