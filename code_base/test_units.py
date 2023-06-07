from memory_and_file_ops import Allocate_Memory, Get_Value
from load_store_ops import Load, Store
from IO_ops import Read, Write

def test_allocate_memory():
    file = open('test_files/unit_tests.txt','r')
    assert Allocate_Memory(file)['00'] == '+0001'
    assert len(Allocate_Memory(file)) == 100
    assert Allocate_Memory(file)['99'] == '+0000'

def test_get_value():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    assert Get_Value(0,MEM) == '+0001'
    assert type(Get_Value(0,MEM)) == str
    assert Get_Value(10,MEM) == '+0000'


def test_load():
    file = open('test_files/unit_tests.txt','r')
    MEM = Allocate_Memory(file)
    ACC = '+0000'
    first_MEM, first_ACC = Load('01',MEM,ACC)
    assert first_ACC == '-0002'
    assert MEM == first_MEM
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


