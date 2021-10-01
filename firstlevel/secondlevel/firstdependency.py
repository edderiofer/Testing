from seconddependency import seconddependency

def firstdependency():
    try:
      seconddependency()
    except Exception as ex:
      # we could not parse it, write id to file
      print("FAILED AT SECOND DEPENDENCY")
      return