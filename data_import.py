def get_data(file):
    raw=open(file)
    status=[]
    gender=[]
    dept=[]
    count=[]
    data=[status,gender,dept,count]
    # the data is just an array of subarrays for the different categories
    for line in raw:
        i=0
        for datum in line.split(','):
            data[i].append(datum)# append each data point to the appropriate subarray
            i+=1
    raw.close()
    return data
