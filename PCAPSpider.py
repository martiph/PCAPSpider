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
    msec_little_endian = 'd4c3b2a1' # timestamp with microseconds, little endian notation
    nsec_little_endian = '4d3cb2a1' # timestamp with nanoseconds, little endian notation
    msec_big_endian = 'a1b2c3d4' # timestamp with microseconds, big endian notation
    nsec_big_endian = 'a1b23c4d' # timestamp with nanoseconds, big endian notation
    result = {
        "magic_number": magic_number,
        "endianness": None,
        "timestamp_format": None
    }
    
    if magic_number == msec_little_endian:
        result["endianness"] = "little endian"
        result["timestamp_format"] = "microseconds"
    elif magic_number == nsec_little_endian:
        result["endianness"] = "little endian"
        result["timestamp_format"] = "nanoseconds"
    elif magic_number == msec_big_endian:
        result["endianness"] = "big endian"
        result["timestamp_format"] = "microseconds"
    elif magic_number == nsec_big_endian:
        result["endianness"] = "big endian"
        result["timestamp_format"] = "nanoseconds"
    else:
        raise Exception("File type not supported. Magic number doesn't indicate PCAP file.")
    return result

def parse_frame_cyclic_sequence(fcs):
    """
    Frame Cyclic Sequence present (4 bits):
        if the "f" [the last] bit is set, then the FCS bits provide the number of bytes of FCS that are appended to each packet.
        valid values are between 0 and 7, with ethernet typically having a length of 4 bytes.
    """



def parse_pcap_file(path):
    """
    Parse the PCAP file to which the path was provided.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        with open(path, "rb") as pcap:
            # read file header
            magic_number = pcap.read(4).hex()
            major_version = pcap.read(2)
            minor_version = pcap.read(2)
            reserved_bytes = pcap.read(12) # discard those, according to specs they are not used
            snap_len = pcap.read(4)
            frame_cyclic_sequence = pcap.read(1) # only 4 bits are needed

            magic_number_check = verify_pcap_magic_number(magic_number)

            packets = pcap.readlines()
            for packet in packets:
                print("")

if __name__ == "__main__":
    parse_pcap_file("./test_pcap.pcap")
