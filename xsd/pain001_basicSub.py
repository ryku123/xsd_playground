#!/usr/bin/env python

#
# Generated Mon Mar 21 22:01:05 2016 by generateDS.py version 2.20a.
#
# Command line options:
#   ('-o', 'pain001_new.py')
#   ('-s', 'pain001_basicSub.py')
#   ('--super', 'pain001_new')
#   ('--member-specs', 'dict')
#   ('--export', 'write etree literal')
#
# Command line arguments:
#   pain.001.001.03.ch.02.xsd
#
# Command line:
#   /usr/local/bin/generateDS.py -o "pain001_basic.py" -s "pain001_basicSub.py" --super="pain001_basic" --member-specs="dict" --export="write etree literal" pain.001.001.03.ch.02.xsd
#
# Current working directory (os.getcwd()):
#   xsd
#

import sys
from lxml import etree as etree_

import pain001_new as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class AccountIdentification4Choice_CHSub(supermod.AccountIdentification4Choice_CH):
    def __init__(self, IBAN=None, Othr=None):
        super(AccountIdentification4Choice_CHSub, self).__init__(IBAN, Othr, )
supermod.AccountIdentification4Choice_CH.subclass = AccountIdentification4Choice_CHSub
# end class AccountIdentification4Choice_CHSub


class ActiveOrHistoricCurrencyAndAmountSub(supermod.ActiveOrHistoricCurrencyAndAmount):
    def __init__(self, Ccy=None, valueOf_=None):
        super(ActiveOrHistoricCurrencyAndAmountSub, self).__init__(Ccy, valueOf_, )
supermod.ActiveOrHistoricCurrencyAndAmount.subclass = ActiveOrHistoricCurrencyAndAmountSub
# end class ActiveOrHistoricCurrencyAndAmountSub


class AmountType3ChoiceSub(supermod.AmountType3Choice):
    def __init__(self, InstdAmt=None, EqvtAmt=None):
        super(AmountType3ChoiceSub, self).__init__(InstdAmt, EqvtAmt, )
supermod.AmountType3Choice.subclass = AmountType3ChoiceSub
# end class AmountType3ChoiceSub


class BranchAndFinancialInstitutionIdentification4Sub(supermod.BranchAndFinancialInstitutionIdentification4):
    def __init__(self, FinInstnId=None, BrnchId=None):
        super(BranchAndFinancialInstitutionIdentification4Sub, self).__init__(FinInstnId, BrnchId, )
supermod.BranchAndFinancialInstitutionIdentification4.subclass = BranchAndFinancialInstitutionIdentification4Sub
# end class BranchAndFinancialInstitutionIdentification4Sub


class BranchAndFinancialInstitutionIdentification4_CH_BicOrClrIdSub(supermod.BranchAndFinancialInstitutionIdentification4_CH_BicOrClrId):
    def __init__(self, FinInstnId=None):
        super(BranchAndFinancialInstitutionIdentification4_CH_BicOrClrIdSub, self).__init__(FinInstnId, )
supermod.BranchAndFinancialInstitutionIdentification4_CH_BicOrClrId.subclass = BranchAndFinancialInstitutionIdentification4_CH_BicOrClrIdSub
# end class BranchAndFinancialInstitutionIdentification4_CH_BicOrClrIdSub


class BranchAndFinancialInstitutionIdentification4_CHSub(supermod.BranchAndFinancialInstitutionIdentification4_CH):
    def __init__(self, FinInstnId=None):
        super(BranchAndFinancialInstitutionIdentification4_CHSub, self).__init__(FinInstnId, )
supermod.BranchAndFinancialInstitutionIdentification4_CH.subclass = BranchAndFinancialInstitutionIdentification4_CHSub
# end class BranchAndFinancialInstitutionIdentification4_CHSub


class BranchData2Sub(supermod.BranchData2):
    def __init__(self, Id=None, Nm=None, PstlAdr=None):
        super(BranchData2Sub, self).__init__(Id, Nm, PstlAdr, )
supermod.BranchData2.subclass = BranchData2Sub
# end class BranchData2Sub


