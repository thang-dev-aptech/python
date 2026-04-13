students = [
    {"name": "An", "age": 20, "scores": (8, 7, 9)},
    {"name": "Bình", "age": 21, "scores": (6, 5, 7)},
    {"name": "Cường", "age": 19, "scores": (9, 8, 10)}
]


new_list_students = [
    {
        **item,
        "avg" : sum(item["scores"]) / len(item["scores"])
    }
    for item in students
]

print(new_list_students)


max_avg = max(item["avg"] for item in new_list_students)
print(max_avg)

avg_7 = [item for item in new_list_students if item["avg"] >= 7]
print(avg_7)


desc_student = sorted(new_list_students, key=lambda x : x["avg"], reverse=True)
print(desc_student)