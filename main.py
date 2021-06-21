def maxWater(arr, n) :
     

    res = 0; 
    i=0;
     

    for i in range(1, n - 1) : 
         
 
        left =int(arr[i]); 
        for j in range(i) :
            left = max(left, arr[j]); 
         

        right = arr[i]; 
         
        for j in range(i + 1 , n) : 
            right = max(right, arr[j]);
             

        res = res + (min(left, right) - arr[i]); 
 
    return res; 
 

if __name__ == "__main__" : 
 
    arr =[];
    n =int(input("Enter the number of Walls or gaps "))
    i=0
    for i in range(0, n):
        h =int(input("Enter the height of walls "))
        arr.append(h)
    
    print("Max water that can be stored is: ",maxWater(arr, n))
    
