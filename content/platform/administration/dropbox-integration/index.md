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
weight: 45
toc: true
---

## The Dropbox Integration

Connecting your DataTrails tenancy to your Dropbox account will allow you to automatically record and maintain the provenance metadata of your files in an immutable Audit Trail.

DataTrails uses transparent and auditable distributed ledger technology to maintain an immutable trail of provenance metadata independent of, but in concert with, the original file in Dropbox. 
The original data never enters the DataTrails system and remains on Dropbox.
The provenance metadata that is recorded in the immutable audit trail can be shared and verified globally completely independently of the data itself. This increases the scope for efficient and transparent collaboration without changing the risk profile of the data.

During the set up process you will select which Dropbox folders will be linked to DataTrails. A provenance metatdata record will be created on your DataTrails tenancy for every file found within a linked folder. It will be created as a [Document Profile Asset](/developers/developer-patterns/document-profile/) which can be verified using [Instaproof](/platform/overview/instaproof/). 

From then on, each time a new file is created in a linked folder, a corresponding provenance metadata record will be created on DataTrails. Any modifications to a file in a linked folder will be recorded as a [Publish Event](/developers/developer-patterns/document-profile/#publish-event) in the provenance metadata record for that file.  
The result is that the auditable provenance record for your files begins at the moment that you link a folder and that an immutable audit trail for each file automatically grows as the files are modified. 

You are free, at any time, to link and unlink a folder at all levels of your folder tree using the instructions at [Editing the list of Linked folders](/platform/administration/dropbox-integration/#editing-the-list-of-linked-folders)

Please also see our [FAQ](https://support.datatrails.ai/hc/en-gb/articles/14378210620562-Dropbox-File-and-Folder-Management-FAQ) for more information.
{{< note >}}
**Note:** During configuration, when you link a folder in the UI we will automatically link any subfolders too. Similarly, if you unlink a folder in the UI we will automatically unlink any subfolders. 
 
If you create a subfolder in Dropbox after the integration has been set up it will be automatically added to the linked folder list. If you delete a subfolder or move it to an unlinked location it will be automatically removed from the linked folder list.

 If a folder is unlinked for any reason, such by as direct configuration or by being moved, the Audit Trail will stop. Relinking the folder will restart the Audit Trail but we cannot recover any Events that happened while the folder was unlinked.  
{{< /note >}}
{{< note >}}
**Note:** DataTrails masks the file path and replaces the filename with the Asset ID in the public Asset view that is returned by Instaproof. This is intentional so that private information cannot be accidentally released via the Instaproof search results.<br>
Knowledge of the filename is not needed to prove provenance because Instaproof will attest and verify the content of a file even if the filename has been changed.<br>
The permissioned view that is seen by an administrator who is logged into a tenancy will show the file name and the file path.
{{< /note >}}

### Connecting DataTrails to Dropbox

1. Select **Settings** or **Integrations** from the side bar and then the **Integrations** tab
{{< img src="DropboxStart.png" alt="Dropbox Integration" caption="<em>Settings</em>" class="border-0">}}
1. Select **Dropbox** and then **Proceed**.
{{< img src="DropboxProceed.png" alt="Dropbox Integration" caption="<em>Proceed</em>" class="border-0">}}
If you are already logged into Dropbox on the device that you are using to set up the integration then you will proceed directly to step 3.<br>If you are not logged in then Dropbox will ask you to authenticate.
{{< img src="DropboxAuth.png" alt="Dropbox Integration" caption="<em>Log in to Dropbox</em>" class="border-0">}}
1. DataTrails now asks for permission to see metadata for your files and folders. Click **Allow** to give DataTrails permission to access your Dropbox Folders.
{{< img src="DropboxDataTrailsAllow.png" alt="Dropbox Integration" caption="<em>Select Allow</em>" class="border-0">}}
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
{{< img src="DataTrailsDisconnect.png" alt="Dropbox Integration" caption="<em>File icon on the right</em>" class="border-0">}}
1. You will see the list of available folders. Select a folder to link or deselect a folder to unlink and then click **Confirm**
{{< img src="DropboxConfirm.png" alt="Dropbox Integration" caption="<em>Reconfigure folders and Confirm</em>" class="border-0">}}

### Disconnecting DataTrails from Dropbox

To disconnect DataTrails and Dropbox you have the option to disconnect using both applications.

1. Select the Disconnect icon in DataTrails
{{< img src="DataTrailsDisconnect.png" alt="Dropbox Integration" caption="<em>Disconnect Dropbox</em>" class="border-0">}}
You will see a warning message.
{{< img src="DisconnectWarning.png" alt="Dropbox Integration" caption="<em>Disconnect Warning</em>" class="border-0">}}
This means that this specific tenancy will no longer be used for provenance. You would do this if you no longer want to use a connected tenancy while continuing to use other connected tenancies.
1. If you also want to disconnect in Dropbox, log in to Dropbox, select your account and then **Settings** followed by the **Apps** tab. Select DataTrails and then **Disconnect**
{{< img src="DropboxDisconnectApp.png" alt="Dropbox Integration" caption="<em>Disconnect DataTrails</em>" class="border-0">}}
You would disconnect in Dropbox if you no longer wish to use DataTrails for provenance. This will remove access permissions for all your tenancies and should be done after you have disconnected all your individual tenancies in DataTrails.


This is how to connect and disconnect DataTrails and Dropbox, it is that simple! Please see our [FAQ](https://support.datatrails.ai/hc/en-gb/articles/14378210620562-Dropbox-File-and-Folder-Management-FAQ) for more information.
