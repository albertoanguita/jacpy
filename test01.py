# from hash.hash import DirItemPolicy
from hash import hashUtils


items = hash.dirItems('C:/Users/alber/Desktop/BACKUP ABRIL 2022', hash.DirItemPolicy.AllAlphabetic, 0, 2)

print(items)