#!/bin/bash

# Set the target directory
TARGET_DIR="./src/leetcode/questions"

# Check if the directory exists
if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: Directory $TARGET_DIR does not exist."
    exit 1
fi

# Find the longest directory name for alignment
max_length=0
total_files=0

for subdir in "$TARGET_DIR"/*/; do
    if [[ -d "$subdir" ]]; then
        name=$(basename "$subdir")
        [[ ${#name} -gt $max_length ]] && max_length=${#name}
    fi
done

# Print aligned results and calculate total files
for subdir in "$TARGET_DIR"/*/; do
    if [[ -d "$subdir" ]]; then
        count=$(find "$subdir" -maxdepth 1 -type f | wc -l)
        total_files=$((total_files + count))
        printf "%-${max_length}s : %3d problems\n" "$(basename "$subdir")" "$count"
    fi
done

# Print total count
echo "----------------------------------"
printf "%-${max_length}s : %3d problems\n" "Total" "$total_files"
