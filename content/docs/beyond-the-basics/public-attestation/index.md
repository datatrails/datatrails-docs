---
 title: "Public Attestation"
 description: "Public Assets vs Private Assets"
 lead: "Transparency through Public Attestation"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   docs:
     parent: "beyond-the-basics"
 weight: 42
 toc: true
---

You may wish to attest information to the general public, without the need for viewers to log-in to their RKVST account. `Public Assets` can be used to publicly assert data, also referred to as Public Attestation. For example, you may attest to data containing a vulnerability report against an OpenSource software package or the maintenance records for a building.

Permissioned Assets can only be shared through the creation of [Access Policies](../../rkvst-basics/sharing-assets-with-obac/). Public Assets, however, may be shared with a read-only `Public URL`, similar to the link sharing you may have seen in file sharing services such as Google Drive or DropBox. 

Any Events updating a Public Asset will also be public, and will each have their own unique Public URL.

Following the link to a Public Asset or Public Event will allow read-only access to its information, without the need to sign in to RKVST.


## Creating a Publicly Attested Asset

{{< warning >}}
**Warning**: Assets can only be made public at Asset Creation and cannot be made private afterwards. Any information published will be publicly accessible forever.
{{< /warning >}}

1. Create an Asset with your desired attributes and set it to public. See [Creating an Asset](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/) for detailed instructions. 

{{< tabs name="create_asset_public" >}}
{{{< tab name="UI" >}}
Select `Add Asset` from the sidebar and fill in the desired details.
{{< img src="CreateAsset.png" alt="Rectangle" caption="<em>Asset Details</em>" class="border-0" >}}
Check the box next to `Make Asset Public`.
{{< img src="PublicCheck.png" alt="Rectangle" caption="<em>Check Asset as Public</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Create a JSON file with your desired Asset details. Set keyword `public` to true.

```json
{
    "behaviours": ["RecordEvidence", "Attachments"],
    "attributes": {
        "arc_display_name": "Publicly Attested Asset",
        "arc_display_type": "Example",
        "arc_description": "This example asset is publicly attested, so anyone with the link can access its details without signing in to RKVST."
    },
    "public": true
}
```
{{< /tab >}}
{{< /tabs >}}

2. Publish your Public Asset.

{{< warning >}}
**WARNING:** Once an Asset is made public, it cannot be made private. Any information published will be publicly accessible forever.
{{< /warning >}}

{{< tabs name="set_public_public" >}}
{{{< tab name="UI" >}}
Click `Create Asset` to complete your Public Asset creation. 
{{< img src="PublicCheck.png" alt="Rectangle" caption="<em>Publish Your Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here. 

```bash 
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets
```

{{< /tab >}}
{{< /tabs >}}

3. Retrieve public link to share your Public Asset with others. 

{{< note >}}
**NOTE:** A Public Asset may only be updated by the tenancy that created it. Anyone viewing the Asset using the public link will have read-only access.
{{< /note >}}

{{< tabs name="get_link_public" >}}
{{{< tab name="UI" >}}
Click on the copy icon next to the green `PUBLIC` badge. This will copy the Asset's public URL to your clipboard. 
{{< img src="PublicAsset.png" alt="Rectangle" caption="<em>Copy the Public Link</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
A Public Asset's URL can be retrived via the [Assets API](https://docs.rkvst.com/docs/api-reference/assets-api/). Use the Asset ID returned in the previous step.

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/<asset-id>:publicurl
```
{{< /tab >}}
{{< /tabs >}}

4. The following screenshot shows the public view of the Asset when the link is followed. 
{{< img src="PublicView.png" alt="Rectangle" caption="<em>Public View</em>" class="border-0" >}}


### Adding an Event to a Public Asset

{{< note >}}
**NOTE:** Any Events added to a Public Asset will also be public. Events may only be added by the tenancy that originally created the Public Asset.
{{< /note >}}

1. Create an Event with your desired attributes. See [Creating an Event](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/) for detailed instructions. 

{{< tabs name="create_event_public" >}}
{{{< tab name="UI" >}}
Select `Record Event` from the Asset view and fill in the desired details. When finished, click `Record Event` at the bottom right of the pop-up.
{{< img src="AddPublicEvent.png" alt="Rectangle" caption="<em>Event Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Create a JSON file with your desired Event details. 

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_description": "Adding new information to public asset.",
    "arc_display_type": "Update",
    "Public Update": "New Information"
  }
}
```

Use the curl command to run your JSON file. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here. 

```bash 
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets/<asset-id>/events
```
{{< /tab >}}
{{< /tabs >}}

2. Your Event will be readable when the Public Asset link is followed. 

{{< img src="PublicView.png" alt="Rectangle" caption="<em>Event Listed in Public View</em>" class="border-0" >}}

{{< img src="EventPublic.png" alt="Rectangle" caption="<em>Event Information</em>" class="border-0" >}}

3. You may also retrieve a public URL to the Event itself, using the [Assets API](https://docs.rkvst.com/docs/api-reference/assets-api/). 

{{< tabs name="get_link_event_public" >}}
{{< tab name="JSON" >}}
Use the following curl command, which will return the public URL for the Event.
```bash 
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/<asset-id>/events/<event-id>:publicurl
```
{{< /tab >}}
{{< /tabs >}}