import requests
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True, help="Path to url input file")
ap.add_argument("-l", "--list", required=True, help="Path to bruteforce list file")
ap.add_argument("-o", "--output", required=False, help= "Path for output file")

args=vars(ap.parse_args())

print("########### Simple Directory BruteForce ###########")
urls = open(args["urls"], 'r')
dic = open(args["list"], 'r')
if args["output"]:
	out = open(args["output"], 'w')
dictionary = dic.readlines()
lines = urls.readlines()
urls.close()
dic.close()
for i in lines:
	i = i.strip('\n')
	print("Host: "+i)
	for words in dictionary:
		words = words.strip('\n')
		r=requests.get(i+words)
		print(" Status: "+str(r.status_code)+" --  /"+words+" -- Length: "+str(len(r.content)))
		if args["output"]:
			out.write(r.url+"\n")
		


