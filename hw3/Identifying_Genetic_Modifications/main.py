# Authors: Richard Roy, Justin Birdsall

if __name__ == "__main__":
    # Input: N number of genes in genome for this animal
    # next line: N values indicating the IDs of each gene
    # NOTE: originally all IDs were in correct sorted order 

    # Output: yes or no, (yes if it is sorted or can be swapped or reversed to be sorted)
    # (no if it cannot be sorted or swapped or reversed to be sorted)
    # if yes, then next line is either swap, followed by the two indices to swap (starting at 1)
    # or reverse, folllowed by the first and last positions that need to be reversed
    
    # IF BOTH: use swap option
    num_genes = int(input())
    gene_ids = input().split()
    # convert gene_ids to integers
    gene_ids = [int(gene) for gene in gene_ids]

    # PLAN: make copy of gene_ids, sort it, then compare to original
    # if they are the same, then it is already sorted
    # if not, then we need to figure out if it can be sorted with a swap or reverse
    gene_ids_sorted = sorted(gene_ids)

    #print(gene_ids)
    #print(gene_ids_sorted)
    if gene_ids == gene_ids_sorted:
        print("yes")
        
    else:
        #print("no")
        # PLAN: find the first and last index that are different
        # then check if the list can be sorted by swapping those two indices
        # if not, then check if the list can be sorted by reversing the list between those two indices
        # if neither, then print no
        first_diff = -1
        last_diff = -1
        for i in range(num_genes):
            if gene_ids[i] != gene_ids_sorted[i]:
                first_diff = i
                break
        #for i in range(num_genes-1, -1, -1):
        for i in range(num_genes-1, first_diff, -1):
            if gene_ids[i] != gene_ids_sorted[i]:
                last_diff = i
                break
        # make new copy of gene_ids to test swap and reverse
        gene_ids_swap = gene_ids.copy()
        # test swap
        holder = gene_ids_swap[first_diff]
        gene_ids_swap[first_diff] = gene_ids_swap[last_diff]
        gene_ids_swap[last_diff] = holder
        # compare gene_ids_copy to gene_ids_sorted
        if gene_ids_swap == gene_ids_sorted:
            print("yes")
            print("swap", first_diff+1, last_diff+1)
        else:
            # test reverse
            #               # before first diff same   # between first and last diff reversed   # after last diff same
            gene_ids_reverse = gene_ids[:first_diff] + gene_ids[first_diff:last_diff+1][::-1] + gene_ids[last_diff+1:]
            if gene_ids_reverse == gene_ids_sorted:
                print("yes")
                print("reverse", first_diff+1, last_diff+1)
            else: 
                print("no")