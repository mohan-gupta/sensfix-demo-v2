from fastapi import APIRouter

from typing import Union
from enum import Enum
from pydantic import BaseModel

from dependencies import (
    db_v1, db_v2, collection_val, collection_cl1_name,
    collection_cl2_name, collection_ticket, collection_resp
    )

#loading the collections
cl1 = db_v2.get_collection(collection_cl1_name)
cl2 = db_v2.get_collection(collection_cl2_name)
ticket = db_v1.get_collection(collection_ticket)
response = db_v1.get_collection(collection_resp)
valid_complaint = db_v1.get_collection(collection_val)

router = APIRouter()

# Defining datatypes
class Complaint(Enum):
    COMP = "complete"
    INCOMP = "incomplete"  

class ComplaintL1(Enum):
    PLMBNG = "plumbing"
    HVAC = "hvac"
    FIRE_SAF = "fire safety"
    WST_MNG = "waste management"
    ELEVTR_MNG = "elevator maintainence"
    PRKNG_TRNSP = "parking and transportation"
    GYM_EQP = "gym and fitness equipment maintainence"

class Plumbing(Enum):
    EMRGNC = "emergencies"
    LKS = "leaks"
    BLCKGS = "blockages"
    INSTL = "installations"
    RPRS = "repairs"
    MNTNC = "maintainence"
    WTR_QLT = "water quality "
    
class HVAC(Enum):
    EMRGNC = "emergencies"
    RDTR_MLF = "radiator malfunction"
    HEAT_PMP = "heat pump problems"
    BLR_ISS = "boiler issues"
    VNTLN_FAN = "ventilation fan issues"
    AC_ELC = "ac electrical issues"
    AC_NOISE = "ac noise issues"
    
class FireSafety(Enum):
    EMRGNC = "emergencies"
    FR_ALM = "fire alarms"
    FR_EXTNG = "fire extinguishers"
    FR_DRL = "fire drills"
    FR_SML = "small fires"
    FR_MJR = "major fires"
    FR_INVG = "fire investigations"
    
class WasteMngmnt(Enum):
    RES_WST = "residential waste"
    CMRCL_WST = "commercial waste"
    HZRDS_WST = "hazardous waste"
    WST_DROP = "waste drop off centres"
    WST_SRT = "waste sorting"
    REUSE_INIT = "reuse initiatives"
    RCL_STD = "recycling standards"
    
class ElevatorMngmnt(Enum):
    EMRGNC = "emergencies"
    INSPC = "inspection"
    CLNG = "cleaning"
    MCH_RPR = "mechanical repairs"
    ELC_RPR = "electrical repairs"
    SYS_UP = "system upgrades"
    COSMC_UP = "cosmetic upgrades"
    
class ParkingTransp(Enum):
    PRKNG_MNTNC = "parking lot maintainence"
    PRKNG_ALLOC = "parking space allocation"
    PDSTRN_SAF = "pedestrian safety"
    PRKNG_SAF = "parking structures"
    BICYC_INIT = "bicycle initiatives"
    PUB_TRNSPRT = "public transportation coordination"
    ENVMNT_ASS = "environmental impact assesment"
    
class GymEqp(Enum):
    POOL_CLN = "pool cleaning"
    WTR_Q = "water quality testing"
    CARDIO_EQP = "cardio equipment maintainence"
    STRN_EQP = "strenght equipment maintainence"
    HYG_CLN = "hygiene and clealiness"
    FRST_AD = "first aid"
    MCH_ISS = "mechanical issues"
    
class Ticket(Enum):
    ticket = "ticket"
    not_tick = "not_ticket"

# Defining the Input Schmas for the API
class InpComplaint(BaseModel):
    text: str
    correct_class: Complaint
    
class InpComplaintL1(BaseModel):
    text:str
    correct_class: ComplaintL1
    
    
class InpComplaintL2(BaseModel):
    text:str
    l1_category: ComplaintL1
    correct_class: Union[Plumbing, HVAC, FireSafety, WasteMngmnt, ElevatorMngmnt, ParkingTransp, GymEqp]
    
class InpResp(BaseModel):
    complaint_text: str
    complaint_response: str
    l1_category: ComplaintL1
    complaint_class: Union[Plumbing, HVAC, FireSafety, WasteMngmnt, ElevatorMngmnt, ParkingTransp, GymEqp]
    
class InptTicket(BaseModel):
    text: str
    correct_class: Ticket

# creating routes
@router.post("/complaint_is_complete")
async def is_complete_complaint(cmp: InpComplaint):
    """
    endpoint to update the valid complaint type(complete/incomplete)
    """
    valid_complaint.update_one({"cmp_id":1}, {"$push": {cmp.correct_class.value: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }

@router.post("/complaint_l1_type")
async def classify_complaint(cmp: InpComplaintL1):
    """
    endpoint to update the correct level 1 category of the complaint
    """
    cl1.update_one(
        {cmp.correct_class.value: {"$exists":True}},
        {"$push": {cmp.correct_class.value: cmp.text}},
        upsert=True
        )
    
    return {
        "response": "updated record successfully"
    }
    
@router.post("/complaint_l2_type")
async def classify_complaint2(cmp: InpComplaintL2):
    """
    endpoint to update the correct level 2 category of the complaint
    """
    cl2.update_one(
        {cmp.l1_category.value: {"$exists":True}},
        {"$push": {f"{cmp.l1_category.value}.{cmp.correct_class.value}": cmp.text}},
        upsert=True
        )
    
    return {
        "response": "updated record successfully"
    }
    
    
@router.post("/complaint_response")
async def complaint_response(cmp: InpResp):
    """
    endpoint to update the correct response for complaint with the correct category
    """
    response.update_one(
        {cmp.l1_category.value: {"$exists":True}},
        {"$push": {
            f"{cmp.l1_category.value}.{cmp.complaint_class.value}": [
                cmp.complaint_text, cmp.complaint_response
                ]
            }
         },
        upsert=True
        )
    
    return {
        "response": "updated record successfully"
    }
    

@router.post("/ticket_clf")
async def classify_ticket(cmp: InptTicket):
    """
    endpoint to update the correct ticket type of the complaint
    """
    ticket.update_one({"cmp_id":1}, {"$push": {cmp.correct_class.value: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }