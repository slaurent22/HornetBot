import json, os, shutil

JSON_PATH = "save.json"
data : dict = {}
VERSION = 0.1

def save():
    shutil.copy2(JSON_PATH, JSON_PATH + ".bak")
    # For write-time safety - if we error mid-write then contents of the file won't be completed!

    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=4)

if not os.path.exists(JSON_PATH):
    data = {"version": VERSION, "module_templates": {}, "guilds": {}}
    save()
else:
    with open(JSON_PATH) as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Could not deserialise save.json - loading backup")
            with open(JSON_PATH + ".bak") as f2:
                data = json.load(f2)
        if VERSION > data["version"]:
            print(f"Save json is out of date! Json ver: {data['version']} < Save ver: {VERSION}")
            exit(11)

def reload():
    """Method to serialise and deserialise data from a json. Used to dereference module dictionaries"""
    global data
    save()
    with open(JSON_PATH) as f:
        data = json.load(f)

def addModuleTemplate(module_name, init_data):
    data["module_templates"][module_name] = init_data
    save()

def initModules():
    for guild_id in getGuildIds():
        modules = getGuildData(guild_id)["modules"]
        for templ_name in data["module_templates"]:
            if templ_name not in modules:
                modules[templ_name] = data["module_templates"][templ_name]
    reload()

def getGuildIds() -> list[str]:
    return data["guilds"].keys()

def getModuleData(guild_id, module_name):
    return getGuildData(guild_id)["modules"][module_name]

def getGuildData(guild_id):
    if str(guild_id) not in data["guilds"].keys():
        initGuildData(guild_id)
    return data["guilds"][str(guild_id)]

def initGuildData(guild_id : str, guild_name : str = ""):
    data["guilds"][guild_id] = {
        "nick" : guild_name,
        "adminRoles" : [],
        "spoileredPlayers": [],
        "modules"  : {module:default for module, default in list(data["module_templates"].items())}
    }
    reload()

def initModule(module_name, init_data):
    for guild_id in getGuildIds():
        modules = getGuildData(guild_id)["modules"]
        if module_name not in modules:
            modules[module_name] = init_data
            save()