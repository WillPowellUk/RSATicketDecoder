from Utilities import Utilities

import numpy as np
from math import pow
import json


class Decoder:
    def __init__(self, ticket_str:str) -> None:
        self.ticket_str = ticket_str
    

    # main decode function
    def decode(self):
        # check ticket is the right size and format
        if len(self.ticket_str) < 16:
            raise Exception("Ticket too short")
    
        if self.ticket_str[0:2] != "06":
            raise Exception(f"Ticket isn't a RSP6 ticket: magic was {self.ticket_str[0:2]}")

        # Extract issuer id (i.e. TT for Trainline)
        issuer_id = self.ticket_str[13:15]
        # Decode from base 26 encoding the rest of ticket
        self.ticket_int = Utilities.base26_decode(self.ticket_str[15:])

        # Load the JSON data from the file
        with open("PublicKeys.json", "r") as json_file:
            data = json.load(json_file)

        # Check if the issuer ID exists 
        if issuer_id not in data:
            raise Exception("Issuer ID not found")
        
        # Cycle through keys for issuer and try to decode
        keys = data[issuer_id]
        for key in keys:
            # the most important line: S^e mod N
            message = np.power(self.ticket_int, int(key["public_exponent_hex"],16)) % int(key["modulus_hex"], 16)
            message_bytes = message.to_bytes(256, byteorder='big')
            unpadded = Utilities.strip_padding(message_bytes)
            if unpadded is not None: 
                print("Unpack Successful!")
                print(unpadded)
            
        raise Exception(f"All signature unwrap attempts failed (tried {len(keys)} keys for issuer {issuer_id})")


if __name__ == "__main__":
    # cardiff ticket example
    encoded_ticket_str = '06DNQMCQF6S00TTKAONESWRDYJFSMEJMYVOXBTRNSVFNHTUTKXNFIDSYKVPVIRWBDHASQXBRRKIHPYPPQPYUYGFJKAYLEMKFTJIENGRKQDMGMQNHTZGDFYJBGZSMAKRZRXUIYJYNEFDIDOOTPQXVGUVNXPLAYATOXTPFJAQZPAYKQBCHBVKNBRPXKDIWBQJVCNYFNVAEZTHOHQLUCUPONPUDELCNTJQJWOUNWGTQA'
    decoder = Decoder(encoded_ticket_str)
    decoder.decode()



