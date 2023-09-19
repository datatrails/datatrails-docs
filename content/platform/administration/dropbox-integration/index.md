---
title: "Dropbox Integration"
description: "Integrating with DropBox"
lead: ""
date: 2023-09-15T13:18:42+01:00
lastmod: 2023-09-15T13:18:42+01:00
draft: false
images: []
menu: 
  platform:
    parent: "administration"
weight: 47
toc: true
---

## The DropBox Integration
This integration allows you to link your RKVST tenancy directly with DropBox to automatically add provenance to your files. 

During the set up process, any files found in the configured directories and their subfolders will always be added to your RKVST tenancy as a **public** [Document Profile Asset](/developers/developer-patterns/document-profile/). These assets can be verified using [Instaproof](/platform/overview/instaproof/).

From then on, each time a new file is created a corresponding asset will also be created on RKVST and any modifications to an existing file will be registered as a [Publish Event](/developers/developer-patterns/document-profile/#publish-event) on the correct asset. 

{{< note >}}
**Note:** RKVST will **never** upload a copy of the file.

The file name and file path are masked in the UI. This is intentional so that private information cannot be accidentally released via the Instaproof search results and because RKVST is not intended to replace the excellent file management functionality that is provided by DropBox.<br>
Knowledge of the filename is not needed to prove provenance because Instaproof will attest and verify the content of a file even if the filename has been changed. 
{{< /note >}}

### Connecting RKVST to DropBox

1. Select **Settings** from the side bar and then the **Integrations** tab.  
{{< img src="DropBoxStart.png" alt="Dropbox Integration" caption="<em>Settings</em>" class="border-0">}}

2. Select **DropBox** and then **Proceed**.
{{< img src="DropBoxProceed.png" alt="Dropbox Integration" caption="<em>Proceed</em>" class="border-0">}}
If you are already logged into DropBox on the device that you are using to set up the integration then you will proceed directly to step 3.<br>If you are not logged in then DropBox will ask you to authenticate.  

{{< img src="DropBoxAuth.png" alt="Dropbox Integration" caption="<em>Log in to DropBox</em>" class="border-0">}}

3. DropBox will display an alert message. Click **Continue**.
{{< img src="DropBoxAlert.png" alt="Dropbox Integration" caption="<em>Select Continue</em>" class="border-0">}}

4. Following the alert, click **Allow** to give RKVST permission to access your DropBox Folders.
{{< img src="DropBoxRKVSTAllow.png" alt="Dropbox Integration" caption="<em>Select Allow</em>" class="border-0">}}

5. Select the folder on DropBox that you wish to connect to RKVST and then secect **Confirm**. The contents of this folder and *all its subfolders* will be added to RKVST as public Document Profile Assets.
{{< img src="DropBoxConfirm.png" alt="Dropbox Integration" caption="<em>Select Folder and Confirm</em>" class="border-0">}}

6. You will see a success message and DropBox will be connected.
{{< img src="DropBoxSuccess.png" alt="Dropbox Integration" caption="<em>Success!</em>" class="border-0">}}

Click on an icon on the right to edit the connection or to disconnect.
{{< img src="DropBoxConnected.png" alt="Dropbox Integration" caption="<em>Connected</em>" class="border-0">}}

7. Check the Asset Overview to see your DropBox files.
{{< img src="DropBoxAssets.png" alt="Dropbox Integration" caption="<em>Assets</em>" class="border-0">}}
{{< note >}}
**Remember:** The filenames of the DropBox files are masked using the format <em>xxx...</em>  
{{< /note >}}

### Disconnecting RKVST from DropBox
To uncouple RKVST and DropBox you must disconnect using both applications.
1. Select the Disconnect icon in RKVST.
{{< img src="RKVSTDisconnect.png" alt="Dropbox Integration" caption="<em>Disconnect DropBox</em>" class="border-0">}}
You will see a warning message.
{{< img src="DisconnectWarning.png" alt="Dropbox Integration" caption="<em>Disconnect Warning</em>" class="border-0">}}

2. In DropBox, select your account and then **Settings** followed by the **Apps** tab. Select RKVST and then **Disconnect**. 
{{< img src="DropBoxDisconnectApp.png" alt="Dropbox Integration" caption="<em>Disconnect RKVST</em>" class="border-0">}}

This is how to connect and disconnect RKVST and DropBox, it is that simple!