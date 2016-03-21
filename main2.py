from xsd import pain001_newSub as pain001
import sys
from datetime import datetime


#create Group Header
grphdr = pain001.GroupHeader32_CHSub()
grphdr.set_MsgId("SomeMessageIDnnnnnnmklkkkklkjkljlkjkljlkjkljkljlkjlkjlkkkkkkkkkkkkkkkkk")   # no validation!
grphdr.set_CreDtTm(datetime.strptime("2010-02-15T07:30:00", '%Y-%m-%dT%H:%M:%S'))
grphdr.set_NbOfTxs("11")
grphdr.set_CtrlSum(3949.75)


# create PartyChoice (tag: Id)
_id = pain001.Party6Choice_CHSub()
_id.set_PrvtId(None)

# create OrganisationIdentification (tag BiCOrBEI)
_orgId = pain001.OrganisationIdentification4_CHSub()
_orgId.set_BICOrBEI("4_*(!&(*$&!@)(*#&)!@(*#56AaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSD")    # no validation!
_id.set_OrgId(_orgId)


# create PartyIdentification
initgPty = pain001.PartyIdentification32_CH_NameAndIdSub()

# tag: Nm
# initgPty.set_Nm(None)
initgPty.set_Id(_id)
initgPty.set_CtctDtls(None)

# tag: InitgPty
grphdr.set_InitgPty(initgPty)

# tag: CstmrCdtTrfInitn
cst = pain001.CustomerCreditTransferInitiationV03_CHSub(GrpHdr=grphdr, PmtInf=None)

# tag: Document
doc = pain001.DocumentSub(cst)

doc.export(sys.stdout, 0)