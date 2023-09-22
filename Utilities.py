from typing import Optional
import base26

class Utilities:
    def base26_decode(input_str) -> int:
        return int.from_bytes(base26.decode(input_str), "big")
        
        # out = 0
        # input_bytes = input_str.encode('utf-8')

        # for val in input_bytes[::-1]:
        #     out *= 26
        #     out += val - ord('A')
        # return out
    
    
    def strip_padding(tkt: bytes) -> Optional[bytes]:
        if not tkt:
            return None
        
        if tkt[0] == 1:
            # PKCS#1 v1
            tkt = tkt[1:]
            iter_idx = 0
            while iter_idx < len(tkt):
                if tkt[iter_idx] == 0:
                    return tkt[iter_idx + 1:]
                elif tkt[iter_idx] == 255:
                    iter_idx += 1
                else:
                    return None
        
        elif tkt[0] == 2:
            # PKCS#1 v2
            tkt = tkt[1:]
            iter_idx = 0
            while iter_idx < len(tkt):
                if tkt[iter_idx] == 0:
                    return tkt[iter_idx + 1:]
                iter_idx += 1
        
        return None