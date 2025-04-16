---
title: "Creating an Asset"
description: "Creating your first Asset"
lead: "Creating your first Asset"
date: 2021-05-18T14:52:25+01:00
lastmod: 2021-05-18T14:52:25+01:00
draft: false
images: []
menu:
  platform:
    parent: "overview"
weight: 33
toc: true
aliases:
  - ../quickstart/creating-an-asset
  - ../quickstart/tutorial
  - /docs/rkvst-basics/creating-an-asset/
---
An Asset can be anything: a file (a document, an image, a sound file etc.), a software application, a shipping container, or even a physical product. It can be any digital or physical object with an associated name, description, and attributes.

Each Asset will have a history of any actions performed upon it by any actor.

You may share Assets and their history with specific stakeholders using [permission sharing](/platform/administration/managing-access-to-an-asset-with-abac/). DataTrails also enables you to publicly attest the provenance of your Assets. To learn how, see [Public Attestation](/platform/overview/public-attestation/).

The creation of an Asset is the first Event in its lifecycle. The following steps will guide you in creating your first Asset.

{{< note >}}
**Note:** Please refer to [Core Concepts](/platform/overview/core-concepts/#assets) for more information on Assets.
{{< /note >}}

## Creating an Asset
1. Create your Asset
{{< tabs name="add_asset" >}}
{{< tab name="UI" >}}
Using the sidebar, select `Assets & Documents` and then `Register Asset`
{{< img src="AssetRegister.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.
[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
{{< /note >}}
The DataTrails YAML runner is executed as a series of steps, each step representing a single operation with an `action`.

In order to create an Asset we use the action `ASSETS_CREATE_IF_NOT_EXISTS`.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
```

{{< /tab >}}
{{< tab name="JSON" >}}
Create an empty file, in later steps we will add the correct JSON.

```json
{

}
```

{{< /tab >}}
{{< /tabs >}}<br>

1. Add details to your new Asset.

{{< tabs name="add_asset_details" >}}
{{{< tab name="UI" >}}
You will see an Asset Creation form, where you provide details of your new Asset:
{{< img src="AssetCreateUpdate.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Here you can fill out some more metadata about your asset:

* `selector` is the identifying attribute the yaml runner will use to check if your Asset exists already before attempting to create it. In this case, we use `arc_display_name` which represents the name of the Asset.
* `behaviours` detail what class of events in your Asset's lifecycle you might wish to record; `RecordEvidence` is the standard and recommended behavior for all Assets.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Container
    selector:
      - attributes:
        - arc_display_name
    behaviours:
      - RecordEvidence
```

{{< /tab >}}
{{< tab name="JSON" >}}
In the file you created earlier, begin adding metadata for your Asset:

* `behaviours` detail what class of events in your Asset's lifecycle you might wish to record; `RecordEvidence` is the standard and recommended behavior for all Assets.

```json
{
    "behaviours": ["RecordEvidence"]
}
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. As a minimum, you will need to add an Asset Name and Asset Type to create an Asset:

   * `Asset Name` - This is the unique name of the Asset i.e. 'My First Container'.
   * `Asset Type` - This is the class of the object; while it is arbitrary, it is best to have consistency amongst the type of Assets you use i.e. if it is a shipping container, the type could be `Shipping Container`, which will then be pre-populated for future Assets to use as their own types.
{{< tabs name="add_asset_details_min" >}}
{{{< tab name="UI" >}}
{{< img src="AssetCreateUpdate.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The YAML Runner uses the reserved attributes `arc_display_name` and `arc_display_type`  to represent `Asset Name` and `Asset Type` respectively.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Container
    selector:
      - attributes:
        - arc_display_name
    behaviours:
      - RecordEvidence
    attributes:
      arc_display_name: My First Container
      arc_display_type: Shipping Container
```

{{< /tab >}}
{{< tab name="JSON" >}}
The DataTrails API uses the reserved attributes `arc_display_name` and `arc_display_type`  to represent `Asset Name` and `Asset Type` respectively.

```json
{
    "behaviours": ["RecordEvidence"],
    "attributes": {
        "arc_display_name": "My First Container",
        "arc_display_type": "Shipping Container"
    }
}
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. At this point, you may wish to use the `Advanced Options` tab to add other details to your Asset, including extended attributes or attachments such as PDFs or Thumbnail Images.

    **Extended attributes are user-defined** and can be added to each unique Asset.

    Not all Assets of a specific type need to have the same extended attributes, but in most cases it is better to do so for consistency.

    To add a new attribute to an Asset, enter your key-value pair.

    For Example:
{{< tabs name="add_extended_attributes" >}}
{{{< tab name="UI" >}}
Select `Add Attribute`, and add your key-value pairs.
{{< img src="AssetExtendedAttributes.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Extended attributes are custom key-value pairs, such as `Width`, `Length`, and `Height` you see below.


```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Container
    selector:
      - attributes:
        - arc_display_name
    behaviours:
      - RecordEvidence
    attributes:
      arc_display_name: My First Container
      arc_display_type: Shipping Container
      arc_description: Originally shipped from Shanghai
      Width: "2.43m"
      Length: "6.06m"
      Height: "2.59m"
    confirm: false
```

{{< /tab >}}
{{< tab name="JSON" >}}
Extended attributes are custom key-value pairs, such as `Width`, `Length`, and `Height` you see below.

```json
{
    "behaviours": ["RecordEvidence"],
    "attributes": {
        "arc_display_name": "My First Container",
        "arc_display_type": "Shipping Container",
        "arc_description": "Originally shipped from Shanghai",
        "Width": "2.43m",
        "Length": "6.06m",
        "Height": "2.59m",
    }
}
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. Complete your Asset creation
{{< tabs name="finish_create_asset" >}}
{{{< tab name="UI" >}}
Click `Register Asset`
{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.datatrails.ai/runner/index.html) command to run your YAML file!

```bash
$ archivist_runner \
      -u https://app.datatrails.ai \
      --client-id <your-client-id> \
      --client-secret client_secret.txt \
      my_first_container.yaml
```

{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. View your Assets
{{< tabs name="view_all_assets" >}}
{{{< tab name="UI" >}}
Navigate to 'Assets & Documents' to see your Asset in the UI.
{{< img src="Asset.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
You can view all Asset data using the `ASSETS_LIST` action. Use the `print_response` keyword to get the full output.

```yaml
---
steps:
  - step:
      action: ASSETS_LIST
      description: List all assets.
      print_response: true
```

{{< /tab >}}
{{< tab name="JSON" >}}
You can view all Asset data using the following command.

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v2/assets
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. View details of the Asset you created
{{< tabs name="view_specific_asset" >}}
{{{< tab name="UI" >}}
To view your Asset, click on the Asset row. You will see the detailed history of your Asset.
{{< img src="AssetView.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The `ASSETS_LIST` action can be filtered using identifying attributes (`attrs`) to view the details of a specific Asset.

```yaml
---
steps:
  - step:
      action: ASSETS_LIST
      description: Display Asset named My First Container.
      print_response: true
    attrs:
      arc_display_name: My First Container
```

{{< /tab >}}
{{< tab name="JSON" >}}
Details of a specific asset can be retrieved using identifying attributes (`attrs`), such as name, type, or presence of a certain field.

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v2/assets?attributes.arc_display_name=My%20First%20Container
```

{{< /tab >}}}
{{< /tabs >}}
Here we see all details entered: The extended attributes and a history of Events recorded on the Asset.
{{< note >}}
**Note:** After registration, Assets cannot be updated using the asset creation screens but an Asset's `Asset Attributes` can be updated as part of an Event.

For more information on creating Events, [click here.](/platform/overview/creating-an-event-against-an-asset/)
{{< /note >}}
The first Event will always be the Asset Creation. In the next section, we will cover how to create your own Events for your Asset.
