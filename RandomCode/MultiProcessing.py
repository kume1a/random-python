import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print("Sleeping for {} second(s)".format(seconds))
    time.sleep(seconds)
    # print("Done sleeping")
    return "Done sleeping"

if __name__=="__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = executor.map(do_something,secs)
        for p in results:
            print(p)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # results = [executor.submit(do_something,1) for _ in range(100)]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #     p1 = executor.submit(do_something,1)
        #     print(p1.result())




    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.2]) 
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    print("Finished in {} second(s)".format(round(time.perf_counter()-start),2))