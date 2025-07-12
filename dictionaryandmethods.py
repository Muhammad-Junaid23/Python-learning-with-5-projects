# we will explore dictionary and its methods

profile = {
    "name":"Not found",
    "field":"Tech",
    "country":"404",
    "rank":27
}

print("country value in profile : ",profile["country"])
print("rank in profile : ",profile["rank"])

profile["job_type"]="Remote"

print("job_type in profile : ",profile["job_type"])


print("profile data : ",profile)

# methods on dictionary
print(profile.get("name"))
print(profile.keys())
print(profile.items())
print(profile.values())



