# Authors: Richard Roy, Justin Birdsall

if __name__ == "__main__":

    # input: firsrt line two ints
    # first: n: number of missions
    # second: m: number of available agents for missions

    # second line: n space-separated positive ints
    # each describes the respective mission's cost

    # output: total cost for all missions

    # NOTE: each agent will increase their cost for each additional mission they take on
    # after the first mission (0 missions = cost, 1 = cost + cost, 2 = cost + 2cost, etc.)

    # PLAN: convert num agents to a dict with amount of missions gone on as the key
    # use this value to calculate the cost of each mission (cost + cost * dict:value)
    #if 0, cost + 0, if 1 cost + cost, if 2 cost + cost *2, etc.

    # from this, we can calculate the total cost of all missions
    # we just need to find the lowest cost total
   
    # get first input
    input_line = input().split()
    num_missions = int(input_line[0])
    num_agents = int(input_line[1])

    # convert agents into dictionary entries
    agents = {id:0 for id in range(num_agents)}

    # get second input
    mission_costs = input().split()
    # convert mission_costs to list of ints
    mission_costs = list((int(i) for i in mission_costs))

    # all data properly collected/converted

    # calculate the lowest cost for all missions

    # sort the mission costs by "priority"(cost), don't
    # want the repeat agents to take on the most expensive missions
    # after already taking on others

    # sort the mission costs
    # iterate backwards to allow pop()
    mission_costs.sort()
    #mission_costs.reverse()
    #print(mission_costs)

    # iterate backwards throught mission costs
    # iterate through agents
    # add the cost of the mission to the total cost
    # via popping the mission cost from the mission_costs list
    # and applying the algorithm to calculate the cost of the mission
    # from the agent's mission count
    # increment the agent's mission count
    total_cost = 0

    # "pointer" to most recently "used" agent
    last_agent_id = -1

    #loop backwards through mission costs
    for mission_cost in reversed(mission_costs):
        # wrapping agent id
        last_agent_id = last_agent_id + 1
        if last_agent_id == num_agents:
            last_agent_id = 0
        # calculate cost of mission
        total_cost += mission_cost + (mission_cost * agents[last_agent_id])
        # increment agent's mission count
        agents[last_agent_id] += 1
    
    print(total_cost)