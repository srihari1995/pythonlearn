def reverse( text ):
	new=""
	n=-1
	while n >= -1*len(text):
		new=new+text[n]
		n-=1
	return new	
if __name__=="__main__":
	print reverse("srihari")