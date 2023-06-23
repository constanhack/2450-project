class DataModel:
    def __init__(self, data, accumulator = '+0000', pc_location = 0):
        
        self._private_MEM = data
        self._private_ACC = accumulator
        self._private_PC = pc_location
        self.mem_size = len(data)
        self.min_value = -9999
        self.max_value = 9999
        self._private_value_length = 4
        

    def get_mem_value(self,memory_location):
        if type(memory_location) != int:
            raise TypeError
        if memory_location >= 0 and memory_location < self.mem_size:
            try:
                return int(self._private_MEM[str(memory_location).zfill(2)])
            except ValueError:
                raise ValueError
        raise MemoryError


    def set_mem_value(self,value, memory_location):
        if memory_location >= 0 and memory_location < self.mem_size:
            if self.validate_value(value):
                if value < 0:
                    self._private_MEM[str(memory_location).zfill(2)] = f"-{str(value)[1:].zfill(self._private_value_length)}"
                    return True
                else:
                    self._private_MEM[str(memory_location).zfill(2)] = f"+{str(value).zfill(self._private_value_length)}"
                    return True
        return False
    
    def get_pc(self):
        return self._private_PC
    
    def set_pc(self,value):
        if type(value) == int and value >=-1 and value < self.mem_size:
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
        if self.validate_value(value):
            if value < 0:
                self._private_ACC = f"-{str(value)[1:].zfill(self._private_value_length)}"
            else:
                self._private_ACC = f"+{str(value).zfill(self._private_value_length)}"
            return True
        return False
    
    def validate_value(self,value):
        try:
            int_value = int(value)
        except:
            return False
        if int_value >= self.min_value and int_value <= self.max_value:
            return True
        return False
             
        



