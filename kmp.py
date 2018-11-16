class SimpleKMP:
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def get_temporary_array(self):
        pattern = self.pattern
        array = [0]

        j = 0
        i = 1
        while len(array) < len(pattern):
            if pattern[i] == pattern[j]:
                j += 1
                i += 1
                array.append(j)
            else:
                if j != 0:
                    j = array[j - 1]
                else:
                    array.append(0)
                    i += 1
        
        return array

    def find(self):
        array = self.get_temporary_array()
        string = self.string
        pattern = self.pattern

        found = -1

        j = 0
        i = 0
        while j != len(array):
            if string[i] == pattern[j]:
                if found == -1:
                    found = i
                j += 1
                i += 1
            else:
                j = array[j - 1]
                found = -1

        return found