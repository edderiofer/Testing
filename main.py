from firstlevel.secondlevel.firstdependency import firstdependency

def on_run():
    try:
      firstdependency()
    except Exception as ex:
      # we could not parse it, write id to file
      print("FAILED AT FIRST DEPENDENCY")
      return


on_run()