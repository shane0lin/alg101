# Level 1: in memory database which support basic operation
# SET (int timestamp, String key, String field, String value)
# if field already exists, overwrite it
# CompareAndSet(int timestamp, String key, String field, String expectValue, String newValue)
# if key or field not exists -> ignore the operation
# return true if update successfully, where expectValue match current value in the data store
# CAD(int timestamp, String key, String field, string expectValue)
# Get(int time, string key, string field)
# Level 2: display record based on filters
# SCAN(int time, string key), return field(value), sort by field in lexico order
# ScanByPrefix(int time, string key, string prefix) only field matched with the prefix would be selected
# Level 3: support TTL
# SetWithTTL()
# CASWithTTL()
# Level 4: support look back operation to retrieve values stored at a specific timestamp in the past
# GetWhen(int timestamp, string key, string field, int timeAt)

class MyDB:
    def __init__(self):
        self.data = {}  # key: (field, value), timestamp
        self.ttl_data = {}  # key: (field, value), timestamp, ttl

    def SET(self, timestamp, key, field, value):
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = (value, timestamp)
    
    def CompareAndSet(self, timestamp, key, field, expectValue, newValue):
        if key not in self.data or field not in self.data[key]:
            return False
        current_value, _ = self.data[key][field]
        if current_value == expectValue:
            self.data[key][field] = (newValue, timestamp)
            return True
        return False
    
    def CAD(self, timestamp, key, field, expectValue):
        return self.CompareAndSet(timestamp, key, field, expectValue, None)
    
    def Get(self, time, key, field):
        if key not in self.data or field not in self.data[key]:
            return None
        value, timestamp = self.data[key][field]
        if timestamp <= time:
            return value
        return None
    def SCAN(self, time, key):
        if key not in self.data:
            return []
        result = []
        for field, (value, timestamp) in self.data[key].items():
            if timestamp <= time:
                result.append((field, value))
        result.sort(key=lambda x: x[0])
        return result
    def ScanByPrefix(self, time, key, prefix):
        if key not in self.data:
            return []
        result = []
        for field, (value, timestamp) in self.data[key].items():
            if field.startswith(prefix) and timestamp <= time:
                result.append((field, value))
        result.sort(key=lambda x: x[0])
        return result
    def SetWithTTL(self, timestamp, key, field, value, ttl):
        if key not in self.ttl_data:
            self.ttl_data[key] = {}
        self.ttl_data[key][field] = (value, timestamp, ttl)
    def CASWithTTL(self, timestamp, key, field, expectValue, newValue, ttl):
        if key not in self.ttl_data or field not in self.ttl_data[key]:
            return False
        current_value, current_timestamp, current_ttl = self.ttl_data[key][field]
        if current_value == expectValue and current_timestamp + current_ttl > timestamp:
            self.ttl_data[key][field] = (newValue, timestamp, ttl)
            return True
        return False
    
    def GetWhen(self, timestamp, key, field, timeAt):
        if key not in self.data or field not in self.data[key]:
            return None
        value, current_timestamp = self.data[key][field]
        if current_timestamp <= timeAt:
            return value
        return None