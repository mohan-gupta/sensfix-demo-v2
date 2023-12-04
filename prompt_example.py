import re
from typing import List, Dict

#importing the database and collection names
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

def convert_dct_to_str(dct) -> str:
    """
    Function to convert input data into string
    """
    template = """
    {label}:
    {data}
    """
    
    prmpt_text = []
    for k,v in dct.items():
        label = "/".join(k.split("_"))
        data = "\n".join(v)
        res = template.format(label=label, data=data)
        prmpt_text.append(res)
        
    return ("\n".join(prmpt_text))

def convert_ticket_data_to_str(dct):
    """
    Function to convert the ticket examples into string
    """
    template = """
    {label}:
    {examples}
    """
    
    prmpt_text = []
    for k,v in dct.items():
        eg = "\n".join(v)
        res = template.format(label=k, examples=eg)
        prmpt_text.append(res)
        
    return ("\n".join(prmpt_text))

def convert_response_data_to_str(dct):
    """
    Function to convert response examples into string
    """
    template = """
    Complaint: {complaint}:
    Response: {response}
    """
    
    prmpt_text = []
    for cmp, resp in dct:
        res = template.format(complaint=cmp, response=resp)
        prmpt_text.append(res)
        
    return ("\n".join(prmpt_text))

def l1_category_names() -> List[str]:
    """
    Function to get the list of level 1 categories
    """
    res = cl1.find(projection={"_id":0})
    
    category_l1_lst = []
    for item in res:
        category_l1_lst.extend(list(item.keys()))

    return category_l1_lst

def l2_category_names(l1_category) -> List[str]:
    """
    Function to get the list of level 2 categories for a category
    """
    res = cl2.find_one({l1_category: {"$exists": True}}, projection={"_id":0})
    category_l2_lst = []
    
    for item in res.values():
        category_l2_lst.extend(list(item.keys()))
    
    return category_l2_lst

def get_validation_examples() -> str:
    """
    Function to fetch all the examples of complete and incomplete complaints from the valid_complaint collection
    """
    data = valid_complaint.find(projection={"_id":0, "cmp_id":0})
    data = data[0]

    return convert_dct_to_str(data)
    

def get_category_l1_examples() -> str:
    """
    Function to fetch all the examples of category level 1 from the cl1 collection
    """
    data = cl1.find(projection={"_id":0})
    data_dct = {}
    
    for item in data:
        data_dct.update(item)

    return convert_dct_to_str(data_dct)

def get_category_l2_all_examples() -> Dict[str, Dict[str, List[str]]]:
    """
    Function to fetch all the data from the cl2 collection
    """   
    data = cl2.find(projection={"_id":0, "cmp_id":0})    
    data_dct = {}
    
    for item in data:
        data_dct.update(item)
        
    return data_dct

def get_category_l2_example(l2_data, category) -> str:
    """
    Function to fetch all the examples of a category from the cl2 collection
    """    
    res = ""
    
    category = re.sub("[^a-zA-Z]*", "", category)
    cat_ex = l2_data[category.lower()]
    
    res += convert_dct_to_str(cat_ex)
    
    return res

def get_ticket_examples() -> str:
    """
    Function to fetch all the examples of ticket and not ticket from the ticket collection
    """
    data = ticket.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    return convert_ticket_data_to_str(data)

def get_response_all_examples() -> Dict[str, List[str]]:
    data = response.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    
    return data

def get_response_example(response_data, category) -> str:
    """
    Function to fetch all the examples of responses for a category from the response collection
    """    
    category = category.lower()
    res = convert_response_data_to_str(response_data[category])
    return res

# if __name__ == "__main__":
#     print(l1_category_names())
#     print(l2_category_names("fire safety"))
#     print(get_validation_examples())
#     print(get_category_l1_examples())
#     l2_data = get_category_l2_all_examples()
#     print(get_category_l2_example(l2_data, "hvac"))
#     print(get_ticket_examples())
#     print(get_response_all_examples())