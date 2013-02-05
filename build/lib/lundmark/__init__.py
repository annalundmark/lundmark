#

def getting_data(): 
	import untangle

	doc=untangle.parse("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")

	doc.get_elements()

	outages = doc.NYCOutages.outage

	for i in range (0, len(outages)): 
		outage = outages[i]
		if outage.equipmenttype.cdata=="ES": 
			if outage.reason.cdata=="REPAIR": 
				print outage.get_elements()