from lab01 import RunnerRegister

registry = RunnerRegister()
registry.register("Gerhard", "c3")
registry.register("Tom", "c2")
registry.register("Toni", "c1")
registry.register("Margot", "c2")
registry.register("Gerhard", "c2")
print(registry.check_runners("c2"))