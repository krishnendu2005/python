try:
    10+"hello"
except NameError as err:
    print("name error",err)   
except TypeError as err:
    print("type error",err)  
except ValueError as err:
    print("value error",err)    
except:
    print("something went wrong")  