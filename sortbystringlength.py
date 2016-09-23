"""
a = ['ccc', 'aaaa', 'd', 'bb'];
def strlensort(x):
	lenlist = [];
	for i in x:
		lenlist.append(len(i)); #getting the length of all lists
	order = [];
	j = len(lenlist);
	while j>0:
		pos = lenlist.index(min(lenlist));
		order.append(pos);
		lenlist[pos]=10000;
		j-=1;
	print(order)
	for j in order:
		print(x[j], end=' ');
strlensort(a);
"""

class Alpha(object):
	name = "Alpha";
	def __init__(self, a):
		self.status = a;
	def shout(self):
		print(self.status.upper());
	def myname(self):
		print(self.name);

class Beta(Alpha):
	name = "Beta";
	def __init__(self, b):
		self.merastatus = b+"mera man";
	def shout(self):
		print(self.merastatus+"This is mera status boi");


b = Beta("I am beta. What's up?");
b.myname();
b.shout();