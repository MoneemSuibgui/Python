


class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
        
    def say_hello(self):
        return f"hello {self.first_name} {self.last_name}"


user = User("Moneem","Suibgui")
owner=user.say_hello()

print(owner)
print(__name__)
if __name__ == "__main__":
    print("exiting my assignment work correctly")
else:
    print("my work is done")