#The code below is to show job applicants who have been accepted to a job interview.
#The code based on break and continue example.
applicants = [
    {'Name':'Machio','submitted_resume':True,'Accepted_other_offer':True},
    {'Name':'Henry','submitted_resume':True,'Accepted_other_offer':False},
    {'Name':'Promise','submitted_resume':True,'Accepted_other_offer':True},
    {'Name':'Angela','submitted_resume':False,'Accepted_other_offer':True},
    {'Name':'Dancan','submitted_resume':True,'Accepted_other_offer':True},
    {'Name':'Purity','submitted_resume':True,'Accepted_other_offer':False},
    {'Name':'Jane','submitted_resume':True,'Accepted_other_offer':False},
    {'Name':'Derick','submitted_resume':False,'Accepted_other_offer':True},
    {'Name':'Sedrick','submitted_resume':True,'Accepted_other_offer':False}
]
for applicant in applicants:
    if not applicant['submitted_resume']:
        print(f"skipping {applicant['Name']}: no resume submitted")
        continue
    if applicant['Accepted_other_offer']:
        print(f"stopping intervews. {applicant['Name']} has accepted the offer")
        break
    print(f"Interviewing {applicant['Name']}...")
print("---------------------------------------------------")
    
    
    
