"""Filesystem provides API to work with files"""

class Folder:
    """Create folders. Default extension = .fld | No other arguments needed than name."""
    def __init__(self, name):
        self.name = name
        if GLOBAL_FIDS != 0:
            self.fid = len(GLOBAL_FIDS) - 1
        else:
            self.fid = 0
        GLOBAL_FIDS.append(len(GLOBAL_FIDS))
        self.addr = GLOBAL_FIDS[len(GLOBAL_FIDS) - 1]
        self.ext = "fld"
        self.type = "folder"

    def get_extension(self):
        """intended to always return .fld (fld)"""
        return self.ext

    def get_name(self):
        """folder.name is acceptable"""
        return self.name

class File:
    """Create files with custom extension and any data in content var and custom name."""
    def __init__(self, content, ext, name):
        self.content = content
        self.ext = ext
        self.name = name
        self.type = "file"

    def get_content(self):
        """file.content is acceptable"""
        return self.content

    def get_extension(self):
        """file.ext is acceptable"""
        return self.ext

    def get_name(self):
        """file.name is acceptable"""
        return self.name

GLOBAL_FIDS = []

ROOT = {}
ROOT[0] = []

def create_folder(name, parent_folder):
    """creating folder and assigning empty list to folder's id on ROOT"""
    folder_instance = Folder(name)

    ROOT[parent_folder].append(folder_instance)
    ROOT[folder_instance.addr] = []


    return folder_instance.addr

def create_file(name, ext, content, parent_folder):
    """creating file and adding it to the folder in ROOT"""
    file_instance = File(content, ext, name)
    ROOT[parent_folder].append(file_instance)

    return file_instance

def surface_folder_peek(fid):
    """returning folder contents as a tuple of names and extensions"""
    name_list = []
    ext_table = {}
    for x in ROOT[fid]:
        name_list.append(x.get_name())
        ext_table[x.get_name()] = x.get_extension()
    return (name_list, ext_table)

def recursive_folder_peek(fid): #highly instable and buggy shit!
    """return contents of folder and all it's subfulders"""
    name_list = []
    ext_table = {}

    queue = []
    queue.append(fid)

    index = 0

    while index <= len(queue) - 1:
        for x in ROOT[queue[index]]:
            if x.type == "folder":
                queue.append(x.addr)
                name_list.append(x.get_name())
                ext_table[x.get_name()] = x.get_extension()
            else:
                name_list.append(x.get_name())
                ext_table[x.get_name()] = x.get_extension()

            index += 1

    return (name_list, ext_table)

def delete_file(fid, name):
    deleted = False
    for i in range(0, len(ROOT[fid])):
        if ROOT[fid][i].get_name() == name:
            deleted = ROOT[fid].pop(i)
            break
    return deleted
            

def surface_folder_delete(fid):
    """Deletes folder. DOES NOT delete subfolder contents!"""
    subfolders_fids = []

    for x in ROOT[fid]:
        if x.type == "folder":
            subfolders_fids.append(x.fid)
        ROOT[fid].pop(ROOT[fid].index(x))

create_folder("mm folde", 0)
create_folder("le folde", 0)
create_file("nigger", "nigga", "nigger content", 1)
tuplel = surface_folder_peek(1)
for i in range(0, len(tuplel[0])):
    print(tuplel[1][tuplel[0][i]])
print(ROOT)
input()