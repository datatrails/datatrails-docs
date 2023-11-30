---
title: "Dropbox Integration"
description: "Integrating with Dropbox"
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

## The Dropbox Integration

This integration allows you to connect your DataTrails tenancy directly with Dropbox to automatically add provenance to your files and create an immutable audit trail.

During the set up process you will select which Dropbox folders will be linked to DataTrails. Any files found in the linked folders, and their subfolders, will always be added to your DataTrails tenancy as a **public** [Document Profile Asset](/developers/developer-patterns/document-profile/). These assets can be verified using [Instaproof](/platform/overview/instaproof/).

From then on, each time a new file is created a corresponding asset will also be created on DataTrails and any modifications to an existing file will be registered as a [Publish Event](/developers/developer-patterns/document-profile/#publish-event) on the correct asset.

{{< note >}}
**Note:** DataTrails will **never** upload a copy of the file.

DataTrails uses <em>xxx...</em> to mask the file name and file path in the UI. This is intentional so that private information cannot be accidentally released via the Instaproof search results and because DataTrails is not intended to replace the excellent file management functionality that is provided by Dropbox.<br>
Knowledge of the filename is not needed to prove provenance because Instaproof will attest and verify the content of a file even if the filename has been changed.
{{< /note >}}

### Connecting DataTrails to Dropbox

1. Select **Settings** from the side bar and then the **Integrations** tab
{{< img src="DropboxStart.png" alt="Dropbox Integration" caption="<em>Settings</em>" class="border-0">}}
1. Select **Dropbox** and then **Proceed**.
{{< img src="DropboxProceed.png" alt="Dropbox Integration" caption="<em>Proceed</em>" class="border-0">}}
If you are already logged into Dropbox on the device that you are using to set up the integration then you will proceed directly to step 3.<br>If you are not logged in then Dropbox will ask you to authenticate.
{{< img src="DropboxAuth.png" alt="Dropbox Integration" caption="<em>Log in to Dropbox</em>" class="border-0">}}
1. DataTrails now asks for permission to see metadata for your files and folders. Click **Allow** to give DataTrails permission to access your Dropbox Folders.
{{< img src="DropboxRKVSTAllow.png" alt="Dropbox Integration" caption="<em>Select Allow</em>" class="border-0">}}
1. Select the Dropbox folder that you wish to link to DataTrails and then click **Confirm**. The contents of this folder and *all its subfolders* will be added to DataTrails as public Document Profile Assets.
{{< img src="DropboxConfirm.png" alt="Dropbox Integration" caption="<em>Select folder and Confirm</em>" class="border-0">}}
1. You will see a success message. Dropbox will be connected and the selected folders will be linked.
{{< img src="DropboxSuccess.png" alt="Dropbox Integration" caption="<em>Success!</em>" class="border-0">}}
Click on an icon on the right to edit the connection or to disconnect.
{{< img src="DropboxConnected.png" alt="Dropbox Integration" caption="<em>Configuration icons on the right</em>" class="border-0">}}
1. Check the Asset Overview to see your Dropbox files.
{{< img src="DropboxAssets.png" alt="Dropbox Integration" caption="<em>Assets</em>" class="border-0">}}
{{< note >}}
**Remember:** The filenames of the Dropbox files are masked using the format <em>xxx...</em>  
{{< /note >}}

### Editing the list of Linked folders
1. Select the File icon in DataTrails
{{< img src="RKVSTDisconnect.png" alt="Dropbox Integration" caption="<em>File icon on the right</em>" class="border-0">}}
1. You will see the list of available folders. Select a folder to link or deselect a folder to unlink and then click **Confirm**
{{< img src="DropboxConfirm.png" alt="Dropbox Integration" caption="<em>Reconfigure folders and Confirm</em>" class="border-0">}}

### Disconnecting DataTrails from Dropbox

To disconnect DataTrails and Dropbox you have the option to disconnect using both applications.

1. Select the Disconnect icon in DataTrails
{{< img src="RKVSTDisconnect.png" alt="Dropbox Integration" caption="<em>Disconnect Dropbox</em>" class="border-0">}}
You will see a warning message.
{{< img src="DisconnectWarning.png" alt="Dropbox Integration" caption="<em>Disconnect Warning</em>" class="border-0">}}
This means that this specific tenancy will no longer be used for provenance. You would do this if you no longer want to use a connected tenancy while continuing to use other connected tenancies.
1. If you also want to disconnect in Dropbox, log in to Dropbox, select your account and then **Settings** followed by the **Apps** tab. Select DataTrails and then **Disconnect**
{{< img src="DropboxDisconnectApp.png" alt="Dropbox Integration" caption="<em>Disconnect DataTrails</em>" class="border-0">}}
You would disconnect in Dropbox if you no longer wish to use DataTrails for provenance. This will remove access permissions for all your tenancies and should be done after you have disconnected all your individual tenancies in DataTrails.


This is how to connect and disconnect DataTrails and Dropbox, it is that simple!
