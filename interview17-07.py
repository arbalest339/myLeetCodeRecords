class Solution:
    def trulyMostPopular(self, names, synonyms):
        import re
        name_dict = {}
        syno_map = {}
        for name_num in names:
            mathcObj = re.search(r"([^(]*)\((\d+)\)", name_num)
            name = mathcObj.group(1)
            num = mathcObj.group(2)
            name_dict[name] = int(num)
        
        for syno_pair in synonyms:
            mathcObj = re.search(r"\(([^,]*),([^)]*)\)", syno_pair)
            name1 = mathcObj.group(1)
            name2 = mathcObj.group(2)

            if name1 not in name_dict:
                name_dict[name1] = 0
            if name2 not in name_dict:
                name_dict[name2] = 0

            old_name1 = name1
            while name1 in syno_map:
                name1 = syno_map[name1]
            if old_name1 != name1:
                syno_map[old_name1] = name1

            old_name2 = name2
            while name2 in syno_map:
                name2 = syno_map[name2]
            if old_name2 != name2:
                syno_map[old_name2] = name2

            if name2 < name1:
                name1, name2 = name2, name1
            if name1 == name2:
                continue
            syno_map[name2] = name1
            name_dict[name1] += name_dict[name2]
            name_dict[name2] = -1
        
        res = []
        for name, num in name_dict.items():
            if num >= 0:
                res.append(f"{name}({num})")
        return res


if __name__ == "__main__":
    solution = Solution()
    names = ["a(10)","c(13)"]
    synonyms = ["(a,b)","(c,d)","(b,c)"]
    solution.trulyMostPopular(names, synonyms)