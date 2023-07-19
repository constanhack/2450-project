from business_logic import Check_for_Operation



def main(mem,window):

    while mem.get_pc() < mem.mem_size:
        pc_location = mem.get_pc()
        if mem.get_mem_value(pc_location) == 0:
            mem.increment_pc()
            continue

        if mem.get_mem_value(pc_location) >= 0:
            branched = Check_for_Operation(str(mem.get_mem_value(pc_location)),mem,window)
            
            if branched:
                continue
                
        if mem.get_pc() == 'HALT':
            return
        mem.increment_pc()

    return