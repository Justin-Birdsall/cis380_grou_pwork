import subprocess
import polars as pl
import random

def parse_timing(time_str):
    time_str = time_str.split("\n")
    timings = {"real": None, "user": None, "sys": None}
    for line in time_str:
        if not any([key in line for key in timings]):
            continue
        k, t = line.strip().split("\t")
        m = float(t.split("m")[0])
        s = float(t.split("m")[-1].replace("s", ""))
        timings[k] = s + (m*60)
    return timings

if __name__ == "__main__":
    
    # variants
    variants = 100
    



    # Generate target values 1 --> 10000
    #targets = [random.randint(0, 1000000) for _ in range(50)]
    #targets.sort()

    # How many replicates to run each input size?
    replicates = 5

    timing_data = {"rep_id": [], "method": [], "input_size": [], "time": []}
    cnt = 0
    #for n in targets:
    for i in range(variants):
        cnt += 1
        # generate input
        f = open("input_test.txt", "w")

        # first line
        n = random.randint(1, 107)
        k = random.randint(1, 1000)
        if k > n:
            k = random.randint(1, n)
        f.write(f"{n} {k}")
        
        # next N lines
        for i in range(n):
            f.write(f"\n{random.randint(1, 1000000000)}")
        f.close()
        
        print(f"Timing input size {n} foilable {k} ({cnt} / {variants})")
        # ignoring replicates for now
        for r in range(replicates):
        
            # Time original
            cmd = f"time python3 HW3.1_original.py < input_test.txt"
            output = subprocess.run(cmd, shell=True, capture_output=True, check=True)
            timing = parse_timing(output.stderr.decode("UTF-8"))
            timing_data["rep_id"].append(r)
            timing_data["time"].append(timing["user"] + timing["sys"])
            timing_data["method"].append("original-py")
            timing_data["input_size"].append(n)
            
            # Time optimized
            cmd = f"time python3 HW3.1_optimized.py < input_test.txt"
            output = subprocess.run(cmd, shell=True, capture_output=True, check=True)
            timing = parse_timing(output.stderr.decode("UTF-8"))
            timing_data["rep_id"].append(r)
            timing_data["time"].append(timing["user"] + timing["sys"])
            timing_data["method"].append("optimized-py")
            timing_data["input_size"].append(n)
        
    timing_df = pl.DataFrame(data = timing_data)
    timing_df.write_csv("HW3.1_timing.csv")
    print(timing_df)
    # print average time for each method
    print(timing_df.group_by("method").agg(pl.col("time").mean()).sort("method"))

        



    #     cnt += 1
    #     coins_str = " ".join(map(str, coins))
    #     print(f"Timing input size {n} ({cnt} / {len(targets)})")
    #     for r in range(replicates):
    #         # Time exact-change-dp.py
    #         cmd = f"time python3 exact-change-dp.py --target {n} --coins {coins_str}"
    #         output = subprocess.run(cmd, shell=True, capture_output=True, check=True)
    #         timing = parse_timing(output.stderr.decode("UTF-8"))
    #         timing_data["rep_id"].append(r)
    #         timing_data["time"].append(timing["user"] + timing["sys"])
    #         timing_data["method"].append("dp-py")
    #         timing_data["input_size"].append(n)

    #         # Time ec-dp
    #         cmd = f"time ./ec-dp {n} {coins_str}"
    #         output = subprocess.run(cmd, shell=True, capture_output=True, check=True)
    #         timing = parse_timing(output.stderr.decode("UTF-8"))
    #         timing_data["rep_id"].append(r)
    #         timing_data["time"].append(timing["user"] + timing["sys"])
    #         timing_data["method"].append("dp-cpp")
    #         timing_data["input_size"].append(n)

    # timing_df = pl.DataFrame(data = timing_data)
    # timing_df.write_csv("exact-change-timing.csv")
    # print(timing_df)
