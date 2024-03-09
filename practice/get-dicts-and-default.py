# The get() method on dicts, and its "default" argument if no match

name_for_userid = {
    382: "Leo",
    590: "Tom",
    951: "Sam",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")
    
    
greeting(382) # "Hi Leo!"
greeting(666) # "Hi there!"
