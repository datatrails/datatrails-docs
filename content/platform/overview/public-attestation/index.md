---
 title: "Public Attestation"
 description: "Public Assets vs Permissioned Assets"
 lead: 
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   platform:
     parent: "overview"
 weight: 38
 toc: true
 aliases:
  - /docs/beyond-the-basics/public-attestation/
---
## Transparency through Public Attestation

Not everything needs to be kept secret.

Using the example of an image in a news report, the publisher needs everyone to be able to see the image but at the same time the viewers of the image want to know that it is genuine while the owner of the image will want to be credited. There needs to be a way for consumers of data to anonymously verify the data that they are consuming is genuine and also where it came from.

Public attestation allows you to [attest](https://www.merriam-webster.com/dictionary/attest) information about data to the general public, without the need for the users of the information to log-in to your DataTrails account by using `Public Assets`.

`Permissioned Assets` can only be shared through the creation of [Access Policies](/platform/administration/sharing-access-outside-your-tenant/). Public Assets, however, may be shared with a `Public URL` that points to a read-only view of the Asset, similar to the link-based sharing you may have seen in file sharing services such as Google Drive or DropBox.

Any Events recorded against a Public Asset will also be public, and each Event will have a unique Public URL.

This means that following the link to a Public Asset or Public Event will allow read-only access to the Audit Trail, without the need to sign in to DataTrails.

Anyone with the Public URL can access and view the Audit Trail and verify the data but only those with access to the Permissioned URL can make the attestation about the data.

{{< note >}}
**Note:** For more detailed Asset creation instructions, visit [Creating an Asset](/platform/overview/creating-an-asset/).
{{< /note >}}

## Creating a Publicly Attested Asset

{{< warning >}}
**Warning**: Assets can only be made public at Asset Creation and **cannot be made private afterwards**. The Asset and all its Events will be publicly accessible **forever**.
{{< /warning >}}

1. Create an Asset with your desired attributes and set it to public. See [Creating an Asset](/platform/overview/creating-an-asset/) for detailed instructions on this topic.
{{< tabs name="create_asset_public" >}}
{{{< tab name="UI" >}}
Select `Register Asset` from the sidebar and fill in the desired details.<br>
Set the toggle next to `Attest Publicly` to `ON`.
{{< img src="CreateAssetNumbered.png" alt="Rectangle" caption="<em>Asset Details</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="JSON" >}}
Create a JSON file with your desired Asset details. Set keyword `public` to true.

```json
{
    "behaviours": ["RecordEvidence"],
    "attributes": {
        "arc_display_name": "Publicly Attested Asset",
        "arc_display_type": "Example",
        "arc_description": "This example asset is publicly attested, so anyone with the link can access its details without signing in to DataTrails."
    },
    "public": true
}
```

{{< /tab >}}
{{< /tabs >}}

1. Publish your Public Asset
{{< tabs name="set_public_public" >}}
{{{< tab name="UI" >}}
Click `Register Asset` to complete your Public Asset creation.
{{< img src="CreateAsset.png" alt="Rectangle" caption="<em>Publish Your Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file. See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets
```

{{< /tab >}}
{{< /tabs >}}

1. Retrieve public link to share your Public Asset with others
{{< note >}}
**NOTE:** A Public Asset may only be updated by the Tenancy that created it. Anyone viewing the Asset using the public link will have read-only access.
{{< /note >}}
{{< tabs name="get_link_public" >}}
{{< tab name="UI" >}}
Click on the **Share** button next to the right of the Asset Details. This will open a pop-up containing options for copying the public and private links of the Asset.
{{< img src="PublicAsset.png" alt="Rectangle" caption="<em>Copy the Public Link</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
A Public Asset's URL can be retrieved via the [Assets API](/developers/api-reference/assets-api/). Use the Asset ID returned in the previous step.

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v2/assets/<asset-id>:publicurl
```

{{< /tab >}}
{{< /tabs >}}

1. The following screenshot shows the public view of the Asset when the public link is followed.
{{< img src="PublicView.png" alt="Rectangle" caption="<em>Public View</em>" class="border-0" >}}

### Adding an Event to a Public Asset

{{< note >}}
**NOTE:** Any Events added to a Public Asset will also be public. Events may only be added by the tenancy that originally created the Public Asset.
{{< /note >}}

1. Create an Event with your desired attributes. See [Creating an Event](/platform/overview/creating-an-event-against-an-asset/) for detailed instructions
{{< tabs name="create_event_public" >}}
{{{< tab name="UI" >}}
Select `Record Event` from the Asset view and fill in the desired details. When finished, click `Record Event` at the bottom right of the pop-up.
{{< img src="AddPublicEvent.png" alt="Rectangle" caption="<em>Event Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Create a JSON file with your desired Event details

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

Use the curl command to run your JSON file. See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets/<asset-id>/events
```

{{< /tab >}}
{{< /tabs >}}

1. Your Event will be readable in the Event History tab when the link to the public view is followed. Click on the Event to see the details.
{{< img src="PublicViewEvent.png" alt="Rectangle" caption="<em>Event Listed in Public View</em>" class="border-0" >}}  
1. You may also retrieve a public URL to the Event itself, using the [Assets API](/developers/api-reference/assets-api/)
{{< tabs name="get_link_event_public" >}}
{{< tab name="JSON" >}}
Use the following curl command, which will return the public URL for the Event.

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v2/assets/<asset-id>/events/<event-id>:publicurl
```

{{< /tab >}}
{{< /tabs >}}
