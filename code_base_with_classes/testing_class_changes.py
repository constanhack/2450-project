from data_loader import DataLoader
from data_model import DataModel


data = DataLoader()
mem = DataModel(data.get_data())

print(mem._private_MEM.items())

print(mem.get_mem_value(100))

print(mem.mem_size)