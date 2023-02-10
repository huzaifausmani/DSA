projects = [
    {
        "name": "firstProject",
        "tags": [],
        "files": []
    },
    {
        "name": "secondProject",
        "tags": [],
        "files": ['UserFile/Hello', 'UserFile/Hello', 'UserFile/Hello', 'UserFile/Hello']
    },
    {
        "name": "thirdProject",
        "tags": [],
        "files": []
    }
]

projectFiles = projects.filter(project => project.name === "secondProject")[0].files
projectFiles.map((files) => console.log(files))