# Authors: Richard Roy, Justin Birdsall



if __name__ == "__main__":
    num_ids = int(input())
    ids = {}
    # place holder for the max freq so we can compare without
    # having to check if it exists every time
    ids[-1] = 0
    max_freq = [-1]
    for i in range(num_ids):
        id = int(input().split()[0])
        if id in ids:
            ids[id] += 1
        else:
            ids[id] = 1
            
        # update the max freq
        if ids[id] >= ids[max_freq[0]]:   
                # if id is already in the list,
                # it was previously tied for max freq
                # so we know it is the sole max freq now
                if id in max_freq:
                    max_freq = [id]
                # if it is not, it is now tied for max freq
                # otherwise it would have been in the list
                # already
                else:
                    max_freq.append(id)
    max_freq.sort()
    print(max_freq[0])







