from EncodedTicket import EncodedTicket
from Utitilies import Utilities

from math import pow

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

        

        



        


if __name__ == "__main__":
    testTicket = EncodedTicket('06DNQMCQF6S00TTKAONESWRDYJFSMEJMYVOXBTRNSVFNHTUTKXNFIDSYKVPVIRWBDHASQXBRRKIHPYPPQPYUYGFJKAYLEMKFTJIENGRKQDMGMQNHTZGDFYJBGZSMAKRZRXUIYJYNEFDIDOOTPQXVGUVNXPLAYATOXTPFJAQZPAYKQBCHBVKNBRPXKDIWBQJVCNYFNVAEZTHOHQLUCUPONPUDELCNTJQJWOUNWGTQA')
    decoder = Decoder(testTicket.originalStr)
    decoder.decode()



