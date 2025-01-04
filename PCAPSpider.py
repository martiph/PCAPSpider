"""
Read a pcap file and create a visualisation.

PCAPSpider -p "path to PCAP file"
"""
import os.path

def verify_pcap_magic_number(magic_number):
    """
    Verifies if the magic number (32bits) actually matches the specification (https://datatracker.ietf.org/doc/id/draft-gharris-opsawg-pcap-00.html)
    0xA1B2C3D4, time stamps in packet records are in seconds and microseconds
    0xA1B23C4D, time stamps in packet records are in seconds and nanoseconds
    """
    print(magic_number)
    # if magic_number != "" and magic_number != "":
        # raise Exception("File type not supported.")



def parse_pcap_file(path):
    """
    Parse the PCAP file to which the path was provided.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        with open(path, "rt") as pcap:
            magic_number = pcap.read(2)
            verify_pcap_magic_number(magic_number)
            packets = pcap.readlines()
            for packet in packets:
                print(packet)

if __name__ == "__main__":
    print("to be implemented")
