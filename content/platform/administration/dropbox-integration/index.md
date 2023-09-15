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

Any files found in the specified directories, and their subfolders, will be added as a public [Document Profile Asset](/developers/developer-patterns/document-profile/) in RKVST that can be verified using [Instaproof](/platform/overview/instaproof/).

Each time a new file is created a corresponding asset will also be created on RKVST and modifications a file will be registered as a [Publish Event](/developers/developer-patterns/document-profile/#publish-event) on the correct asset. 

### Connecting RKVST to DropBox

1. Select **Settings** from the side bar and then the **Integrations** tab.  
{{< img src="DropBoxStart.png" alt="Dropbox Integration" caption="<em>Settings</em>" >}}

2. Select **DropBox** and then **Proceed**.
{{< img src="DropBoxProceed.png" alt="Dropbox Integration" caption="<em>Proceed</em>" >}}
{{< note >}}
**Note:** If you are setting up the integration while logged into DropBox this DropBox account will be used to connect to RKVST. If you are not logged in then DropBox will ask you to authenticate.  
{{< /note >}}
{{< img src="DropBoxAuth.png" alt="Dropbox Integration" caption="<em>Log in to DropBox</em>" >}}

3. DropBox will display an alert message. Click **Continue**.
{{< img src="DropBoxAlert.png" alt="Dropbox Integration" caption="<em>Select Continue</em>" >}}

4. Following the alert, click **Allow** to give RKVST permission to access your DropBox Folders.
{{< img src="DropBoxRKVSTAllow.png" alt="Dropbox Integration" caption="<em>Select Allow</em>" >}}

5. Select the folder on DropBox that you wish to connect to RKVST and then secect **Confirm**. The contents of this folder and *all its subfolders* will be added to RKVST as public Document Profile Assets.
{{< img src="DropBoxConfirm.png" alt="Dropbox Integration" caption="<em>Select Folder and Confirm</em>" >}}

6. You will see a success message and DropBox will be connected.
{{< img src="DropBoxSuccess.png" alt="Dropbox Integration" caption="<em>Success!</em>" >}}

Click on an icon on the right to edit the connection or to disconnect.
{{< img src="DropBoxConnected.png" alt="Dropbox Integration" caption="<em>Connected</em>" >}}

7. Check the Asset Overview to see your DropBox files.
{{< img src="DropBoxAssets.png" alt="Dropbox Integration" caption="<em>Assets</em>" >}}
{{< note >}}
**Note:** The filenames of the DropBox files is masked using the format <em>xxx...</em>  
{{< /note >}}

### Disconnecting RKVST from DropBox
To uncouple RKVST and DropBox you must disconnect using both applications.
1. Select the Disconnect icon in RKVST.
{{< img src="RKVSTDisconnect.png" alt="Dropbox Integration" caption="<em>Disconnect DropBox</em>" >}}
You will see a warning message.
{{< img src="DisconnectWarning.png" alt="Dropbox Integration" caption="<em>Disconnect Warning</em>" >}}

2. In DropBox, select your account and then **Settings** followed by the **Apps** tab. Select RKVST and then **Disconnect**. 
{{< img src="DropBoxDisconnectApp.png" alt="Dropbox Integration" caption="<em>Disconnect RKVST</em>" >}}

This is how to connect and disconnect RKVST and DropBox, it is that simple!