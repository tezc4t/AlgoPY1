head = {
    "value" : 11,
    "next" : {
        "value" : 3,
        "next": {
            "value":23,
            "next" : {
                "value":7,
                "next": None
            }
        }
    }
}

# This work with List
print(head["next"]["next"]["value"])

# This only work with Linked List
# print(my_linked_list.head.next.next.value)