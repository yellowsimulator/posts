import os
import yaml
import pandas as pd
from typing import Dict, Any, List

def get_metadata(metadata_file: str) -> Dict[str, Any]:
    """
    Read YAML metadata file and return its contents as a dictionary.

    Args:
    - metadata_file (str): Path to the YAML metadata file.

    Returns:
    - metadata (Dict[str, Any]): Dictionary containing the metadata read from the file.
    """
    with open(metadata_file, 'r') as file:
        metadata = yaml.safe_load(file)
    return metadata


def get_full_path_without_basename(file_path: str) -> str:
    """
    Get the full path of a file without the basename.

    Args:
    - file_path (str): The full path of the file.

    Returns:
    - str: The full path without the basename.
    """
    return os.path.dirname(file_path)


def get_preprocessing_description() -> str:
    """
    Extract the preprocessing description from the docstring.

    Returns:
    - str: The preprocessing description.
    """
    docstring = rename_raw_column_names.__doc__
    if docstring:
        lines = docstring.split('\n')
        preprocessing_lines = [line.strip() for line in lines if line.strip().startswith("Preprocessing done:")]
        if preprocessing_lines:
            return preprocessing_lines[0].replace("Preprocessing done: ", "").strip()
    return "Preprocessing done."


def rename_raw_column_names(metadata_file: str, new_column_names: List[str], target_folder: str = 'data/silver') -> None:
    """
    Read the metadata file, rename the important columns in the raw CSV file located in bronze,
    and save the new preprocessed CSV file and metadata file in the specified folder.

    Args:
    - metadata_file (str): Path to the YAML metadata file.
    - new_column_names (List[str]): List of new column names to rename the important columns.
    - target_folder (str): Folder where the preprocessed files will be saved. Default is 'data/silver'.

    Preprocessing done: The columns were renamed based on the provided list of new column names.
    """
    metadata = get_metadata(metadata_file)
    source_path = get_full_path_without_basename(metadata_file)
    os.makedirs(target_folder, exist_ok=True)
    preprocessing_description = get_preprocessing_description()

    for file_info in metadata['files']:
        file_name = file_info['file_name']
        selected_columns = file_info.get('selected_columns', {})
        source_file_path = os.path.join(source_path, file_name)
        source_df = pd.read_csv(source_file_path)
        column_renames = {old: new for old, new in zip(selected_columns.keys(), new_column_names)}
        source_df.rename(columns=column_renames, inplace=True)
        preprocessed_csv_path = os.path.join(target_folder, os.path.basename(file_name))
        target_df = source_df[new_column_names]
        target_df.to_csv(preprocessed_csv_path, index=False)
        
        file_info['preprocessing'] = preprocessing_description
        file_info['renamed_columns'] = {new: old for old, new in column_renames.items()}

    preprocessed_metadata_path = os.path.join(target_folder, os.path.basename(metadata_file))
    with open(preprocessed_metadata_path, 'w') as file:
        yaml.dump(metadata, file, sort_keys=False)


if __name__ == "__main__":
    metadata_path = "data/bronze/metadata.yaml"
    new_column_names = ["reference_date", "price", "product"]
    rename_raw_column_names(metadata_path, new_column_names)
    #metadata = get_metadata(path)
    #print(metadata)
