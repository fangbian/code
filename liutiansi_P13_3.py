import dns.resolver
domain=raw_input('please input a domain:')
#A=dns.resolver.query(domain,'A')
#for i in A.response.answer:
#	for j in i.items:
#		print j.address
	
MX=dns.resolver.query(domain,'MX')
for i in MX:
	print 'MX preference=',i.preference, 'mail exchanger=', i.exchange