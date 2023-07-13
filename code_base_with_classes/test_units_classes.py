from data_loader import DataLoader
from data_model import DataModel
from load_store_ops_v2 import Load, Store
from IO_ops_v2 import Read, Write
from arithmetic_ops_v2 import Add, Subtract, Divide, Multiply, Check_No_Overflow
from control_ops_v2 import Branch, BranchNeg, BranchZero, Halt, No_Infinite_Branching
import pytest

class testingWindow():
    def appendOutput(self,value):
        print(value)

testWindow = testingWindow()


def test_allocate_memory():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    #Testing smallest allocated location
    assert mem.get_mem_value(0) == 1
    
    #Testing largest allocated location 
    assert mem.get_mem_value(99) == 0

    #Testing allocated size is correct
    assert mem.mem_size == 100

    #Testing accessing value with string (should fail)
    with pytest.raises(TypeError):
        mem.get_mem_value('00')

    #Testing outside allocated size with correct key type (string)
    with pytest.raises(MemoryError):
        mem.get_mem_value(100)

def test_get_value():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())

    #Testing if correct value type of int is returned
    assert type(mem.get_mem_value(0)) == int

    #Testing if private variable is stored as str
    assert type(mem._private_MEM['00']) == str

    #Testing if correct value is returned at smallest allocated location
    assert mem.get_mem_value(0) == 1
    
    #Testing if correct value is returned at allocated but empy location
    assert mem.get_mem_value(10) == 0

    #Testing if keyError is called
    with pytest.raises(MemoryError):
        mem.get_mem_value(100)


def test_load():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    Load(1,mem,testWindow)

    #Testing returned accumulator (ACC) is correct type (int)
    assert type(mem.get_acc()) == int

    #Testing returned accumulator (ACC) is correct value from allocated location with a value
    assert mem.get_acc() == -2

    #Testing if valueError is called when MEM at location is not a valid input
    int_MEM = DataModel({'00':'abcd'})
    with pytest.raises(ValueError):
        Load(0,int_MEM,testWindow)


def test_store():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    Store(0,mem,testWindow)

    #Testing returned accumulator (ACC) is correct type (int)
    assert type(mem.get_acc()) == int

    #Testing if original ACC equal to the value at location '00'
    assert mem.get_acc() == mem.get_mem_value(0)


# def test_read(monkeypatch):
    # data = DataLoader(100,True,'test_files/unit_tests.txt')
    # mem = DataModel(data.get_data())
    # #Testing Valid input is returned and matches given input
    # monkeypatch.setattr('builtins.input', lambda _: '+1111')
    # Read(0,mem,testWindow)
    # assert  mem.get_mem_value(0) == 1111

    # #Testing multiple invalid inputs followed by the exit input of 'q'
    # inputs = iter(['10000', '-12345', 'Hello', 'Quality', 'quit', 'q'])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # assert Read(0,mem,testWindow) == None
    # assert mem._private_PC == 'HALT'

    

def test_write(capfd):
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    Write(0,mem,testWindow)
    output, err = capfd.readouterr()

    #Testing if printed word is the expected word
    assert output == '1\n'

    #Testing if ValueError is called when MEM at location is not a string
    int_MEM = DataModel({'00':'abcd'})
    with pytest.raises(ValueError):
        Write(0,int_MEM,testWindow)

    #Testing if ValueError is called when MEM at location is not a valid input
    int_MEM = DataModel({'00':'abcd'})
    with pytest.raises(ValueError):
        Write(0,int_MEM,testWindow)

    #Testing if SystemExit is called when value of data > 9999 or < -9999
    len_MEM =  DataModel({'00':'+10000', '01':'-10000'})
    assert Write(0,len_MEM,testWindow) == None
    assert len_MEM._private_PC == 'HALT'

    assert Write(1,len_MEM,testWindow) == None
    assert len_MEM._private_PC == 'HALT'

def test_add():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())

    Add(0,mem,testWindow)
    #Testing if ACC is still the correct type STR
    assert type(mem._private_ACC)== str

    #Testing if returned ACC is correct
    assert mem.get_acc() == 1

    #Testing if ACC is set to the correct value after addition with positive number
    assert mem._private_ACC == '+0001'


