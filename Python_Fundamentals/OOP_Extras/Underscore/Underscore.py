class Underscore:
    
    #  map method
    def map(self, iterable, callback):
        for i in range (len(iterable)) :
            iterable[i] = callback(iterable[i])
        return iterable
        
    #  find method
    def find(self, iterable, callback):
        for item in iterable :
            if callback(item) :
                return item
    
    #  filter method
    def filter(self, iterable, callback):
        truth = []
        for item in iterable :
            if callback(item) :
                truth.append(item)
        return truth
    
    # reject method
    def reject(self, iterable, callback):
        reject = []
        for item in iterable :
            if not callback(item) :
                reject.append(item)
        return reject
    

# create an instance of our class & etting our instance to a variable that is an underscore
_ = Underscore() 

print(_.map([1,2,3], lambda x: x*2)) 
# return [2,4,6]

print(_.find([1,2,3,4,5,6], lambda x: x>4)) 
# return the first value that is greater than 4

print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) 
# return [2,4,6]

print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) 
# return [1,3,5]