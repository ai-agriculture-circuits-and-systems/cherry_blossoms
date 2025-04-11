import json
import pandas as pd
import os

def read_metadata(file_path):
    """Extract metadata from the file header."""
    print(f"Reading metadata from {file_path}")
    metadata = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        current_section = None
        for line in lines:
            if line.startswith('# '):
                if ':' in line:
                    key, value = line[2:].split(':', 1)
                    metadata[key.strip()] = value.strip()
            elif line.startswith('#--------------------'):
                current_section = None
            elif line.startswith('# '):
                current_section = line[2:].strip()
                metadata[current_section] = {}
    return metadata

def convert_flower_data(file_path):
    """Convert flower data to JSON format."""
    print(f"Converting flower data from {file_path}")
    
    # Read the data part (after the header)
    # The data is tab-delimited with no header, so we'll read it manually
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Skip the header (first 150 lines)
        for line in lines[150:]:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split('\t')
                if len(parts) >= 5:  # Make sure we have all columns
                    year = parts[0].strip()
                    if year and year != '-':  # Only include rows with valid years
                        entry = {
                            'year': int(year),
                            'day_of_year': int(parts[1]) if parts[1].strip() and parts[1].strip() != '-' else None,
                            'month_day': parts[2] if parts[2].strip() and parts[2].strip() != '-' else None,
                            'source_code': int(parts[3]) if parts[3].strip() and parts[3].strip() != '-' else None,
                            'reference': parts[4] if parts[4].strip() and parts[4].strip() != '-' else None
                        }
                        data.append(entry)
    
    print(f"Converted {len(data)} entries of flower data")
    return data

def convert_temperature_data(file_path):
    """Convert temperature data to JSON format."""
    print(f"Converting temperature data from {file_path}")
    
    # Read the data part (after the header)
    # The data is tab-delimited with no header, so we'll read it manually
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Skip the header (first 150 lines)
        for line in lines[150:]:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split('\t')
                if len(parts) >= 3:  # Make sure we have all columns
                    year = parts[0].strip()
                    if year and year != '-':  # Only include rows with valid years
                        temprec = parts[1].strip()
                        tempobs = parts[2].strip()
                        
                        entry = {
                            'year': int(year),
                            'reconstructed_temperature': float(temprec) if temprec and temprec != '-' and temprec != '-999.9' else None,
                            'observed_temperature': float(tempobs) if tempobs and tempobs != '-' and tempobs != '-999.9' else None
                        }
                        data.append(entry)
    
    print(f"Converted {len(data)} entries of temperature data")
    return data

def convert_smoothed_temperature_data(file_path):
    """Convert smoothed temperature data to JSON format."""
    print(f"Converting smoothed temperature data from {file_path}")
    
    # Read the data part (after the header)
    # The data is tab-delimited with no header, so we'll read it manually
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Skip the header (first 150 lines)
        for line in lines[150:]:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split('\t')
                if len(parts) >= 3:  # Make sure we have all columns
                    year = parts[0].strip()
                    if year and year != '-':  # Only include rows with valid years
                        temprec = parts[1].strip()
                        tempobs = parts[2].strip()
                        
                        entry = {
                            'year': int(year),
                            'smoothed_reconstructed_temperature': float(temprec) if temprec and temprec != '-' and temprec != '-999.9' else None,
                            'smoothed_observed_temperature': float(tempobs) if tempobs and tempobs != '-' and tempobs != '-999.9' else None
                        }
                        data.append(entry)
    
    print(f"Converted {len(data)} entries of smoothed temperature data")
    return data

def convert_excel_file(file_path, output_name):
    """Convert Excel file to JSON format."""
    print(f"Converting Excel file {file_path} to JSON")
    
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Convert to JSON format
        data = df.to_dict('records')
        
        # Save to JSON file
        output_path = f'json_data/{output_name}.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({'data': data}, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(data)} entries to {output_path}")
        return True
    except Exception as e:
        print(f"Error converting Excel file {file_path}: {str(e)}")
        return False

def main():
    print("Starting conversion process...")
    # Create output directory if it doesn't exist
    os.makedirs('json_data', exist_ok=True)
    print("Created json_data directory")
    
    # Convert flower data
    print("\nProcessing flower data...")
    flower_data = {
        'metadata': read_metadata('data/kyoto2010flower.txt'),
        'data': convert_flower_data('data/kyoto2010flower.txt')
    }
    
    flower_output_path = 'json_data/cherry_blossoms_flower.json'
    with open(flower_output_path, 'w', encoding='utf-8') as f:
        json.dump(flower_data, f, indent=2, ensure_ascii=False)
    print(f"Saved flower data to {flower_output_path}")
    
    # Convert temperature data
    print("\nProcessing temperature data...")
    temp_data = {
        'metadata': read_metadata('data/kyoto2010temp.txt'),
        'data': convert_temperature_data('data/kyoto2010temp.txt')
    }
    
    temp_output_path = 'json_data/cherry_blossoms_temperature.json'
    with open(temp_output_path, 'w', encoding='utf-8') as f:
        json.dump(temp_data, f, indent=2, ensure_ascii=False)
    print(f"Saved temperature data to {temp_output_path}")
    
    # Convert smoothed temperature data
    print("\nProcessing smoothed temperature data...")
    smooth_temp_data = {
        'metadata': read_metadata('data/kyoto2010tempsmooth.txt'),
        'data': convert_smoothed_temperature_data('data/kyoto2010tempsmooth.txt')
    }
    
    smooth_temp_output_path = 'json_data/cherry_blossoms_smoothed_temperature.json'
    with open(smooth_temp_output_path, 'w', encoding='utf-8') as f:
        json.dump(smooth_temp_data, f, indent=2, ensure_ascii=False)
    print(f"Saved smoothed temperature data to {smooth_temp_output_path}")
    
    # Convert Excel files
    print("\nProcessing Excel files...")
    excel_files = [
        ('data/759TempW.xls', 'cherry_blossoms_759_temp'),
        ('data/TempReconstWFinal.xls', 'cherry_blossoms_temp_reconstruction'),
        ('data/KyotoFullFlowerW.xls', 'cherry_blossoms_full_flower')
    ]
    
    for file_path, output_name in excel_files:
        convert_excel_file(file_path, output_name)
    
    print("\nConversion completed successfully!")

if __name__ == '__main__':
    main()