import pandas as pd

def load_and_preprocess_data():
    cpu_data = pd.read_csv('../data/CPUData.csv')
    gpu_data = pd.read_csv('../data/GPUData.csv')
    
    cpu_data['Hardware'] = 'CPU'
    gpu_data['Hardware'] = 'GPU'
    
    combined_data = pd.concat([cpu_data, gpu_data], ignore_index=True)
    return combined_data

if __name__ == "__main__":
    data = load_and_preprocess_data()
    print("Data loaded and preprocessed successfully.")
