# Authors: Richard Roy & Justin Birdsall

import time

import sys

sys.setrecursionlimit(1500)

def remove_subset_iterative(agents, starttime):
    # order most skills to least skills, so we can make more progress in 
    # branching in less time
    #agents.sort(reverse=True)
    stack = []
    stack.append(agents)
    #remove agents that are a subset of another agent
    while stack:
        # if processing takes too long, just break out of the function
        if time.time() - starttime >= 9:
            return stack.pop()
        # pop state from stack
        agents = stack.pop()
        break_flag = False
        for agent in agents:
            if time.time() - starttime >= 9:
                return agents
            if break_flag:
                #break_flag = False
                break
            for other_agent in agents:
                if time.time() - starttime >= 9:
                    return agents
                if break_flag:
                    #reak_flag = False
                    break
                # don't compare agent to itself
                if agent == other_agent:
                    break
                #if agents.index(agent) == agents.index(other_agent):
                #    break
                # other_agent is a subset of agent, remove other_agent
                if agents[agent] | agents[other_agent] == agents[agent]:
                    #agents.remove(other_agent)
                    del agents[other_agent]
                    stack.append(agents)
                    break_flag = True
                    break
                
                if agents[agent] | agents[other_agent] == agents[other_agent]:
                    #agents.remove(agent)
                    del agents[agent]
                    stack.append(agents)
                    break_flag = True
                    break
    #return agents.values()
    return [agent for agent in agents.values()]

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

                

            

def branching_iterative(best_solution, num_required_skills, group_skills, group, agent_index, agents_list, agents_dict, starttime):
    stack = []
    # add initial state to stack
    stack.append((group_skills, group, agent_index))
    # while stack is not empty
    while stack:
        # check if time limit has been reached, return best solution if so (immediately)
        if time.time() - starttime >= 9:
            return best_solution
        # pop state from stack
        state = stack.pop()
        group_skills, group, agent_index = state
        # check if group has all required skills
        if bin(group_skills).count('1') >= num_required_skills:
            # update best solution if new group is better
            if len(group) < best_solution[0]:
                best_solution = len(group), group
            # continue to next state
            continue
        # check if there are no more agents
        if agent_index == len(agents_list):
            # continue to next state, since we can't include or exclude any more agents
            continue
        
        # include agent
        include_group_skills = group_skills | agents_list[agent_index]
        # don't include agents that don't contribute to the required skills
        if include_group_skills == group_skills:
            # continue to next state?
            #continue
            stack.append((group_skills, group, agent_index+1))
            continue
        # prepare new group for include
        include_group = group.copy()
        include_group.append(list(agents_dict.values()).index(agents_list[agent_index]))
        # update best solution if new group is better
        if bin(include_group_skills).count('1') >= num_required_skills:
            if len(include_group) < best_solution[0]:
                best_solution = len(include_group), include_group
        # add include state to stack
        stack.append((include_group_skills, include_group, agent_index+1))
        
        # exclude agent
        # check if remaining agents can cover the remaining skills
        possible_coverage = group_skills
        for agent in agents_list[agent_index+1:]:
            possible_coverage |= agent
        if bin(possible_coverage).count('1') < num_required_skills:
            # continue to next state
            continue
        # add exclude state to stack
        stack.append((group_skills, group, agent_index+1))
        
    return best_solution
        
        
def branching(best_solution, num_required_skills, group_skills, group, agent_index, agents_list, agents_dict, starttime):

    if time.time() - starttime >= 9.9:

        return best_solution

    if bin(group_skills).count('1') >= num_required_skills:

        return len(group), group

    #if agents_list == []:

    if agent_index == len(agents_list):

        #return num_agents + 1, group

        return best_solution

    

    #check if remaining agents can cover the remaining skills

    #if not, return num_agents + 1

    #possible_coverage = group_skills

    

    # recursive case

    # include agent

    include_group_skills = group_skills | agents_list[agent_index]

    # don't include agents that don't contribute to the required skills

    if include_group_skills == group_skills:

        return branching(best_solution, num_required_skills, group_skills, group, agent_index+1, agents_list, agents_dict, starttime)

    new_group = group.copy()

    new_group.append(list(agents_dict.values()).index(agents_list[agent_index]))

    # update best solution if new group is better

    if bin(include_group_skills).count('1') >= num_required_skills:

        best_solution = len(new_group), new_group

    include = branching(best_solution, num_required_skills, include_group_skills, new_group, agent_index+1, agents_list, agents_dict, starttime)

    best_solution = include if include[0] < best_solution[0] else best_solution

    

    

    

    possible_coverage = group_skills

    #for agent in agents_list[1:]:

    for agent in agents_list[agent_index+1:]:

        possible_coverage |= agent

    if bin(possible_coverage).count('1') < num_required_skills:

        #exclude = num_agents + 1, group

        exclude = best_solution

    else:

        # exclude agent

        exclude = branching(best_solution, num_required_skills, group_skills, group, agent_index+1, agents_list, agents_dict, starttime)

    

    return exclude if exclude[0] < include[0] else include

        

