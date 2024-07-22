t=int(input("Enter time in second: "))
hr=0
min=0
sec=0
if (t>0):
    if(t>3600): 
        hr = t//3600    
    if(t%3600>60):
        t=t%3600
        min = t//60
    t=t%60
    sec=t
    print(hr,"hr",min,"min",sec,"sec")
else :
    print("Error")    
