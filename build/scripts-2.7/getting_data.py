from lundmark.session2 import *

xml_file="http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
equipmenttype="ES"
reason="REPAIR"
outages = getData(xml_file)
equipments, reasons = Reasons(outages, equipmenttype, reason)
fraction = Fraction(equipments, reasons)
print fraction