def test_subtract():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())

    #Testing if ACC is returned as the correct type STR
    Subtract(1,mem,testWindow)
    assert type(mem._private_ACC) == str

    #Testing if ACC is set to the correct value after Subtracting and result is positive
    assert mem._private_ACC == '+0002'

    #Testing if returned ACC is correct
    assert mem.get_acc() == 2

    Subtract(0,mem,testWindow)
    #testing if ACC is set to the correct value after subtracting and resutl is negative
    assert mem.get_acc() == 1


def test_divide():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data(),'+0009')

    #Testing if ACC is returned as the correct type INT
    Divide(2,mem,testWindow)
    assert type(mem.get_acc()) == int

    #Testing if ACC in mem is still correct type STR
    assert type(mem._private_ACC) == str

    #Testing if ACC is set to the correct value after dividing and result is positive
    assert mem.get_acc() == 3

    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data(),'+0010')
    #Testing if ACC is set to the correct value after dividing and result is negative
    Divide(1,mem,testWindow)
    assert mem.get_acc() == -5


def test_multiply():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data(),'+0002')

    #Testing if ACC is returned as the correct type INT
    Multiply(2,mem,testWindow)
    assert type(mem.get_acc()) == int

    #Testing if ACC in mem is still correct type STR
    assert type(mem._private_ACC) == str

    #Testing if ACC is set to the correct value after multiplying and result is positive
    assert mem.get_acc() == 6

    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data(),'+0002')
    Multiply(1,mem,testWindow)
    #testing if ACC is set to the correct value after multiplying and resutl is negative
    assert mem.get_acc() == -4
    
def test_check_no_overflow():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    #Testing if valid number in the range of -9999 and 9999 returns true
    assert Check_No_Overflow(9999,mem) == True
    assert Check_No_Overflow(-9999,mem) == True
    assert Check_No_Overflow(0,mem) == True

    #Testing if systemexit is called when range is < -9999 or > 9999
    assert Check_No_Overflow(10000,mem) == None
    assert mem._private_PC == 'HALT'
    
    assert Check_No_Overflow(-10000,mem) == None
    assert mem._private_PC == 'HALT'

def test_branch():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())

    result = Branch(3,mem,testWindow)

    #Testing if PC is returned as the correct type int
    assert type(mem.get_pc()) == int

    #Testing if PC returned is the correct value 
    assert mem.get_pc() == 3

    #Testing if returned_branced status is true
    assert result == True

    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    #Testing if program exits on infinite branch
    assert Branch(0,mem,testWindow) == False


def test_branchneg():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data(),'-0001')

    result = BranchNeg(3,mem,testWindow)

    #Testing if PC is returned as the correct type int
    assert type(mem.get_pc()) == int

    #Testing if returned_branced status is true
    assert result == True

    #Testing if PC returned is the correct value when branched is true
    assert mem.get_pc() == 3

    #Testing if returned ACC is correct type INT
    assert type(mem.get_acc()) == int

    #Testing if private acc value is still correct type STR
    assert type(mem._private_ACC) == str

    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    #Testing if program exits on infinite branch
    assert BranchNeg(0,mem,testWindow) == False
    assert mem._private_PC == 'HALT'

    #Testing if returned branched status is False
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    result = BranchNeg(3,mem,testWindow)
    assert result == False

def test_branchzero():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())

    result = BranchZero(3,mem,testWindow)

    #Testing if PC is returned as the correct type INT
    assert type(mem.get_pc()) == int

    #Testing if returned_branced status is true
    assert result == True

    #Testing if PC returned is the correct value when branched is true
    assert mem.get_pc() == 3

    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    #Testing if program exits on infinite branch:
    assert BranchZero(0,mem,testWindow) == False
    assert mem._private_PC == 'HALT'

    #Testing if returned ACC is correct type
    assert type(mem.get_acc()) == int

    #Testing if private ACC type is still STR
    assert type(mem._private_ACC) == str

    #Testing if returned branched status is False
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data(),'+0001')
    result = BranchZero(3,mem,testWindow)
    assert result == False

def test_halt():
    #Testing that when halt is call system exit is called
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    assert Halt(mem) == None
    assert mem._private_PC == 'HALT'
    
def test_no_infinite_branching():
    data = DataLoader(100,True,'test_files/unit_tests.txt')
    mem = DataModel(data.get_data())
    #Testing when PC and action Numbers are not the same returns true
    assert No_Infinite_Branching(1,2,mem) == True

    #Testing when PC and action Numbers are the same, system exit
    assert No_Infinite_Branching(1,1,mem) == None
    assert mem._private_PC == 'HALT'
    