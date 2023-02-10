projects = [
    {
        "name":"firstProject",
        "tags":[],
        "files":[]
    },
    {
        "name":"secondProject",
        "tags":[],
        "files":['UserFile/Hello']
    },
    {
        "name":"thirdProject",
        "tags":[],
        "files":[]
    } 
]

for project in projects:
    if project["name"] == "firstProject":
        if "UserFile/Hello" in project["files"]: print("fileExists")
        else: 
            project["files"].append("UserFile/Help")
            print(projects)
            break
        
print(projects)