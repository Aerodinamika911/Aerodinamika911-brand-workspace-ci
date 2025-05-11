# Brand Workspace Bundle

This bundle provides a complete setup for a collaborative brand analytics workspace, including GUI tools and deployment scripts.

## Contents

- `workspace_updated.html`: The main real-time collaboration interface.
- `upload_gui.py`: A Tkinter-based GUI for uploading ZIP files to Google Drive.
- `upload_to_drive.py`: A command-line script to upload a file to Google Drive using PyDrive.
- `deploy_workspace.sh`: A bash script to deploy the updated HTML file to the public directory.
- `LICENSE.txt`: GNU General Public License v2.

## Requirements

- Python 3.x
- PyDrive (`pip install PyDrive`)
- tkinter (included with standard Python installations)
- Bash (for deployment script)

## Usage

### GUI File Upload
1. Run `upload_gui.py`.
2. Browse and select your `.zip` file.
3. Upload to Google Drive and get a shareable link.

### CLI File Upload
Run:
```bash
python upload_to_drive.py
```

### Deploy Workspace
Run:
```bash
bash deploy_workspace.sh
```

This will backup the old HTML and deploy the new one to the `./public/` folder.

---

© Released under the GNU GPL v2 License.
