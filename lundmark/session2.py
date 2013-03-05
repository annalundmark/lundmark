#

def getData(data): 
	import untangle
	doc=untangle.parse(data)
	doc.get_elements()
	outages = doc.NYCOutages.outage
	return outages

def Reasons(outages, equipmenttype, reason): 
	equipmenttype_total=0
	reason_total=0
	for outage in outages: 
		if outage.equipmenttype.cdata==equipmenttype: 
			equipmenttype_total=equipmenttype_total + 1
			if outage.reason.cdata==reason: 
				reason_total=reason_total + 1
	return equipmenttype_total, reason_total

def Fraction(equipments_nr, reasons_nr): 
	fraction=float(reasons_nr)/float(equipments_nr)
	return fraction
