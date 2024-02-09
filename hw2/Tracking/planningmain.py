# Authors: Richard Roy, Justin Birdsall


# hash table with ids as keys and hits as values, unique ids, so no need for chaining



if __name__ == "__main__":
    num_ids = int(input())
    # lots of ids, need to find one that has the most hits, but 10^6 is a lot of ids
    # we need to be efficient, so we will use a dictionary to store the ids and their hits
    # that way we can quickly look up the hits for a given id
    # by using a dictionary, we can also easily keep track of the id with the most hits
    # and we can easily update the hits for a given id as we iterate through the logs
    ids = {}
    # when we first find an id, we will set the hits to 1
    # if we find the id again, we will increment the hits
    # this can be done in less than O(n) time
    # because we can look up the id in the dictionary in O(1) time
    # and we can update the hits in O(1) time
    
    # the lowest id num of a tie for most hits
    # will be the one that is printed if there is a tie
    # so we will need to have a way to know which id is the lowest
    
    # we can have a separate dictionary to keep track of the current highest hits (ties) will be resolved by lowest id)
    # and updated as we update the hits for each id, which could cause time issues
    
    curr_suspect = {}   # id: hits, to compare in constant time
    
    for i in range(num_ids):
        id = int(input().split())
        # add to dictionary if not already there
        # if it is already there, increment the hits
        # but this is too slow
        # we can't just use a hash map with the id as the key and initialize the hits to 0
        # because ids could be 0 - 10^12, and we would need to initialize all of them
        # which would take up too much space
        # and time
        # could we use hits as the key and the id as the value?
        # we would need to have collision resolutions, such as chaining, to handle ties
        
        # there are only 1000 unique ids
        
        
        # lets start with a hast table
        
        
        # is there any way we could use two hash tables?
        # one with id as the key and hits as the value
        # and one with hits as the key and id as the value, but with chaining to handle ties?
        # that way we could quickly look up the hits for a given id
        # and quickly look up the id for the highest hits
        # and we could easily update the hits for a given id
        # and we could easily update the highest hits
        
        