import sys
import inspect
def makeMeasureEnum(mods):
    cls=[]
    for i in range(len(mods)):
        if inspect.ismodule(mods[i][1]):
            if not mods[i][0] in sys.builtin_module_names:
                if not mods[i][0] == "inspect" and not mods[i][0] == "__builtins__":
                    tmp = inspect.getmembers(mods[i][1], inspect.isclass)
                    if tmp:
                        for i in tmp:
                            cls.append(i)
    classlist=[]
    for i in range(len(cls)):
        classlist.append(cls[i][0])
    type_dict = {classlist[x]: x for x in range(len(classlist))}
    inv_dict = {v:k for k, v in type_dict.items()} #to look up from db
    return type_dict, inv_dict
