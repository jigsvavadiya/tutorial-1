# class Result:
            # def __init__(slf,phy,chem,math):
                        #   slf.phy=phy
                        #   slf.chem=chem
                        #   slf.math=math
                        #   slf.sco=20
            # value="7dgdg"            
            # def printavg(self,name):
                        #   self.name=name
                        #   return name
       
# rollone=Result()
# rollone.printavg("jgnesh")
# print(rollone.name)
# rollone.printavg("gog")
# print(rollone.name)
# print(rollone.value)





# class three:
    #    def __init__(self):
            #    self.val=input("What value?")
# t=three()
# print(t.val)





# class demo:
    #    def __new__(self):
            #   return 'dataflair'
# d=demo()
# print(type(d))




# class citrus:
    # def __init__(self):
            #    self.detoxifying=True
    # def show(self):
            # if self.detoxifying==True:
                # print("I detoxify") 
            # else: 
                # print("I do not detoxify")
# kumquat=citrus()
# kumquat.show()





# class color:
        # def show(self):
            #    print("You can see me")
# orange=color()
# orange.show()
# class one:
#        def __init__(self):
        #        print("First constructor")
#        def __init__(self):
        #        print("Second constructor")
#        def __init__(self):
        #        print("Thrd constructor")       
# o=one()


class Vehicle:
        def start(self):
                print("Starting engine")
        def stop(self):
                print("Stopping engine")                            
class TwoWheeler(Vehicle):
        def say(self):
                super().start()
                print("I have two wheels")
                super().stop()                            
Pulsar=TwoWheeler()
Pulsar.say()