from dependencies import (
    db_v2,
    collection_cl1_name,
    collection_cl2_name
)

def create_l1_collection():
    data = [
        {
            "plumbing": [
            "There is a drip happening under the kitchen sink",
            "The bathroom sink is completely clogged and wont drain",
            "We need to replace the faucet in the kitchen sink",
            "The commode seat is broken",
            "Boiler needs a check up",
            "The waste tastes weird and needs a quality check",
            "Our basement is flooding, We need a quick resolution"
        ]
        },
        {
            "hvac": [
            "Radiator cold spots; not heating properly.",
            "Heat pump won't start, making strange noises.",
            "Boiler leaking water, no hot water.",
            "Ventilation fan rattling, not extracting air.",
            "AC won't turn on, breaker keeps tripping.",
            "AC unit loud, disruptive banging sounds.",
            "No heat during snowstorm, pipes might freeze."
        ]
            },
        {
            "fire safety": [
            "Alarm was silent during the fire incident.",
            "Extinguisher gauge showed empty, yet was never used.",
            "Fire drill protocol was unclear and chaotic.",
            "Small kitchen fire escalated due to no extinguisher.",
            "Fire doors were blocked during the major fire.",
            "Investigation delayed, leaving safety concerns unaddressed.",
            "Emergency exits were inaccessible during the power outage."
        ]
            },
        {"waste management": [
            "Overflowing bins not collected on designated days.",
            "Dumpsters blocking sidewalk access again.",
            "Leaking chemical containers found in alley.",
            "Long queues always at the drop-off site.",
            "Incorrect bin labeling leads to sorting confusion.",
            "Reuse program lacks clear instructions.",
            "Mixed materials, recycling effort wasted."
        ]
         },
        {"elevator maintainence":[
            "Elevator levels improperly at the third floor.",
            "Cabin smells and is covered in grime.",
            "Doors open halfway then jam.",
            "Lights flicker constantly on fifth floor stop.",
            "Elevator system is outdated, needs modernization.",
            "Interior looks shabby, requires refurbishing.",
            "Passengers trapped, elevator halted mid-level."
        ]
         },
        {"parking and transportation": [
            "Potholes in lot causing tire damage.",
            "Assigned spot consistently taken by others.",
            "Crosswalk signals not functioning properly.",
            "Elevator in garage perpetually out of service.",
            "Bike racks always full, need more.",
            "Bus schedules never align with train times.",
            "Excessive idling contributing to air pollution."
        ]},
        {"gym and fitness equipment maintainence": [
            "Pool has algae and debris, looks uninviting.",
            "Water burns eyes, seems too chlorinated.",
            "Treadmill belt keeps slipping, unusable.",
            "Weights missing, machines squeak loudly.",
            "Locker rooms smell and are dirty.",
            "First aid kit is empty, no bandages left.",
            "Stationary bike pedal broke off during use."
        ]}
        ]
    cl1 = db_v2[collection_cl1_name]
    cl1.insert_many(data)    
    
def create_l2_collection():
    data = [
        {
            "plumbing": {
                "leaks": ["There is a drip happening under the kitchen sink"],
                "blockages": ["The bathroom sink is completely clogged and wont drain"],
                "installations": ["We need to replace the faucet in the kitchen sink"],
                "repairs": ["The commode seat is broken"],
                "maintainence": ["Boiler needs a check up"],
                "water quality ": ["The waste tastes weird and needs a quality check"],
                "emergencies": ["Our basement is flooding, We need a quick resolution"]
                }
        },
        {
            "hvac": {
                "radiator malfunction": ["Radiator cold spots; not heating properly."],
                "heat pump problems": ["Heat pump won't start, making strange noises."],
                "boiler issues": ["Boiler leaking water, no hot water."],
                "ventilation fan issues": ["Ventilation fan rattling, not extracting air."],
                "ac electrical issues": ["AC won't turn on, breaker keeps tripping."],
                "ac noise issues": ["AC unit loud, disruptive banging sounds."],
                "emergencies": ["No heat during snowstorm, pipes might freeze."]
                }
        },
        {
            "fire safety": {
                "fire alarms": ["Alarm was silent during the fire incident."],
                "fire extinguishers": ["Extinguisher gauge showed empty, yet was never used."],
                "fire drills": ["Fire drill protocol was unclear and chaotic."],
                "small fires": ["Small kitchen fire escalated due to no extinguisher."],
                "major fires": ["Fire doors were blocked during the major fire."],
                "fire investigations": ["Investigation delayed, leaving safety concerns unaddressed."],
                "emergencies": ["Emergency exits were inaccessible during the power outage."]
                }
        },
        {
            "waste management": {
                "residential waste": ["Overflowing bins not collected on designated days."],
                "commercial waste": ["Dumpsters blocking sidewalk access again."],
                "hazardous waste": ["Leaking chemical containers found in alley."],
                "waste drop off centres": ["Long queues always at the drop-off site."],
                "waste sorting": ["Incorrect bin labeling leads to sorting confusion."],
                "reuse initiatives": ["Reuse program lacks clear instructions."],
                "recycling standards": ["Mixed materials, recycling effort wasted."]
                }
        },
        {
            "elevator maintainence": {
                "inspection": ["Elevator levels improperly at the third floor."],
                "cleaning": ["Cabin smells and is covered in grime."],
                "mechanical repairs": ["Doors open halfway then jam."],
                "electrical repairs": ["Lights flicker constantly on fifth floor stop."],
                "system upgrades": ["Elevator system is outdated, needs modernization."],
                "cosmetic upgrades": ["Interior looks shabby, requires refurbishing."],
                "emergencies": ["Passengers trapped, elevator halted mid-level."]
                }
        },
        {
            "parking and transportation": {
                "parking lot maintainence": ["Potholes in lot causing tire damage."],
                "parking space allocation": ["Assigned spot consistently taken by others."],
                "pedestrian safety": ["Crosswalk signals not functioning properly."],
                "parking structures": ["Elevator in garage perpetually out of service."],
                "bicycle initiatives": ["Bike racks always full, need more."],
                "public transportation coordination": ["Bus schedules never align with train times."],
                "environmental impact assesment": ["Excessive idling contributing to air pollution."]
                }
        },
        {
            "gym and fitness equipment maintainence": {
                "pool cleaning": ["Pool has algae and debris, looks uninviting."],
                "water quality testing": ["Water burns eyes, seems too chlorinated."],
                "cardio equipment maintainence": ["Treadmill belt keeps slipping, unusable."],
                "strenght equipment maintainence": ["Weights missing, machines squeak loudly."],
                "hygiene and clealiness": ["Locker rooms smell and are dirty."],
                "first aid": ["First aid kit is empty, no bandages left."],
                "mechanical issues": ["Stationary bike pedal broke off during use."]
                }
        }
    ]
    
    cl2 = db_v2[collection_cl2_name]
    cl2.insert_many(data)
    
def create_collections():
    create_l1_collection()
    create_l2_collection()

    print("Collections Created")
    print(db_v2.list_collection_names())
    
if __name__ == "__main__":
    # Collections are created for category l1 and l2
    # create_collections()
    pass