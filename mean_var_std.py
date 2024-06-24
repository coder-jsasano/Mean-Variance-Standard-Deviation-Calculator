import numpy as np



def calculate(input_list):
    if len(input_list) != 9:
            return ValueError("List must contain nine numbers")
    
    array = np.array(input_list).reshape(3,3)

    result = {
        'mean': [
            np.mean(array, axis=0).tolist(),  # Mean along the columns
            np.mean(array, axis=1).tolist(),  # Mean along the rows
            np.mean(array).tolist()           # Mean of the entire array
        ],
        'variance': [
            np.var(array, axis=0).tolist(),   # Variance along the columns
            np.var(array, axis=1).tolist(),   # Variance along the rows
            np.var(array).tolist()            # Variance of the entire array
        ],
        'standard deviation': [
            np.std(array, axis=0).tolist(),   # Standard deviation along the columns
            np.std(array, axis=1).tolist(),   # Standard deviation along the rows
            np.std(array).tolist()            # Standard deviation of the entire array
        ],
        'max': [
            np.max(array, axis=0).tolist(),   # Max along the columns
            np.max(array, axis=1).tolist(),   # Max along the rows
            np.max(array).tolist()            # Max of the entire array
        ],
        'min': [
            np.min(array, axis=0).tolist(),   # Min along the columns
            np.min(array, axis=1).tolist(),   # Min along the rows
            np.min(array).tolist()            # Min of the entire array
        ],
        'sum': [
            np.sum(array, axis=0).tolist(),   # Sum along the columns
            np.sum(array, axis=1).tolist(),   # Sum along the rows
            np.sum(array).tolist()            # Sum of the entire array
        ]
    }
    
    return result

input_list = [0,1,2,3,4,5,6,7,8]
print(calculate(input_list))

"""format = {
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}"""