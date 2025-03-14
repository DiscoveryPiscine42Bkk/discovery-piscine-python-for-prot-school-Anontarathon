
def average(score_dict):
  total = sum(score_dict.values())
  count = len(score_dict)
  return total / count
class_3D = {
  "earlene": 16,
  "jean": 15,
  "coline": 8,
  "luc": 9
}

class_3C = {
  "quentin": 17,
  "julie": 15,
  "sarah": 8,
  "stephanie": 13
}

print(f"Average for class 3D: {average(class_3D)}.")
print(f"Average for class 3C: {average(class_3C)}.")
 
    