class CashAccount16_CH_IdAndCurrencySub(supermod.CashAccount16_CH_IdAndCurrency):
    def __init__(self, Id=None, Ccy=None):
        super(CashAccount16_CH_IdAndCurrencySub, self).__init__(Id, Ccy, )
supermod.CashAccount16_CH_IdAndCurrency.subclass = CashAccount16_CH_IdAndCurrencySub
# end class CashAccount16_CH_IdAndCurrencySub


class CashAccount16_CH_IdTpCcySub(supermod.CashAccount16_CH_IdTpCcy):
    def __init__(self, Id=None, Tp=None, Ccy=None):
        super(CashAccount16_CH_IdTpCcySub, self).__init__(Id, Tp, Ccy, )
supermod.CashAccount16_CH_IdTpCcy.subclass = CashAccount16_CH_IdTpCcySub
# end class CashAccount16_CH_IdTpCcySub


class CashAccount16_CH_IdSub(supermod.CashAccount16_CH_Id):
    def __init__(self, Id=None):
        super(CashAccount16_CH_IdSub, self).__init__(Id, )
supermod.CashAccount16_CH_Id.subclass = CashAccount16_CH_IdSub
# end class CashAccount16_CH_IdSub


class CashAccountType2Sub(supermod.CashAccountType2):
    def __init__(self, Cd=None, Prtry=None):
        super(CashAccountType2Sub, self).__init__(Cd, Prtry, )
supermod.CashAccountType2.subclass = CashAccountType2Sub
# end class CashAccountType2Sub


class CategoryPurpose1_CH_CodeSub(supermod.CategoryPurpose1_CH_Code):
    def __init__(self, Cd=None):
        super(CategoryPurpose1_CH_CodeSub, self).__init__(Cd, )
supermod.CategoryPurpose1_CH_Code.subclass = CategoryPurpose1_CH_CodeSub
# end class CategoryPurpose1_CH_CodeSub


class Cheque6_CHSub(supermod.Cheque6_CH):
    def __init__(self, ChqTp=None, DlvryMtd=None):
        super(Cheque6_CHSub, self).__init__(ChqTp, DlvryMtd, )
supermod.Cheque6_CH.subclass = Cheque6_CHSub
# end class Cheque6_CHSub


