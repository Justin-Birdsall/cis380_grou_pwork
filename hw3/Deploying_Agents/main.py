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
   
    pass