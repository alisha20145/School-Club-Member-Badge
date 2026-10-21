# ================================
# SCHOOL CLUB MEMBER BADGE
# ================================

# ---------- PART 1: member details ----------
member_name = input("Enter your real name: ")
club_name = input("Enter your club name: ")

# ---------- PART 2: data types ----------
member_number = 8
points = 9.5
is_active = True

print("Member Number:", member_number, "-> type:", type(member_number))
print("Points:", points, "-> type:", type(points))
print("Active:", is_active, "-> type:", type(is_active))

# ---------- PART 3: badge code ----------
badge_code = member_name[0:3] + club_name[-1] + str(member_number)
print("Badge code: ", badge_code)

# ---------- PART 4: final badge ----------
print("===== CLUB BADGE =====")
print("Member: " + member_name)
print("Club: " + club_name)
print("Code: " + badge_code)
print("Points: " + str(points) + ", Active: " + str(is_active))
