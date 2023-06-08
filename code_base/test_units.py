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

def test_store():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = '+9999'
    first_MEM, first_ACC = Store('00',MEM,ACC)
    assert first_MEM['00'] == ACC
    assert first_ACC == ACC

def test_read(monkeypatch):
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    monkeypatch.setattr('builtins.input', lambda _: '+1111')
    first_MEM = Read('00',MEM)
    assert Get_Value(0,first_MEM) == '+1111'
    monkeypatch.setattr('builtins.input', lambda _: '1111')
    second_MEM = Read('00',MEM)
    assert Get_Value(0,second_MEM) == '+0001'

def test_write(capfd):
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    first_MEM = Write('00',MEM)
    output, err = capfd.readouterr()
    assert output == '+0001\n'
    assert first_MEM == MEM


