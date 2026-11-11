# Parent Class
class Employee:
    def __init__(self):
        self.__empId=None
        self.__empName=""
    def setEmpId(self,empId):
        self.__empId=empId
    def getEmpId(self):
        return self.__empId
    def setEmpName(self, empName):
        self.__empName=empName
    def getEmpName(self):
        return self.__empName
# Child class 1   
class RegularEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.__salary=0
        self.__bonus=0
    def setSalary(self, salary):
        self.__salary = salary
    def getSalary(self):
        return self.__salary
    def setBonus(self, bonus):
        self.__bonus = bonus
    def getBonus(self):
        return self.__bonus
# Child class 2
class ContractEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.__payPerHour=0
        self.__contractPeriod=0
    def setPayPerHour(self, payPerHour):
        self.__payPerHour = payPerHour
    def getPayPerHour(self):
        return self.__payPerHour
    def setContractPeriod(self,contractPeriod):
        self.__contractPeriod = contractPeriod
    def getContractPeriod(self):
        return self.__contractPeriod

# Creating objects
regular=RegularEmployee()
regular.setEmpId(201)
regular.setEmpName("Anita")
regular.setSalary(60000)
regular.setBonus(5000)

contract=ContractEmployee()
contract.setEmpId(202)
contract.setEmpName("Vikram")
contract.setPayPerHour(800)
contract.setContractPeriod(12)

print("Regular Employee Details: ")
print("ID:", regular.getEmpId())
print("Name:", regular.getEmpName())
print("Salary:", regular.getSalary())
print("Bonus:", regular.getBonus())

print("\nContract Employee Details: ")
print("ID:", contract.getEmpId())
print("Name:", contract.getEmpName())
print("Pay per hour:", contract.getPayPerHour())
print("Contract period:", contract.getContractPeriod())
