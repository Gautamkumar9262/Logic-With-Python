#write a python script to find maximum size batch code from a dictionary where key-value in the dictionary are batch codes and data values zise of the batch.

batches={'sa':200,
         'sb':189,
         'sc':207,
         'sd':305,
         'se':280
}
max=0
batch_code=''
for k,v,in batches.items():
    if(v>max):
        max=v
    batch_code=k
print("max size batch code is ",batch_code)
