
 #Multiplication tables from 2 to 10
     for num in range(2, 11):  
         print(f"\n--- Table of {num} ---")  
         for i in range(1, 11):  
             print(f"{num} x {i} = {num * i}")