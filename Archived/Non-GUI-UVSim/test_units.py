from memory_and_file_ops import Allocate_Memory, Get_Value
from load_store_ops import Load, Store
from IO_ops import Read, Write
from arithmetic_ops import Add, Subtract, Divide, Multiply, Check_No_Overflow
from control_ops import Branch, BranchNeg, BranchZero, Halt, No_Infinite_Branching
import pytest

def test_allocate_memory():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    #Testing smallest allocated location
    assert MEM['00'] == '+0001'
    
    #Testing largest allocated location 
    assert MEM['99'] == '+0000'

    #Testing allocated size is correct
    assert len(MEM) == 100

    #Testing allocated key is string not int
    with pytest.raises(KeyError):
        MEM[00]

    #Testing outside allocated size with correct key type (string)
    with pytest.raises(KeyError):
        MEM['100']
    

def test_get_value(capsys):
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)

    #Testing if correct value type of string is returned
    assert type(Get_Value(0,MEM)) == str

    #Testing if correct value is returned at smallest allocated location
    assert Get_Value(0,MEM) == '+0001'
    
    #Testing if correct value is returned at allocated but empy location
    assert Get_Value(10,MEM) == '+0000'

    #Testing if SystemExit is called
    with pytest.raises(SystemExit):
        Get_Value(100,MEM)


def test_load():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = '+0000'
    returned_MEM, returned_ACC = Load('01',MEM,ACC)

    #Testing returned accumulator (ACC) is correct type (str)
    assert type(returned_ACC) == str

    #Testing returned accumulator (ACC) is correct value from allocated location with a value
    assert returned_ACC == '-0002'

    #Testing if returned MEM is the same as the first MEM
    assert MEM == returned_MEM

    #Testing if returned accumulator (ACC) is correct value from allocated but empty location
    returned_MEM_2, returned_ACC_2 = Load('99',MEM,ACC)
    assert returned_ACC_2 == '+0000'

    #Testing if SystemExit is called when MEM at location is not a string
    int_MEM = dict()
    int_MEM['00'] = 1
    with pytest.raises(SystemExit):
        Load('00',int_MEM,ACC)

    #Testing if SystemExit is called when length of a string in mem is not 5
    len_MEM = dict()
    len_MEM['00'] = '+123'
    with pytest.raises(SystemExit):
        Load('00',len_MEM,ACC)

    #testing if SystemExit is called when word in mem doesn't start with + or  -
    sign_MEM = dict()
    sign_MEM['00'] = '12345'
    with pytest.raises(SystemExit):
        Load('00',sign_MEM,ACC)

    #Testing if SystemExit is called when word in MEM passes above systemexit calls but fails due to not being an Int
    str_MEM = dict()
    str_MEM['00'] = '+12W4'
    with pytest.raises(SystemExit):
        Load('00',str_MEM,ACC)

def test_store():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = '+9999'
    returned_MEM, returned_ACC = Store('00',MEM,ACC)

    #Testing if the returned ACC is a string
    assert type(returned_ACC) == str 

    #Testing if original ACC equal to the value at location '00'
    assert returned_MEM['00'] == ACC

    #Testing if the returned ACC and original ACC are the same
    assert returned_ACC == ACC

    #Testing if SystemExit is called when ACC is not a string
    int_ACC = 12345
    with pytest.raises(SystemExit):
        Store('00',MEM,int_ACC)

    #Testing if SystemExit is called when length of a string in ACC is not 5
    len_ACC = '+123'
    with pytest.raises(SystemExit):
        Store('00',MEM,len_ACC)

    #testing if SystemExit is called when ACC doesn't start with + or  -
    sign_ACC = '12345'
    with pytest.raises(SystemExit):
        Store('00',MEM,sign_ACC)

    #Testing if SystemExit is called when ACC passes above systemexit calls but fails due to not being an Int
    str_ACC = '+12W4'
    with pytest.raises(SystemExit):
        Store('00',MEM,str_ACC)

