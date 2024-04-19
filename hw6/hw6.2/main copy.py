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
                
            
def branching_iterative(best_solution, num_required_skills, group_skills, group, agent_index, agents_list, agents_dict, starttime):
    stack = []
    memo = {}
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
        
        # memoization
        #memo_key = (group_skills, group, agent_index)
        
        # different combination of agents can have the same group_skills,
        # but the agents from the index onwards will always contribute the same skills
        memo_key = (group_skills, agent_index)
        if memo_key in memo:
            continue
        
        # check if group has all required skills
        if bin(group_skills).count('1') >= num_required_skills:
            # update best solution if new group is better
            if len(group) < best_solution[0]:
                best_solution = len(group), group
            memo[memo_key] = best_solution
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
        
if __name__ == "__main__":
    start_time = time.time()
    
    num_candidate_agents, num_required_skills = map(int, input().split())
    #input()
    original_index = 0
    agents_dict = {}
    agents_binary = []
    all_optimized_agents = []
    #unique_skills = set()
    unique_skills = []
    candidate_skills = []
    #candidate_skills = [input().split() for _ in range(num_candidate_agents)]
    for _ in range(num_candidate_agents):
        input()
        skills = input().split()
        agent_binary = 0
        for skill in skills:
            if skill not in unique_skills:
                unique_skills.append(skill)
            #agent_binary |= 1 << list(unique_skills).index(skill)
            agent_binary |= 1 << unique_skills.index(skill)
        if agent_binary not in agents_binary:
            agents_binary.append(agent_binary)
            agents_dict[original_index] = agent_binary
            all_optimized_agents.append(original_index)
        candidate_skills.append(skills)
        original_index += 1
        
    
    # exclude agents that are a subset of other agents
    agents_binary = remove_subset(agents_binary)
    best_solution = (original_index, all_optimized_agents)
    # print(f"best_solution: {best_solution}")
    # print(f"num_required_skills: {num_required_skills}")
    # print(f"agents_list: {agents_binary}")
    # print(f"agents_dict: {agents_dict}")
    group = []
    ret = branching_iterative(best_solution, num_required_skills, 0, group, 0, agents_binary, agents_dict, start_time)
    ret1 = ret[1]
    ret1.sort()
    print(ret[0])
    print(" ".join(str(int) for int in ret1))