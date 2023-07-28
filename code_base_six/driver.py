from business_logic import Check_for_Operation

def main(mem,window):
    # Warn the user if they are using a 4-digit code of 6-digit
    if mem.get_mem_value(0) < 10000 and mem.get_mem_value(0) > -10000:
        window.appendOutput(f'WARNING: Your file is not in 6-digit BasicML and may not run as expected. Please select the checkbox at the bottom left of the window to convert your file to 6 digit BasicML.')
    
    while mem.get_pc() < mem.mem_size:
        pc_location = mem.get_pc()
        
        if mem.get_mem_value(pc_location) == 0:
            mem.increment_pc()
            continue
        if mem.get_mem_value(pc_location) >= 0:
            branched = Check_for_Operation(mem._private_MEM[str(pc_location).zfill(3)][1:],mem,window)
            
            if branched:
                continue
                
        if mem.get_pc() == 'HALT':
            return
        mem.increment_pc()

    return
