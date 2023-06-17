class DataModel:
    def __init__(self, data, accumulator = '+0000', pc_location = 0):
        
        self._private_MEM = data
        self._private_ACC = accumulator
        self._private_PC = pc_location
        self.mem_size = len(data)

    def get_mem_value(self,memory_location):
        if memory_location >= 0 and memory_location < self.mem_size:
            try:
                return self._private_MEM[str(memory_location).zfill(2)] 
            except:
                return False
        return False


    def set_mem_value(self,value, memory_location):
        if memory_location >= 0 and memory_location < self.mem_size:
            if value < 0:
                self._private_MEM[str(memory_location).zfill(2)] = f"-{str(value)[1:].zfill(4)}"
                return True
            else:
                self._private_MEM[str(memory_location).zfill(2)] = f"+{str(value).zfill(4)}"
                return True
            
        return False
    
    def get_pc(self):
        return self._private_PC
    
    def set_pc(self,value):
        if type(value) == int and value >=0 and value < self.mem_size:
            self._private_PC = value
            return True
        return False
    
    def increment_pc(self):
        if self._private_PC < self.mem_size:
            self.set_pc(self._private_PC + 1)
            return True
        return False
    
    def get_acc(self):
        return int(self._private_ACC)

    def set_acc(self,value):
        if type(value) == int and value >= -9999 and value <= 9999:
            if value < 0:
                self._private_ACC = f"-{str(value)[1:].zfill(4)}"
            else:
                self._private_ACC = f"+{str(value).zfill(4)}"

            print(f"{self._private_ACC} {type(self._private_ACC)}")
            return True
        return False
             
        



