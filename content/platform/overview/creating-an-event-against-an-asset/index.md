---
title: "Creating an Event Against an Asset"
description: "Creating your first Event"
lead: "Creating your first Event"
date: 2021-05-18T15:32:01+01:00
lastmod: 2021-05-18T15:32:01+01:00
draft: false
images: []
menu:
  platform:
    parent: "overview"
weight: 34
toc: true
aliases:
  - ../quickstart/creating-an-event-against-an-asset
  - /docs/rkvst-basics/creating-an-event-against-an-asset/
---

If you wish to begin tracking your Asset history and build an immutable Audit Trail, you need to create Events.

Asset Creation is the first Event. The more Events recorded against an Asset, the richer and deeper its history becomes.

Events track key moments of an Asset's lifecycle; details of Who Did What When to an Asset.

{{< note >}}
**Note:** Before creating an Event, follow [this guide](/platform/overview/creating-an-asset/) to create your first Asset.
{{< /note >}}

## Creating Events

1. Create an Event
{{< tabs name="add_event" >}}
{{{< tab name="UI" >}}
When viewing your Asset, click the `Record Event` button.
{{< img src="EventRecord.png" alt="Rectangle" caption="<em>Recording an Event</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.
[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
{{< /note >}}

To create your Event, use the action `EVENTS_CREATE`.

```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Record event against My First Container.
      asset_label: assets/<asset-id>
    behaviour: RecordEvidence
```

The `asset_id` must match the Asset ID found in the details of your Asset. See [Step 7 of Creating an Asset](/platform/overview/creating-an-asset/).
{{< /tab >}}
{{< tab name="JSON" >}}
Create an empty file, in later steps we will add the correct JSON.

```json
{

}
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. Add Event type and description
{{< tabs name="add_event_type" >}}
{{{< tab name="UI" >}}
You will see the following Event creation form:
{{< img src="EventInformation.png" alt="Rectangle" caption="<em>Entering Event Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}

Fill out metadata about your Event

`operation` and `behaviour` detail what class of Event is being performed. By default this should always be `Record` and `RecordEvidence`, respectively.

In the attributes section you should also add the required DataTrails attributes `arc_description` and `arc_display_type` to represent `Event Description` and `Event Type` from the UI.

```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Record event against My First Container.
      asset_label: assets/<asset-id> 
    operation: Record
    behaviour: RecordEvidence
    event_attributes:
      arc_description: Inspection Event
      arc_display_type:  Inspection
```

{{< /tab >}}
{{< tab name="JSON" >}}

Fill out metadata about your Event; `operation` and `behaviour` detail what class of Event is being performed. By default this should always be `Record` and `RecordEvidence`, respectively.

In the attributes section you should also add the required DataTrails attributes `arc_description` and `arc_display_type` to represent the UI fields `Event Description` and `Event Type`.

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_description": "Inspection Event",
    "arc_display_type": "Inspection",
  }
}
```

This Event will be POSTed to a specific Asset endpoint when the curl command is run. To do this, you will need the desired `assets/<asset-id>` string.
{{< /tab >}}}
{{< /tabs >}}<br>

1. You may enter both Event and Asset attributes

   `Event Attributes` - Attributes specific to an Event, i.e. which device recorded the Event<br>
   `Asset Attributes` - Attributes of the Asset that **may change** as a result of the Event, i.e. overall weight of a container
{{< tabs name="add_event_attr" >}}
{{{< tab name="UI" >}}
Select the `Add Attribute` button on each tab to add your key-value pairs.<br>You may also add an attachment to your Event. In this example we will attach a text document called `Inspection Standards` as a custom attribute. Select the symbol to upload a file.
{{< img src="AttachmentUpload.png" alt="Rectangle" caption="<em>Event Specific Attributes</em>" class="border-0" >}}

{{< img src="EventAssetAttributes.png" alt="Rectangle" caption="<em>Event Asset Attributes</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}

Add your `event_attributes` and `asset_attributes` as key-value pairs. You may also add an attachment to your Event. In this case, we have attached a PDF document labeled `Inspection Standards`

```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Record event against My First Container.
      asset_label: assets/<asset-id>
    operation: Record
    behaviour: RecordEvidence
    event_attributes:
      arc_description: Inspection Event
      arc_display_type:  Inspection
      Cargo: Rare Metals
    asset_attributes:
      Weight: "1192kg"
    attachments: 
      - filename: inspection_standards.pdf
        content_type: document/pdf
        display_name: Inspection Standards
    confirm: false
```

{{< /tab >}}
{{< tab name="JSON" >}}

You may add an attachment to your Event. To do so you will need to upload your attachment to DataTrails using the [Blobs API](/developers/api-reference/blobs-api/).

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "content_type=document/pdf" \
    -F "file=@/path/to/file" \
    https://app.datatrails.ai/archivist/v1/blobs
```

Add your `event_attributes` and `asset_attributes` as key-value pairs. Use the `blobs/<attachment-id>` returned from the curl command above as the `arc_attachment_identity` in your Event.

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_description": "Inspection Event",
    "arc_display_type": "Inspection",
    "Cargo": "Rare Metals",
    "inspection_standards": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/<blob-id>",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "standards.pdf",
      "arc_display_name": "Inspection Standards",
      },
  },
  "asset_attributes": {
    "Weight": "1192kg"
  }
}
```

{{< /tab >}}}
{{< /tabs >}}
Here we see someone noted the type of cargo loaded in the Event, and recorded the total weight of the cargo using a newly defined `Weight` attribute.<br><br>
Every Event has an automatically generated `timestamp_accepted` and `principal_accepted` attribute that records _when_ who performed what, as submitted to DataTrails.<br><br>
There is an option to append [`timestamp_declared`](/platform/overview/advanced-concepts/#timestamps-on-events) and [`principal_declared`](/platform/overview/advanced-concepts/#user-principals-on-events) attributes on the Event, for example, if the Event happened offline or a third party reports it. This creates a more detailed record.<br><br>
Documents and images can be recorded with an Event in the same way as an Asset. This is useful for storing additional material that is linked to the Audit Trail metadata for posterity.<br>For example, each `Inspection` Event can store the documentation for the specific standard used for each container inspection. This allows historical checking of Events and the standard and processes that were applied at the time.

1. Record your Event
{{< tabs name="record_event" >}}
{{{< tab name="UI" >}}
Once you have entered all data, click the `Record Event` Button to add the Event to your Asset.
{{< img src="EventRecorded.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}
You will see that the Asset Attribute we changed is also recorded in the Asset View.

{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.datatrails.com/runner/index.html) to run your YAML file!

```bash
$ archivist_runner \
      -u https://app.datatrails.ai \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      my_first_container_inspection_event.yaml
```

{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets/<asset-id>/events
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. View your Event details
{{< tabs name="view_event" >}}
{{{< tab name="UI" >}}
Click the `Event history` tab and then on a row to inspect the Event:

{{< img src="EventView.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here we see the details entered earlier and also tabs that will show both the Event attributes and Asset attribute updates:

{{< img src="EventAttributeView.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}
{{< img src="AttributeUpdatesView.png" alt="Rectangle" caption="<em>Viewing Attribute Updates</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The `EVENTS_LIST` action can be used to view all Events, or filtered using attributes (`attrs`) to view details of a specific Event

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
      description: List inspection Events against the Asset 'My First Container'.
      print_response: true
      asset_label: assets/<asset-id>
    attrs:
      arc_display_type: Inspection
    asset_attrs:
      arc_display_type: Shipping Container 
```

{{< /tab >}}
{{< tab name="JSON" >}}
Event data can be viewed using curl commands

To view all Events across all Assets, use:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v2/assets/-/events
```

To view the details of the Event you just created for My First Container, use:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v2/assets/<asset-id>/events/<event-id>
```

{{< /tab >}}}
{{< /tabs >}}
Please see the [Administration](/platform/administration/) section for information on how to manage your assets

In the next section we look at a specific type of Asset, the Document Profile Asset.
