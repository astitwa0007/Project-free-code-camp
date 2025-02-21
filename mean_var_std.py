import numpy as np

def check_list(lst):
    if len(lst) < 9 or len(lst)>9:
        raise ValueError("List must contain nine numbers.")
    return "List is valid."



def Calaculate(a:list)->dict:
    try:
      check_list(a)  
    except ValueError as e:
      print(e)

    arr=np.array(a).reshape((3,3))


    results= {
        "mean":[list(np.mean(arr,axis=0)),list(np.mean(arr,axis=1)),np.mean(arr.flatten())],

        "variance":[list(np.var(arr,axis=0)),list(np.var(arr,axis=1)),np.var(arr.flatten())],

        "standard deviation":[list(np.std(arr,axis=0)),list(np.std(arr,axis=1)),np.std(arr.flatten())],

        "max":[list(np.max(arr,axis=0)),list(np.max(arr,axis=1)),np.max(arr.flatten())],

        "min":[list(np.min(arr,axis=0)),list(np.min(arr,axis=1)),np.min(arr.flatten())],

        "sum":[list(np.sum(arr,axis=0)),list(np.sum(arr,axis=1)),np.sum(arr.flatten())],
    }


    return results



data_list=list(map(int,input("Enter: ").split()))

print(Calaculate(data_list))
