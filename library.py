class Library:
    def __init__(self):
        self.__items = []
        self.__members = []

    def add_item(self, item):
        self.__items.append(item)

    def register_member(self, member):
        self.__members.append(member)

    def borrow_item(self, member_id, item_id):
        member = self.__find_member(member_id)
        item = self.__find_item(item_id)

        if member and item and not item.is_borrowed:
            item.borrow()
            member.borrow_item(item)
            print(f"✅ {member.name} has borrowed {item.title}.")
        else:
            print(f"❌ Could not borrow item {item_id}. Either it's not available or the member wasn't found.")

    def return_item(self, member_id, item_id):
        member = self.__find_member(member_id)
        item = self.__find_item(item_id)

        if member and item:
            item.return_item()
            member.return_item(item)
            print(f"✅ {member.name} has returned {item.title}.")
        else:
            print(f"❌ Could not return item {item_id}. Either it's not found or the member wasn't found.")

    def display_all_items(self):
        print("\n📚 All Items in the Library:\n----------------------------")
        for item in self.__items:
            print(item.display_details())

    def __find_member(self, member_id):
        for member in self.__members:
            if member.member_id == member_id:
                return member
        return None

    def __find_item(self, item_id):
        for item in self.__items:
            if item.item_id == item_id:
                return item
        return None
