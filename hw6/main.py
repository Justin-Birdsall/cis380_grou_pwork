# Authors: Richard Roy & Justin Birdsall

def branching(required_skills, group_skills, group_size, agents_list, num_agents):
    #if required_skills == bin(0):
    #    return 0
    if required_skills == group_skills:
        return group_size
    if agents_list == []:
        return num_agents + 1
    
    #check if remaining agents can cover the remaining skills
    #if not, return num_agents + 1
    possible_coverage = group_skills

    
    # recursive case
    # include agent
    # use logic here later
    include_group_skills = group_skills | agents_list[0]
    #print(f"include: {bin(include_group_skills)}")
    #print(f"exclude: {bin(group_skills)}")

    # don't include agents that don't contribute to the required skills
    if include_group_skills == group_skills:
        return branching(required_skills, group_skills, group_size, agents_list[1:], num_agents)
    
    include = branching(required_skills, include_group_skills, group_size + 1, agents_list[1:], num_agents)
    #new_possible_coverage = possible_coverage
    exclude = branching(required_skills, group_skills, group_size, agents_list[1:], num_agents)
    
    return min(include, exclude)
    #return include
        
    # exclude agent

if __name__ == "__main__":
    
    input_line = input().split()
    num_candidate_agents = int(input_line[0])
    num_required_skills = int(input_line[1])
    required_skills = [skill for skill in input().split()]
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
    # padding with 0s to make sure all agents have the same number of skills (num_required_skills)
    required_skills_binary = 0
    for skill in required_skills:
        required_skills_binary |= 1 << required_skills.index(skill)

    possible_coverage = 0
    agents_binary = []
    for agent in candidate_agents:
        agent_binary = 0
        #agent_binary = bin(bin(0) for _ in range(num_required_skills))
        #agent_binary = f"{0:0{num_required_skills}b}"
        for skill in agent:
            agent_binary |= 1 << required_skills.index(skill)
            possible_coverage |= 1 << required_skills.index(skill)
        #agent_binary |= agent_binary & required_skills_binary
        agents_binary.append(agent_binary)

    #might do this while getting agents
    # exclude agents that are a subset of other agents
    temp_agents = agents_binary
    temp_agents.sort(reverse=True)

    
    print(branching(required_skills_binary, 0, 0, agents_binary, num_candidate_agents))

    #for agent in agents_binary:
    #    print(bin(agent))

    #print()
    #print(bin(required_skills_binary))

    