def findCollisions(collision):
    noOfCollisions, right = 0, 0
    for i in collision:
        if i == '<':
            noOfCollisions = noOfCollisions + right
        else: right = right + 1
    return noOfCollisions

collision = ['>','>','<','>','>','<','>','<']
print(findCollisions(collision))