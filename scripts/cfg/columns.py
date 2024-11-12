COLS_CFG_SCOPE = [
    {"name": "Column 1", "rename": "col_1", "dtype": "object", "drop": False},
    {"name": "Column 2", "rename": "col_2", "dtype": "int64", "drop": False},
    {"name": "Column 3", "rename": "col_3", "dtype": "float64", "drop": False},
    {"name": "Column 4", "rename": "col_4", "dtype": "datetime", "drop": False},
]
"""
### Is a list of dictionaries where each dictionary represents a column  configuration for a dataset. Each dictionary contains the following keys:
    - `name`: the original column name in the dataset;
    - `rename`: the new name for the column after renaming;
    - `dtype`: the desired data type for the column;
    - `drop`: a boolean flag indicating whether the column should be dropped (True) or kept (False);

Example
-------
```
for col_cfg in COLS_CFG_SCOPE:
    # Rename columns according to the 'rename' key in the configuration
    if col_cfg["rename"]:
        df.rename(columns={col_cfg["name"]: col_cfg["rename"]}, inplace=True)
    
    # Change the data type of the column according to the 'dtype' key in the configuration
    if col_cfg["dtype"]:
        df[col_cfg["rename"]] = df[col_cfg["rename"]].astype(col_cfg["dtype"])
    
    # Drop columns if the 'drop' key is set to True
    if col_cfg["drop"]:
        df.drop(columns=[col_cfg["rename"]], inplace=True)
```py
"""
