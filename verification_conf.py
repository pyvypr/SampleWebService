verification_conf = {
  "app.routes" : {
    "paths_branching_test" : [
      Forall(
        t = calls('f')
      ).Check(
        lambda t : (
          t.duration()._in([0, 1])
        )
      )
    ]
  }
}

grouping_variable = ""

exempt_functions = [""]