def test_read(monkeypatch):
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)

    #Testing Valid input is returned and matches given input
    monkeypatch.setattr('builtins.input', lambda _: '+1111')
    returned_MEM = Read('00',MEM)
    assert Get_Value(0,returned_MEM) == '+1111'

    #Testing multiple invalid inputs followed by the exit input of 'q'
    with pytest.raises(SystemExit):
        inputs = iter(['1111', '1234', 'Hello', 'Quality', 'quit', 'q'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        returned_MEM_2 = Read('00',MEM)
        Get_Value(0,returned_MEM_2)
    

def test_write(capfd):
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    returned_MEM = Write('00',MEM)
    output, err = capfd.readouterr()

    #Testing if printed word is the expected word
    assert output == '+0001\n'

    #Testing if MEM returned is the same as original MEM
    assert returned_MEM == MEM

    #Testing if SystemExit is called when MEM at location is not a string
    int_MEM = dict()
    int_MEM['00'] = 1
    with pytest.raises(SystemExit):
        Write('00',int_MEM)

    #Testing if SystemExit is called when length of a string in mem is not 5
    len_MEM = dict()
    len_MEM['00'] = '+123'
    with pytest.raises(SystemExit):
        Write('00',len_MEM)

    #testing if SystemExit is called when word in mem doesn't start with + or  -
    sign_MEM = dict()
    sign_MEM['00'] = '12345'
    with pytest.raises(SystemExit):
        Write('00',sign_MEM)

    #Testing if SystemExit is called when word in MEM passes above systemexit calls but fails due to not being an Int
    str_MEM = dict()
    str_MEM['00'] = '+12W4'
    with pytest.raises(SystemExit):
        Write('00',str_MEM)

def test_add():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = "+0000"

    #Testing if ACC is returned as the correct type STR
    returned_MEM, returned_ACC = Add('00',MEM,ACC)
    assert type(returned_ACC) == str

    #Testing if returned_MEM is the same as original MEM
    assert returned_MEM == MEM

    #Testing if ACC is set to the correct value after addition with positive number
    assert returned_ACC == '+0001'

    returned_MEM_2, returned_ACC_2 = Add('01',MEM,ACC)
    #testing if ACC is set to the correct value after addition with negative number
    assert returned_ACC_2 == '-0002'

def test_subtract():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = "+0000"

    #Testing if ACC is returned as the correct type STR
    returned_MEM, returned_ACC = Subtract('01',MEM,ACC)
    assert type(returned_ACC) == str

    #Testing if returned_MEM is the same as original MEM
    assert returned_MEM == MEM

    #Testing if ACC is set to the correct value after Subtracting and result is positive
    assert returned_ACC == '+0002'

    returned_MEM_2, returned_ACC_2 = Subtract('00',MEM,ACC)
    #testing if ACC is set to the correct value after subtracting and resutl is negative
    assert returned_ACC_2 == '-0001'


def test_divide():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = "+0009"

    #Testing if ACC is returned as the correct type STR
    returned_MEM, returned_ACC = Divide('02',MEM,ACC)
    assert type(returned_ACC) == str

    #Testing if returned_MEM is the same as original MEM
    assert returned_MEM == MEM

    #Testing if ACC is set to the correct value after dividing and result is positive
    assert returned_ACC == '+0003'

    ACC = '+0010'
    returned_MEM_2, returned_ACC_2 = Divide('01',MEM,ACC)
    #testing if ACC is set to the correct value after dividing and resutl is negative
    assert returned_ACC_2 == '-0005'


def test_multiply():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = "+0002"

    #Testing if ACC is returned as the correct type STR
    returned_MEM, returned_ACC = Multiply('02',MEM,ACC)
    assert type(returned_ACC) == str

    #Testing if returned_MEM is the same as original MEM
    assert returned_MEM == MEM

    #Testing if ACC is set to the correct value after multiplying and result is positive
    assert returned_ACC == '+0006'

    returned_MEM_2, returned_ACC_2 = Multiply('01',MEM,ACC)
    #testing if ACC is set to the correct value after multiplying and resutl is negative
    assert returned_ACC_2 == '-0004'
    
def test_check_no_overflow():
    #Testing if valid number in the range of -9999 and 9999 returns true
    assert Check_No_Overflow(9999) == True
    assert Check_No_Overflow(-9999) == True
    assert Check_No_Overflow(0) == True

    #Testing if systemexit is called when range is < -9999 or > 9999
    with pytest.raises(SystemExit):
        assert Check_No_Overflow(10000)

    with pytest.raises(SystemExit):
        assert Check_No_Overflow(-10000)

def test_branch():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    PC = 0

    returned_MEM, returned_PC, returned_branched = Branch('03',MEM,PC)

    #Testing if PC is returned as the correct type int
    assert type(returned_PC) == int

    #Testing if PC returned is the correct value 
    assert returned_PC == 3

    #Testing if returned_branced status is true
    assert returned_branched == True

    #Testing if returned_MEM is the same as delivered MEM
    assert returned_MEM == MEM

    #Testing if program exits on infinite branch
    with pytest.raises(SystemExit):
        assert Branch('00',MEM,PC)


def test_branchneg():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = '-0001'
    PC = 0

    returned_MEM, returned_ACC, returned_PC, returned_branched = BranchNeg('03',MEM,ACC,PC)

    #Testing if PC is returned as the correct type int
    assert type(returned_PC) == int

    #Testing if returned_branced status is true
    assert returned_branched == True

    #Testing if PC returned is the correct value when branched is true
    assert returned_PC == 3

    #Testing if returned_MEM is the same as delivered MEM
    assert returned_MEM == MEM

    #Testing if program exits on infinite branch
    with pytest.raises(SystemExit):
        assert BranchNeg('00',MEM,ACC,PC)

    #Testing if returned ACC is correct type
    assert type(returned_ACC) == str

    #Testing if returned ACC is the same as passed ACC
    assert returned_ACC == ACC

    #Testing if returned branched status is False
    ACC_2 = '+0000'
    returned_MEM_2, returned_ACC_2, returned_PC_2, returned_branched_2 = BranchNeg('03',MEM,ACC_2,PC)
    assert returned_branched_2 == False

    #Testing if PC returned is the correct value when branched is False
    assert returned_PC_2 == PC


def test_branchzero():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = '+0000'
    PC = 0

    returned_MEM, returned_ACC, returned_PC, returned_branched = BranchZero('03',MEM,ACC,PC)

    #Testing if PC is returned as the correct type int
    assert type(returned_PC) == int

    #Testing if returned_branced status is true
    assert returned_branched == True

    #Testing if PC returned is the correct value when branched is true
    assert returned_PC == 3

    #Testing if returned_MEM is the same as delivered MEM
    assert returned_MEM == MEM

    #Testing if program exits on infinite branch
    with pytest.raises(SystemExit):
        assert BranchZero('00',MEM,ACC,PC)

    #Testing if returned ACC is correct type
    assert type(returned_ACC) == str

    #Testing if returned ACC is the same as passed ACC
    assert returned_ACC == ACC

    #Testing if returned branched status is False
    ACC_2 = '+0001'
    returned_MEM_2, returned_ACC_2, returned_PC_2, returned_branched_2 = BranchZero('03',MEM,ACC_2,PC)
    assert returned_branched_2 == False

    #Testing if PC returned is the correct value when branched is False
    assert returned_PC_2 == PC  

def test_halt():
    #Testing that when halt is call system exit is called
    with pytest.raises(SystemExit):
        assert Halt()
    
def test_no_infinite_branching():
    #Testing when PC and action Numbers are not the same returns true
    assert No_Infinite_Branching(1,'02') == True

    #Testing when PC and action Numbers are the same, system exit
    with pytest.raises(SystemExit):
        assert No_Infinite_Branching(1,'01')
    