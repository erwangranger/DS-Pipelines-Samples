import time

# Record the starting time
start_time = time.time()

import urllib.request
mydestfile='20MB.zip'
print("starting download...")
urllib.request.urlretrieve("http://212.183.159.230/20MB.zip", mydestfile)
print("done")

# Record the ending time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")