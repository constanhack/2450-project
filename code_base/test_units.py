from memory_and_file_ops import Allocate_Memory, Get_Value, File_Picker
from load_store_ops import Load, Store
from IO_ops import Read, Write
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
    first_MEM, first_ACC = Load('01',MEM,ACC)

    #Testing returned accumulator (ACC) is correct type (str)
    assert type(first_ACC) == str

    #Testing returned accumulator (ACC) is correct value from allocated location with a value
    assert first_ACC == '-0002'

    #Testing if returned MEM is the same as the first MEM
    assert MEM == first_MEM

    #Testing if returned accumulator (ACC) is correct value from allocated but empty location
    second_MEM, second_ACC = Load('99',MEM,ACC)
    assert second_ACC == '+0000'

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
    first_MEM, first_ACC = Store('00',MEM,ACC)

    #Testing if the returned ACC is a string
    assert type(first_ACC) == str 

    #Testing if original ACC equal to the value at location '00'
    assert first_MEM['00'] == ACC

    #Testing if the returned ACC and original ACC are the same
    assert first_ACC == ACC

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
    first_MEM = Read('00',MEM)
    assert Get_Value(0,first_MEM) == '+1111'

    #Testing multiple invalid inputs followed by the exit input of 'q'
    with pytest.raises(SystemExit):
        inputs = iter(['1111', '1234', 'Hello', 'Quality', 'quit', 'q'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        second_MEM = Read('00',MEM)
        Get_Value(0,second_MEM)
    

def test_write(capfd):
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    first_MEM = Write('00',MEM)
    output, err = capfd.readouterr()

    #Testing if printed word is the expected word
    assert output == '+0001\n'

    #Testing if MEM returned is the same as original MEM
    assert first_MEM == MEM

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



