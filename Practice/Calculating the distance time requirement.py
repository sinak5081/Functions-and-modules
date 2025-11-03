def distance(**args):
    if "time" in args and "rate" in args:
        args["distance"]= args["rate"]*args["time"]
    elif "rate" in  args and "distance" in args:
        args["time"] = args["distance"]/args["rate"]
    elif "time" in  args and "distance" in args:
        args["rate"] = args["distance"]/args["time"]
    else:
        raise Exception("r dose not compute"%(args,))
    return args
print(distance(rate = 60,time = 0.75))
print()
print(distance(distance = 173,time = 2))