# Property


# A class without Property getter
class StorageBox:

    def __init__(self, per_drive_capacity):
        self.drives = 24
        self.space = per_drive_capacity
        self.capacity = self.space * self.drives

    def add_drives(self, count):
        self.drives += count


# A class with Property getter
class StorageBoxNew:

    def __init__(self, per_drive_capacity):
        self.drives = 24
        self.space = per_drive_capacity

    @property
    def capacity(self):
        return self.space * self.drives

    def add_drives(self, count):
        self.drives += count

# A class with Property getter with alternate syntax
class StorageBoxAlt:

    def __init__(self, per_drive_capacity):
        self.drives = 24
        self.space = per_drive_capacity

    def get_cap(self):
        return self.space * self.drives

    def add_drives(self, count):
        self.drives += count

    capacity = property(get_cap)


lsi = StorageBox(100)
emc = StorageBoxNew(100)
#emc = StorageBoxAlt(100)

print(lsi.capacity, emc.capacity)

lsi.add_drives(6)
emc.add_drives(6)

print(lsi.capacity, emc.capacity)


