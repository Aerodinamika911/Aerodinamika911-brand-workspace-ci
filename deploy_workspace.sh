
#!/bin/bash

# Define paths
TARGET_DIR="./public"
UPDATED_FILE="workspace_updated.html"
DEST_FILE="${TARGET_DIR}/workspace.html"

# Ensure target directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Creating target directory: $TARGET_DIR"
  mkdir -p "$TARGET_DIR"
fi

# Backup old file if it exists
if [ -f "$DEST_FILE" ]; then
  echo "Backing up existing workspace.html to workspace_backup.html"
  cp "$DEST_FILE" "${TARGET_DIR}/workspace_backup.html"
fi

# Copy updated file
echo "Deploying updated workspace.html"
cp "$UPDATED_FILE" "$DEST_FILE"

# Print success message
echo "Deployment complete. File copied to $DEST_FILE"
