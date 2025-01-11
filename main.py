import multiprocessing
def calculate_sum(start,end):
    return sum(range(start,end +1))
def main():
    N=int(input("enter the number to calculate sum up to (N): "))
    P=int(input("enter the number of processes to use (P): "))
    chunk_size= N//P
    ranges= []
    for i in range(P):
        start=i*chunk_size+1
        end=(i+1)* chunk_size if i < P-1 else N
        ranges.append((start,end))
    with multiprocessing.Pool(P) as pool:
        results=pool.starmap(calculate_sum,ranges)
    total_sum=sum(results)
    print(f"total sum from 1 to {N} is: {total_sum}")
if __name__ == "__main__":
    main()
    