class ChequeDeliveryMethod1ChoiceSub(supermod.ChequeDeliveryMethod1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ChequeDeliveryMethod1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ChequeDeliveryMethod1Choice.subclass = ChequeDeliveryMethod1ChoiceSub
# end class ChequeDeliveryMethod1ChoiceSub


class ClearingSystemIdentification2ChoiceSub(supermod.ClearingSystemIdentification2Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ClearingSystemIdentification2ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ClearingSystemIdentification2Choice.subclass = ClearingSystemIdentification2ChoiceSub
# end class ClearingSystemIdentification2ChoiceSub


class ClearingSystemMemberIdentification2Sub(supermod.ClearingSystemMemberIdentification2):
    def __init__(self, ClrSysId=None, MmbId=None):
        super(ClearingSystemMemberIdentification2Sub, self).__init__(ClrSysId, MmbId, )
supermod.ClearingSystemMemberIdentification2.subclass = ClearingSystemMemberIdentification2Sub
# end class ClearingSystemMemberIdentification2Sub


class ContactDetails2Sub(supermod.ContactDetails2):
    def __init__(self, NmPrfx=None, Nm=None, PhneNb=None, MobNb=None, FaxNb=None, EmailAdr=None, Othr=None):
        super(ContactDetails2Sub, self).__init__(NmPrfx, Nm, PhneNb, MobNb, FaxNb, EmailAdr, Othr, )
supermod.ContactDetails2.subclass = ContactDetails2Sub
# end class ContactDetails2Sub


class ContactDetails2_CHSub(supermod.ContactDetails2_CH):
    def __init__(self, Nm=None, Othr=None):
        super(ContactDetails2_CHSub, self).__init__(Nm, Othr, )
supermod.ContactDetails2_CH.subclass = ContactDetails2_CHSub
# end class ContactDetails2_CHSub


class CreditTransferTransactionInformation10_CHSub(supermod.CreditTransferTransactionInformation10_CH):
    def __init__(self, PmtId=None, PmtTpInf=None, Amt=None, XchgRateInf=None, ChrgBr=None, ChqInstr=None, UltmtDbtr=None, IntrmyAgt1=None, CdtrAgt=None, Cdtr=None, CdtrAcct=None, UltmtCdtr=None, InstrForCdtrAgt=None, InstrForDbtrAgt=None, Purp=None, RgltryRptg=None, RmtInf=None):
        super(CreditTransferTransactionInformation10_CHSub, self).__init__(PmtId, PmtTpInf, Amt, XchgRateInf, ChrgBr, ChqInstr, UltmtDbtr, IntrmyAgt1, CdtrAgt, Cdtr, CdtrAcct, UltmtCdtr, InstrForCdtrAgt, InstrForDbtrAgt, Purp, RgltryRptg, RmtInf, )
supermod.CreditTransferTransactionInformation10_CH.subclass = CreditTransferTransactionInformation10_CHSub
# end class CreditTransferTransactionInformation10_CHSub


class CreditorReferenceInformation2Sub(supermod.CreditorReferenceInformation2):
    def __init__(self, Tp=None, Ref=None):
        super(CreditorReferenceInformation2Sub, self).__init__(Tp, Ref, )
supermod.CreditorReferenceInformation2.subclass = CreditorReferenceInformation2Sub
# end class CreditorReferenceInformation2Sub


class CreditorReferenceType1ChoiceSub(supermod.CreditorReferenceType1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(CreditorReferenceType1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.CreditorReferenceType1Choice.subclass = CreditorReferenceType1ChoiceSub
# end class CreditorReferenceType1ChoiceSub


class CreditorReferenceType2Sub(supermod.CreditorReferenceType2):
    def __init__(self, CdOrPrtry=None, Issr=None):
        super(CreditorReferenceType2Sub, self).__init__(CdOrPrtry, Issr, )
supermod.CreditorReferenceType2.subclass = CreditorReferenceType2Sub
# end class CreditorReferenceType2Sub


class CustomerCreditTransferInitiationV03_CHSub(supermod.CustomerCreditTransferInitiationV03_CH):
    def __init__(self, GrpHdr=None, PmtInf=None):
        super(CustomerCreditTransferInitiationV03_CHSub, self).__init__(GrpHdr, PmtInf, )
supermod.CustomerCreditTransferInitiationV03_CH.subclass = CustomerCreditTransferInitiationV03_CHSub
# end class CustomerCreditTransferInitiationV03_CHSub


class DateAndPlaceOfBirthSub(supermod.DateAndPlaceOfBirth):
    def __init__(self, BirthDt=None, PrvcOfBirth=None, CityOfBirth=None, CtryOfBirth=None):
        super(DateAndPlaceOfBirthSub, self).__init__(BirthDt, PrvcOfBirth, CityOfBirth, CtryOfBirth, )
supermod.DateAndPlaceOfBirth.subclass = DateAndPlaceOfBirthSub
# end class DateAndPlaceOfBirthSub


class DocumentSub(supermod.Document):
    def __init__(self, CstmrCdtTrfInitn=None):
        super(DocumentSub, self).__init__(CstmrCdtTrfInitn, )
supermod.Document.subclass = DocumentSub
# end class DocumentSub


class DocumentAdjustment1Sub(supermod.DocumentAdjustment1):
    def __init__(self, Amt=None, CdtDbtInd=None, Rsn=None, AddtlInf=None):
        super(DocumentAdjustment1Sub, self).__init__(Amt, CdtDbtInd, Rsn, AddtlInf, )
supermod.DocumentAdjustment1.subclass = DocumentAdjustment1Sub
# end class DocumentAdjustment1Sub


class EquivalentAmount2Sub(supermod.EquivalentAmount2):
    def __init__(self, Amt=None, CcyOfTrf=None):
        super(EquivalentAmount2Sub, self).__init__(Amt, CcyOfTrf, )
supermod.EquivalentAmount2.subclass = EquivalentAmount2Sub
# end class EquivalentAmount2Sub


class ExchangeRateInformation1Sub(supermod.ExchangeRateInformation1):
    def __init__(self, XchgRate=None, RateTp=None, CtrctId=None):
        super(ExchangeRateInformation1Sub, self).__init__(XchgRate, RateTp, CtrctId, )
supermod.ExchangeRateInformation1.subclass = ExchangeRateInformation1Sub
# end class ExchangeRateInformation1Sub


class FinancialIdentificationSchemeName1ChoiceSub(supermod.FinancialIdentificationSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(FinancialIdentificationSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.FinancialIdentificationSchemeName1Choice.subclass = FinancialIdentificationSchemeName1ChoiceSub
# end class FinancialIdentificationSchemeName1ChoiceSub


class FinancialInstitutionIdentification7Sub(supermod.FinancialInstitutionIdentification7):
    def __init__(self, BIC=None, ClrSysMmbId=None, Nm=None, PstlAdr=None, Othr=None):
        super(FinancialInstitutionIdentification7Sub, self).__init__(BIC, ClrSysMmbId, Nm, PstlAdr, Othr, )
supermod.FinancialInstitutionIdentification7.subclass = FinancialInstitutionIdentification7Sub
# end class FinancialInstitutionIdentification7Sub


class FinancialInstitutionIdentification7_CH_BicOrClrIdSub(supermod.FinancialInstitutionIdentification7_CH_BicOrClrId):
    def __init__(self, BIC=None, ClrSysMmbId=None):
        super(FinancialInstitutionIdentification7_CH_BicOrClrIdSub, self).__init__(BIC, ClrSysMmbId, )
supermod.FinancialInstitutionIdentification7_CH_BicOrClrId.subclass = FinancialInstitutionIdentification7_CH_BicOrClrIdSub
# end class FinancialInstitutionIdentification7_CH_BicOrClrIdSub


class FinancialInstitutionIdentification7_CHSub(supermod.FinancialInstitutionIdentification7_CH):
    def __init__(self, BIC=None, ClrSysMmbId=None, Nm=None, PstlAdr=None, Othr=None):
        super(FinancialInstitutionIdentification7_CHSub, self).__init__(BIC, ClrSysMmbId, Nm, PstlAdr, Othr, )
supermod.FinancialInstitutionIdentification7_CH.subclass = FinancialInstitutionIdentification7_CHSub
# end class FinancialInstitutionIdentification7_CHSub


class GenericAccountIdentification1_CHSub(supermod.GenericAccountIdentification1_CH):
    def __init__(self, Id=None):
        super(GenericAccountIdentification1_CHSub, self).__init__(Id, )
supermod.GenericAccountIdentification1_CH.subclass = GenericAccountIdentification1_CHSub
# end class GenericAccountIdentification1_CHSub


class GenericFinancialIdentification1Sub(supermod.GenericFinancialIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericFinancialIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericFinancialIdentification1.subclass = GenericFinancialIdentification1Sub
# end class GenericFinancialIdentification1Sub


class GenericFinancialIdentification1_CHSub(supermod.GenericFinancialIdentification1_CH):
    def __init__(self, Id=None):
        super(GenericFinancialIdentification1_CHSub, self).__init__(Id, )
supermod.GenericFinancialIdentification1_CH.subclass = GenericFinancialIdentification1_CHSub
# end class GenericFinancialIdentification1_CHSub


class GenericOrganisationIdentification1Sub(supermod.GenericOrganisationIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericOrganisationIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericOrganisationIdentification1.subclass = GenericOrganisationIdentification1Sub
# end class GenericOrganisationIdentification1Sub


class GenericPersonIdentification1Sub(supermod.GenericPersonIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericPersonIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericPersonIdentification1.subclass = GenericPersonIdentification1Sub
# end class GenericPersonIdentification1Sub


class GroupHeader32_CHSub(supermod.GroupHeader32_CH):
    def __init__(self, MsgId=None, CreDtTm=None, NbOfTxs=None, CtrlSum=None, InitgPty=None, FwdgAgt=None):
        super(GroupHeader32_CHSub, self).__init__(MsgId, CreDtTm, NbOfTxs, CtrlSum, InitgPty, FwdgAgt, )
supermod.GroupHeader32_CH.subclass = GroupHeader32_CHSub
# end class GroupHeader32_CHSub


class InstructionForCreditorAgent1Sub(supermod.InstructionForCreditorAgent1):
    def __init__(self, Cd=None, InstrInf=None):
        super(InstructionForCreditorAgent1Sub, self).__init__(Cd, InstrInf, )
supermod.InstructionForCreditorAgent1.subclass = InstructionForCreditorAgent1Sub
# end class InstructionForCreditorAgent1Sub


class LocalInstrument2ChoiceSub(supermod.LocalInstrument2Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(LocalInstrument2ChoiceSub, self).__init__(Cd, Prtry, )
supermod.LocalInstrument2Choice.subclass = LocalInstrument2ChoiceSub
# end class LocalInstrument2ChoiceSub


class OrganisationIdentification4Sub(supermod.OrganisationIdentification4):
    def __init__(self, BICOrBEI=None, Othr=None):
        super(OrganisationIdentification4Sub, self).__init__(BICOrBEI, Othr, )
supermod.OrganisationIdentification4.subclass = OrganisationIdentification4Sub
# end class OrganisationIdentification4Sub


class OrganisationIdentification4_CHSub(supermod.OrganisationIdentification4_CH):
    def __init__(self, BICOrBEI=None, Othr=None):
        super(OrganisationIdentification4_CHSub, self).__init__(BICOrBEI, Othr, )
supermod.OrganisationIdentification4_CH.subclass = OrganisationIdentification4_CHSub
# end class OrganisationIdentification4_CHSub


class OrganisationIdentificationSchemeName1ChoiceSub(supermod.OrganisationIdentificationSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(OrganisationIdentificationSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.OrganisationIdentificationSchemeName1Choice.subclass = OrganisationIdentificationSchemeName1ChoiceSub
# end class OrganisationIdentificationSchemeName1ChoiceSub


class Party6ChoiceSub(supermod.Party6Choice):
    def __init__(self, OrgId=None, PrvtId=None):
        super(Party6ChoiceSub, self).__init__(OrgId, PrvtId, )
supermod.Party6Choice.subclass = Party6ChoiceSub
# end class Party6ChoiceSub


class Party6Choice_CHSub(supermod.Party6Choice_CH):
    def __init__(self, OrgId=None, PrvtId=None):
        super(Party6Choice_CHSub, self).__init__(OrgId, PrvtId, )
supermod.Party6Choice_CH.subclass = Party6Choice_CHSub
# end class Party6Choice_CHSub


class PartyIdentification32Sub(supermod.PartyIdentification32):
    def __init__(self, Nm=None, PstlAdr=None, Id=None, CtryOfRes=None, CtctDtls=None):
        super(PartyIdentification32Sub, self).__init__(Nm, PstlAdr, Id, CtryOfRes, CtctDtls, )
supermod.PartyIdentification32.subclass = PartyIdentification32Sub
# end class PartyIdentification32Sub


class PartyIdentification32_CH_NameAndIdSub(supermod.PartyIdentification32_CH_NameAndId):
    def __init__(self, Nm=None, Id=None, CtctDtls=None):
        super(PartyIdentification32_CH_NameAndIdSub, self).__init__(Nm, Id, CtctDtls, )
supermod.PartyIdentification32_CH_NameAndId.subclass = PartyIdentification32_CH_NameAndIdSub
# end class PartyIdentification32_CH_NameAndIdSub


class PartyIdentification32_CHSub(supermod.PartyIdentification32_CH):
    def __init__(self, Nm=None, PstlAdr=None, Id=None):
        super(PartyIdentification32_CHSub, self).__init__(Nm, PstlAdr, Id, )
supermod.PartyIdentification32_CH.subclass = PartyIdentification32_CHSub
# end class PartyIdentification32_CHSub


class PartyIdentification32_CH_NameSub(supermod.PartyIdentification32_CH_Name):
    def __init__(self, Nm=None, PstlAdr=None, Id=None):
        super(PartyIdentification32_CH_NameSub, self).__init__(Nm, PstlAdr, Id, )
supermod.PartyIdentification32_CH_Name.subclass = PartyIdentification32_CH_NameSub
# end class PartyIdentification32_CH_NameSub


class PaymentIdentification1Sub(supermod.PaymentIdentification1):
    def __init__(self, InstrId=None, EndToEndId=None):
        super(PaymentIdentification1Sub, self).__init__(InstrId, EndToEndId, )
supermod.PaymentIdentification1.subclass = PaymentIdentification1Sub
# end class PaymentIdentification1Sub


class PaymentInstructionInformation3_CHSub(supermod.PaymentInstructionInformation3_CH):
    def __init__(self, PmtInfId=None, PmtMtd=None, BtchBookg=None, NbOfTxs=None, CtrlSum=None, PmtTpInf=None, ReqdExctnDt=None, Dbtr=None, DbtrAcct=None, DbtrAgt=None, UltmtDbtr=None, ChrgBr=None, ChrgsAcct=None, CdtTrfTxInf=None):
        super(PaymentInstructionInformation3_CHSub, self).__init__(PmtInfId, PmtMtd, BtchBookg, NbOfTxs, CtrlSum, PmtTpInf, ReqdExctnDt, Dbtr, DbtrAcct, DbtrAgt, UltmtDbtr, ChrgBr, ChrgsAcct, CdtTrfTxInf, )
supermod.PaymentInstructionInformation3_CH.subclass = PaymentInstructionInformation3_CHSub
# end class PaymentInstructionInformation3_CHSub


class PaymentTypeInformation19_CHSub(supermod.PaymentTypeInformation19_CH):
    def __init__(self, InstrPrty=None, SvcLvl=None, LclInstrm=None, CtgyPurp=None):
        super(PaymentTypeInformation19_CHSub, self).__init__(InstrPrty, SvcLvl, LclInstrm, CtgyPurp, )
supermod.PaymentTypeInformation19_CH.subclass = PaymentTypeInformation19_CHSub
# end class PaymentTypeInformation19_CHSub


class PersonIdentification5Sub(supermod.PersonIdentification5):
    def __init__(self, DtAndPlcOfBirth=None, Othr=None):
        super(PersonIdentification5Sub, self).__init__(DtAndPlcOfBirth, Othr, )
supermod.PersonIdentification5.subclass = PersonIdentification5Sub
# end class PersonIdentification5Sub


class PersonIdentification5_CHSub(supermod.PersonIdentification5_CH):
    def __init__(self, DtAndPlcOfBirth=None, Othr=None):
        super(PersonIdentification5_CHSub, self).__init__(DtAndPlcOfBirth, Othr, )
supermod.PersonIdentification5_CH.subclass = PersonIdentification5_CHSub
# end class PersonIdentification5_CHSub


class PersonIdentificationSchemeName1ChoiceSub(supermod.PersonIdentificationSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(PersonIdentificationSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.PersonIdentificationSchemeName1Choice.subclass = PersonIdentificationSchemeName1ChoiceSub
# end class PersonIdentificationSchemeName1ChoiceSub


class PostalAddress6Sub(supermod.PostalAddress6):
    def __init__(self, AdrTp=None, Dept=None, SubDept=None, StrtNm=None, BldgNb=None, PstCd=None, TwnNm=None, CtrySubDvsn=None, Ctry=None, AdrLine=None):
        super(PostalAddress6Sub, self).__init__(AdrTp, Dept, SubDept, StrtNm, BldgNb, PstCd, TwnNm, CtrySubDvsn, Ctry, AdrLine, )
supermod.PostalAddress6.subclass = PostalAddress6Sub
# end class PostalAddress6Sub


class PostalAddress6_CHSub(supermod.PostalAddress6_CH):
    def __init__(self, AdrTp=None, Dept=None, SubDept=None, StrtNm=None, BldgNb=None, PstCd=None, TwnNm=None, CtrySubDvsn=None, Ctry=None, AdrLine=None):
        super(PostalAddress6_CHSub, self).__init__(AdrTp, Dept, SubDept, StrtNm, BldgNb, PstCd, TwnNm, CtrySubDvsn, Ctry, AdrLine, )
supermod.PostalAddress6_CH.subclass = PostalAddress6_CHSub
# end class PostalAddress6_CHSub


class Purpose2_CH_CodeSub(supermod.Purpose2_CH_Code):
    def __init__(self, Cd=None):
        super(Purpose2_CH_CodeSub, self).__init__(Cd, )
supermod.Purpose2_CH_Code.subclass = Purpose2_CH_CodeSub
# end class Purpose2_CH_CodeSub


class ReferredDocumentInformation3Sub(supermod.ReferredDocumentInformation3):
    def __init__(self, Tp=None, Nb=None, RltdDt=None):
        super(ReferredDocumentInformation3Sub, self).__init__(Tp, Nb, RltdDt, )
supermod.ReferredDocumentInformation3.subclass = ReferredDocumentInformation3Sub
# end class ReferredDocumentInformation3Sub


class ReferredDocumentType1ChoiceSub(supermod.ReferredDocumentType1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ReferredDocumentType1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ReferredDocumentType1Choice.subclass = ReferredDocumentType1ChoiceSub
# end class ReferredDocumentType1ChoiceSub


class ReferredDocumentType2Sub(supermod.ReferredDocumentType2):
    def __init__(self, CdOrPrtry=None, Issr=None):
        super(ReferredDocumentType2Sub, self).__init__(CdOrPrtry, Issr, )
supermod.ReferredDocumentType2.subclass = ReferredDocumentType2Sub
# end class ReferredDocumentType2Sub


class RegulatoryAuthority2Sub(supermod.RegulatoryAuthority2):
    def __init__(self, Nm=None, Ctry=None):
        super(RegulatoryAuthority2Sub, self).__init__(Nm, Ctry, )
supermod.RegulatoryAuthority2.subclass = RegulatoryAuthority2Sub
# end class RegulatoryAuthority2Sub


class RegulatoryReporting3Sub(supermod.RegulatoryReporting3):
    def __init__(self, DbtCdtRptgInd=None, Authrty=None, Dtls=None):
        super(RegulatoryReporting3Sub, self).__init__(DbtCdtRptgInd, Authrty, Dtls, )
supermod.RegulatoryReporting3.subclass = RegulatoryReporting3Sub
# end class RegulatoryReporting3Sub


class RemittanceAmount1Sub(supermod.RemittanceAmount1):
    def __init__(self, DuePyblAmt=None, DscntApldAmt=None, CdtNoteAmt=None, TaxAmt=None, AdjstmntAmtAndRsn=None, RmtdAmt=None):
        super(RemittanceAmount1Sub, self).__init__(DuePyblAmt, DscntApldAmt, CdtNoteAmt, TaxAmt, AdjstmntAmtAndRsn, RmtdAmt, )
supermod.RemittanceAmount1.subclass = RemittanceAmount1Sub
# end class RemittanceAmount1Sub


class RemittanceInformation5_CHSub(supermod.RemittanceInformation5_CH):
    def __init__(self, Ustrd=None, Strd=None):
        super(RemittanceInformation5_CHSub, self).__init__(Ustrd, Strd, )
supermod.RemittanceInformation5_CH.subclass = RemittanceInformation5_CHSub
# end class RemittanceInformation5_CHSub


class ServiceLevel8ChoiceSub(supermod.ServiceLevel8Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ServiceLevel8ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ServiceLevel8Choice.subclass = ServiceLevel8ChoiceSub
# end class ServiceLevel8ChoiceSub


class StructuredRegulatoryReporting3Sub(supermod.StructuredRegulatoryReporting3):
    def __init__(self, Tp=None, Dt=None, Ctry=None, Cd=None, Amt=None, Inf=None):
        super(StructuredRegulatoryReporting3Sub, self).__init__(Tp, Dt, Ctry, Cd, Amt, Inf, )
supermod.StructuredRegulatoryReporting3.subclass = StructuredRegulatoryReporting3Sub
# end class StructuredRegulatoryReporting3Sub


class StructuredRemittanceInformation7Sub(supermod.StructuredRemittanceInformation7):
    def __init__(self, RfrdDocInf=None, RfrdDocAmt=None, CdtrRefInf=None, Invcr=None, Invcee=None, AddtlRmtInf=None):
        super(StructuredRemittanceInformation7Sub, self).__init__(RfrdDocInf, RfrdDocAmt, CdtrRefInf, Invcr, Invcee, AddtlRmtInf, )
supermod.StructuredRemittanceInformation7.subclass = StructuredRemittanceInformation7Sub
# end class StructuredRemittanceInformation7Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from pain001_new import *\n\n')
        sys.stdout.write('import pain001_new as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
