import os

def convert(file_in, file_out, conditon = ""):
	print("Converting pcap file " + file_in + "...")
	os.system('tshark -r ../../../data/%s -Y "%s" -T fields -e ip.src -e ip.dst -e frame.number -e _ws.col.Info -E header=y > ../../../data/%s' %(file_in, conditon, file_out))
	print("..\n Successfully converted PCAP into %s" %(file_out))

