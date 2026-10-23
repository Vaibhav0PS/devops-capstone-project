import sys, json
d = json.load(sys.stdin)
for j in d["jobs"]:
    print("Job:", j["name"], "| status:", j["status"], "| conclusion:", j["conclusion"])
    for s in j["steps"]:
        print("  Step %2d: %-32s %s" % (s["number"], s["name"], s["conclusion"]))
