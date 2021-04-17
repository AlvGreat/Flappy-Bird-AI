import pickle

with open("best.pickle", "rb") as f:
    model = pickle.load(f) # model will be saved here

#print(dir(model))

#print(model.output_nodes)
#print(model.node_evals)

print("Inputs: " + str(model.input_nodes))
print("Weights: " + str(model.values))