import time

def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def list_comprehension(n):
    res = [i**2 for i in range(n)]
    return res

final_output = for_loop(5)
final_output_lc = list_comprehension(5)

print(f"Final output using For Loop: \n {final_output}")
print(f"Final output using List Comprehension: \n {final_output_lc}")

begin_loop_timer = time.time()
final_output = for_loop(10**7)
end_loop_timer = time.time()

print(f"Time taken to Run the For Loop based List operation: {round(end_loop_timer-begin_loop_timer,2)} seconds")


begin_lc_timer = time.time()
final_output_lc = list_comprehension(10**7)
end_lc_timer = time.time()

print(f"Time taken to Run the For List Comprehension based List operation: {round(end_lc_timer-begin_lc_timer)} seconds")