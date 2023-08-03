---
title: "Registering an Event Against a Document Profile Asset"
description: ""
lead: ""
date: 2023-07-26T13:07:55+01:00
lastmod: 2023-07-26T13:07:55+01:00
draft: false
images: []
menu: 
  platform:
    parent: "overview"
weight: 36
toc: true
---

It is rare for a document to remain unchanged during it's lifetime. Some documents are expected to go though many versions (e.g product documentation) while others (e.g. an employment contract) change much less frequently. 

If you need to update your registered Document Profile Asset you can record this as an Event. The [Document Profile](/developers/developer-patterns/document-profile/) defines two types of Event; Publish and Withdraw.

Document Registration is the first Event with each new version being recorded as a Publish Event.

There is also the option to record an event (Record Event) that is important but is not formally part of the document profile. An example of this could be a document content review or a change in security classifiation.

When the document version is no longer to be used there is a Withdraw Event.

These Events track key moments of an Document's lifecycle; details of Who Did What When to each version of the document.

{{< note >}}
Before registering an Event, follow [this guide](/platform/overview/registering-a-document-profile-asset/) to register your first Document Asset.
{{< /note >}}

## Registering Events

1. Open the Asset Overview for a Document Profile Asset. 

{{< tabs name="add_event" >}}
{{{< tab name="UI" >}}
When viewing your Document, you have the choice of `Add New Version` (publish a new version), `Withdraw Document` (the document has reached End of Life) or `Record Event` (any other event that you wish to record).
{{< img src="AssetOverview.png" alt="Rectangle" caption="<em>Document Asset Overview</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
To use the YAML Runner, please visit [this link](https://python.rkvst.com/runner/index.html) for installation instructions.

To create your Event, use the action `EVENTS_CREATE`.
```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Record event against My First Document.
      asset_label: assets/<asset-id>
    behaviour: RecordEvidence
```
The `asset_id` must match the Asset ID found in the details of your Document. See [Step 7 of Registering a Document Profile Asset](/platform/overview/registering-a-document-profile-asset/).
{{< /tab >}}
{{< tab name="JSON" >}}
Create an empty file, in later steps we will add the correct JSON.

```json
{

}
```

{{< /tab >}}}
{{< /tabs >}}
<br>
{{< note >}}
In addition to the Asset and Event attributes that are part of the Document Profile, it is possible to record other attributes that are not part of the profile. These are:
  
* `Event Attributes` - Attributes specific to an Event, i.e. a new author.
* `Asset Attributes` - Attributes of the Asset that may change as a result of the Event, i.e. the new document hash.
{{< /note >}}
<br>
2. Add New Version.

{{< tabs name="add_new_version" >}}
{{{< tab name="UI" >}}
Information that is specific to the Document Profile is entered in the Document Information tab. As with registering the document the new version can be dragged into the Auto-fill box or you can manually enter the document hash. 
{{< img src="AddNewVersion.png" alt="Rectangle" caption="<em>Document Information</em>" class="border-0" >}}
The Advanced Options tab is for additional Asset and Event attributes that are not part of the document profile.
{{< img src="AddNewVersionDetails.png" alt="Rectangle" caption="<em>Advanced Options</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}

Add your `event_attributes` and `asset_attributes` as key-value pairs.

Fill out the metadata about your Event; `operation` and `behaviour` detail what class of Event is being performed. By default this should always be `Record` and `RecordEvidence`, respectively.

In the asset attributes section you should include the required RKVST asset attributes as defined by the document profile. The new document version hash value is `document_hash_value`, the hash algorithm is `document_hash_alg` and the `document_status` which must be `Published`.

In the event attributes section you should also add the required RKVST event attribute `arc_display_type` together with any other event specific attributes. The Document Profile specifies that `arc_display_type` must be `Publish`.  

```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Record event against My First Document.
      asset_label: assets/<asset-id>
    operation: Record
    behaviour: RecordEvidence
    asset_attributes: 
      document_hash_value: 84684c83afd5e9cb3a83439872eae74798979ff5754b15931dbe768092174ec9
      document_hash_alg: sha256
      document_version: "2"
      document_status: Published
    event_attributes:
      arc_description: Publish version 2 of My First Document
      arc_display_type: Publish
      document_version_authors:
        - display_name: Dee Author
          email: dee@writeme.org
        - display_name: Anne Author
          email: anne@writeme.org  
    confirm: true
```
{{< /tab >}}
{{< tab name="JSON" >}}
Add your `event_attributes` and `asset_attributes` as key-value pairs.

Fill out the metadata about your Event; `operation` and `behaviour` detail what class of Event is being performed. By default this should always be `Record` and `RecordEvidence`, respectively.

In the asset attributes section you should include the required RKVST asset attributes as defined by the document profile. The new document version hash value is `document_hash_value`, the hash algorithm is `document_hash_alg` and the `document_status` which must be `Published`.

In the event attributes section you should also add the required RKVST event attribute `arc_display_type` together with any other event specific attributes. The Document Profile specifies that `arc_display_type` must be `Publish`.  

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "asset_attributes": {
        "document_hash_value":"84684c83afd5e9cb3a83439872eae74798979ff5754b15931dbe768092174ec9",
        "document_hash_alg":"sha256",
        "document_version":"2",
        "document_status":"Published"
    },
  "event_attributes": {
    "arc_description": "Publish version 2 of My First Document",
    "arc_display_type": "Publish",
          "document_version_authors": [
            {
              "display_name": "Dee Author",
              "email": "dee@writeme.org"
            },
            {
              "display_name": "Anne Author",
              "email": "anne@writeme.org"
            }
          ]  
  }
}
```

This Event will be POSTed to a specific Asset endpoint when the curl command is run. To do this, you will need to include the correct `assets/<asset-id>` string for the asset in the URL.
{{< /tab >}}}
{{< /tabs >}}
<br>

3. Withdraw Event.
{{< tabs name="withdraw_event" >}}
{{{< tab name="UI" >}}
This option is the final Event in the document lifecycle. When a document is no longer to be used it is withdrawn. 
{{< img src="WithdrawEvent.png" alt="Rectangle" caption="<em>Withdraw Event</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}

Use the attibute/value pairs in the example below to register a `Withdraw` event. 
```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Withdraw My First Document.
      asset_label: assets/<asset-id>
    operation: Record
    behaviour: RecordEvidence
    asset_attributes: 
      document_status: Withdrawn
    event_attributes:
      arc_description: Withdraw My First Document
      arc_display_type: Withdraw
    confirm: true
```
{{< /tab >}}
{{< tab name="JSON" >}}

Use the attibute/value pairs in the example below to register a `Withdraw` event.
```json
{
  "behaviour": "RecordEvidence",
    "operation": "Record",
    "asset_attributes": {
        "document_status":"Withdrawn"
    },
    "event_attributes": {
        "arc_description":"Withdraw My First Document",
        "arc_display_type":"Withdraw"
    }
}
```
{{< /tab >}}}
{{< /tabs >}}
<br>
4. Record Event.

An Event type for generic events that are not part of the Document Profile lifecycle. The asset and event attributes are in separate tabs in this Event type.

See [Creating an Event Against an Asset](/platform/overview/creating-an-event-against-an-asset/) for more information on this event type.
{{< tabs name="record_event" >}}
{{{< tab name="UI" >}}

{{< img src="RecordEvent.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) to run your YAML file!
 
```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Record event against My First Document.
      asset_label: assets/<asset-id>
    operation: Record
    behaviour: RecordEvidence
    event_attributes:
      arc_description: Document review
      arc_display_type:  Review
    confirm: true
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_description": "Document Review",
    "arc_display_type": "Review",
  },
}

```
{{< /tab >}}}
{{< /tabs >}}
<br>
5. Register the Event
{{< tabs name="register_event" >}}
{{{< tab name="UI" >}}
Click on the `Record Event` button to register the event.
{{< img src="RecordEvent.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      my_first_document_event.yaml
```
{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets/<asset-id>/events
```
{{< /tab >}}}
{{< /tabs >}}
<br>
6. View your Event details. 

{{< tabs name="view_event" >}}
{{{< tab name="UI" >}}
Click the Event row to inspect the Event:

{{< img src="EventDetails.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here we see the details entered earlier and also a tab that will show both the Event attributes and Asset attributes:

{{< img src="MoreEventDetails.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
The `EVENTS_LIST` action can be used to view all Events, or filtered using attributes (`attrs`) to view details of a specific Event. 

To view all Events, use: 
```yaml
---
steps:
  - step:
      action: EVENTS_LIST
      description: List all events.
      print_response: true
```
To view the details of the Event you just created for My First Container, use:
```yaml
---
steps:
  - step:
      action: EVENTS_LIST
      description: List Events against the Document 'My First Document'.
      print_response: true
      asset_label: assets/59e2b78b-d555-49a0-8775-f336b640122e 
    attrs:
      arc_display_type: Publish
```
{{< /tab >}}
{{< tab name="JSON" >}}
Event data can be viewed using curl commands. 

To view all Events across all Assets, use:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/-/events
```

To view the details of the Event you just created for My First Document, use:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/<asset-id>/events/<event-id>
```
{{< /tab >}}}
{{< /tabs >}}