# if __name__ == "__main__":

#     start_time = time.time()

    

#     input_line = input().split()

#     num_candidate_agents = int(input_line[0])

#     num_required_skills = int(input_line[1])

#     candidate_agents = []



#     # pairs of lines

#     for _ in range(num_candidate_agents):

#         #line 1 is num of skills they know

#         #line 2 is the skills they know space separated

#         #we don't really care about line 1, we just want line 2 in a list

#         input()

#         candidate_agents.append([skill for skill in input().split()])

    



#     # goal: find smallest number of agents that can cover all the required skills

    

#     # method: store skills in binary form, all skills = 111111, none = 000000, last skill = 100000, etc.



#     # convert required skills to binary for each agent

#     possible_skills = []

#     for agent in candidate_agents:

#         for skill in agent:

#             if time.time() - start_time >= 9.7:

#                 print(len(candidate_agents))

#                 print((i for i in range(len(candidate_agents))))

#                 sys.exit()

#             if skill not in possible_skills:

#                 possible_skills.append(skill)



#     possible_coverage = 0

#     agents_binary = []

#     agents_dict = {}

#     original_index = 0

#     for agent in candidate_agents:

#         agent_binary = 0

#         for skill in agent:

#             if time.time() - start_time >= 9.7:

#                 print(len(candidate_agents))

#                 print((i for i in range(len(candidate_agents))))

#                 sys.exit()

#             agent_binary |= 1 << possible_skills.index(skill)

            

        

#         # no repeated skill sets

#         if agent_binary not in agents_binary:

#             agents_binary.append(agent_binary)

#             agents_dict[original_index] = agent_binary

#         original_index += 1

    

#     # exclude agents that are a subset of other agents

#     #agents_binary = remove_subset(agents_binary)
#     agents_binary = remove_subset_iterative(agents_binary, start_time)

#     group = []

#     all_optimized_agents = []

#     for agent in agents_binary:

#         all_optimized_agents.append(list(agents_dict.keys())[list(agents_dict.values()).index(agent)])

#     best_solution = (len(agents_binary), all_optimized_agents)



#     #ret = branching(best_solution, num_required_skills, 0, 0, group, agents_binary, agents_dict, num_candidate_agents, start_time)

#     #ret = branching(best_solution, num_required_skills, 0, group, 0, agents_binary, agents_dict, start_time)

#     ret = branching_iterative(best_solution, num_required_skills, 0, group, 0, agents_binary, agents_dict, start_time)

#     ret1 = ret[1]

#     ret1.sort()

#     #print("Time: ", time.time() - start_time)

#     print(ret[0])

#     #unwrapped = [int for int in ret1]

#     print(" ".join(str(int) for int in ret1))

if __name__ == "__main__":
    start_time = time.time()
    
    num_candidate_agents, num_required_skills = map(int, input().split())
    original_index = 0
    agents_dict = {}
    agents_binary = []
    all_optimized_agents = []
    unique_skills = []
    candidate_skills = []
    for _ in range(num_candidate_agents):
        input()
        skills = input().split()
        agent_binary = 0
        for skill in skills:
            if skill not in unique_skills:
                unique_skills.append(skill)
            agent_binary |= 1 << unique_skills.index(skill)
        if agent_binary not in agents_binary:
            agents_binary.append(agent_binary)
            agents_dict[original_index] = agent_binary
            all_optimized_agents.append(original_index)
        candidate_skills.append(skills)
        original_index += 1
        
    
    # exclude agents that are a subset of other agents
    #agents_binary = remove_subset_iterative(agents_binary, start_time)
    agents_binary = remove_subset_iterative(agents_dict, start_time)
    best_solution = (original_index, all_optimized_agents)
    group = []
    ret = branching_iterative(best_solution, num_required_skills, 0, group, 0, agents_binary, agents_dict, start_time)
    ret1 = ret[1]
    ret1.sort()
    print(ret[0])
    print(" ".join(str(int) for int in ret1))