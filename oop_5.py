class DictUtils:
    @staticmethod
    def from_lists(keys, values):
        your_dict = {}
        for i in range(len(keys)):
            your_dict[keys[i]] = values[i]
        return your_dict

    @staticmethod
    def from_tuples(tuple_list):
        your_dict = {}
        for t in tuple_list:
            your_dict[t[0]] = t[1]
        return your_dict

    @staticmethod
    def count_dict(items):
        your_dict = {}
        for item in items:
            if item not in your_dict:
                your_dict[item] = 0
            your_dict[item] += 1
        return your_dict

    @staticmethod
    def nested_dict(keys, default_value=None):
        if default_value is None:
            default_value = {}
        your_dict = {}
        for k in keys:
            your_dict[k] = default_value
        return your_dict

    @staticmethod
    def count_info(dictionary):
        results = {
            "keys" : 0,
            "unique_values" : 0
        }
        my_set = set()
        for k in dictionary:
            results["keys"] += 1
            if dictionary[k] not in my_set:
                my_set.add(dictionary[k])
                results["unique_values"] += 1
        return results


    @staticmethod
    def find_key_by_value(dictionary, value):
        for key in dictionary:
            if dictionary[key] == value:
                return key
        return None


    @staticmethod
    def dict_status(dictionary):
        is_empty = True
        is_full = True
        for k in dictionary:
            if not (is_empty or is_full):
                break
            if dictionary[k] is None:
                is_full = False
            else:
                is_empty = False
        if is_full:
            return "Full"
        if is_empty:
            return "Empty"
        return "Has_empty_values"

    @staticmethod
    def numeric_stats(dictionary):
        results = {
            "count" : 0,
            "sum" : 0,
            "min" : None,
            "max" : None
        }
        for key in dictionary:
            if isinstance(dictionary[key], int):
                if results["min"] is None:
                    results["min"] = dictionary[key]
                if results["max"] is None:
                    results["max"] = dictionary[key]
                if dictionary[key] < results["min"]:
                    results["min"] = dictionary[key]
                elif dictionary[key] > results["max"]:
                    results["max"] = dictionary[key]
                results["sum"] += dictionary[key]
                results["count"] += 1

    @staticmethod
    def common_keys(dict1, dict2):
        results = []
        for key in dict1:
            if key in dict2:
                results.append(key)
        return results

    @staticmethod
    def print_dict(dictionary, title="Dictionary"):
        print(f"==== {title} ====")
        for key in dictionary:
            print(f"{key}: {dictionary[key]}")
        print("* * * * * * * * * *")

    @staticmethod
    def safe_update(dictionary, key, value):
        if key in dictionary:
            dictionary[key] = value
        else:
            print(f"{key} is not exist in {dictionary}")

    @staticmethod
    def merge_dicts(dict1, dict2, conflict_strategy="keep_first"):
        results = {}
        for key in dict1:
            results[key] = dict1[key]
        for key in dict2:
            if key in results:
                if conflict_strategy == "keep_first":
                    continue
                elif conflict_strategy == "sum_values":
                    results[key] += dict2[key]
                elif conflict_strategy == "keep_second":
                    results[key] = dict2[key]
            else:
                results[key] = dict2[key]
        return results

