---
title: "Registering a Document Profile Asset"
description: "Register document profile asset"
lead: ""
date: 2023-06-29T15:11:03+01:00
lastmod: 2023-06-29T15:11:03+01:00
draft: false
images: []
menu: 
  platform:
    parent: "overview"
weight: 35
toc: true
---

The RKVST document profile is a set of suggested Asset and Event attributes that allow you to trace the lifecycle of a document.

As it builds on the standard RKVST asset the same processes are used for [Permissioned Sharing](/platform/administration/managing-access-to-an-asset-with-abac/) and [Public Attestation](/platform/overview/public-attestation/).

The following steps will guide you in creating your first Document Profile Asset.

{{< note >}}
Check out our [Core Concepts](/platform/overview/core-concepts/#assets) for more general information on Assets and [Document Profile](/developers/developer-patterns/document-profile/) for details of the Document Profile asset and event attributes.
{{< /note >}}

## Registering a Document

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `rkvst-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

1. Register your Document
{{< tabs name="add_asset" >}}
{{< tab name="UI" >}}
Using the sidebar, select `Register Document`.
{{< img src="RegDocMenu.png" alt="Rectangle" caption="<em>Registering a Document</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The RKVST YAML runner is executed as a series of steps, each step representing a single operation with an `action`.

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

1. You will see the Document Registration form  
  The `Document Information` tab is where you enter the information that is required by the document profile. You have the option to drag your document into the Auto-fill box or you can enter the information into the form manually.  
  The Trust data:  

      * `Name` - This is the unique name of the Document i.e. 'My First Document'
      * `Version` - The version of your document
      * `SHA-256 Hash` - Manually enter the SHA-256 hash of this document version. If you use the auto-fill box we will calculate the SHA-256 hash for you

    Additional options:
      * `Upload on Creation` - Upload the document in addition to the trust data
      * `Attest Publicly` - Enable to allow public attestation of the document<br>  
{{< tabs name="add_asset_details" >}}
{{{< tab name="UI" >}}

{{< img src="RegDocForm2.png" alt="Rectangle" caption="<em>Document Information</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
Here you can fill out some more metadata about your asset:

* `selector` is the identifying attribute the yaml runner will use to check if your Asset exists already before attempting to create it. In this case, we use `arc_display_name` which represents the name of the Asset.
* `behaviours` detail what class of events in your Asset's lifecycle you might wish to record; `RecordEvidence` is the standard and recommended behaviour for all Assets.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Document 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
    public: true
    attributes: 
      arc_display_name: My First Document 
      arc_profile: Document
      document_hash_value: ff2f6191ec870e5120a94795274068f520168108cb8fc87f1239ffa72bd2550c
      document_hash_alg: sha256
      document_version: "1"
    confirm: true
```

{{< /tab >}}
{{< tab name="JSON" >}}
In the file you created earlier, begin adding metadata for your Asset:

* `behaviours` detail what class of events in your Asset's lifecycle you might wish to record; `RecordEvidence` is the standard and recommended behaviour for all Assets.
* `public` determines whether your document is public (*true*) or private (*false*)

```json
{
  "attributes": {
        "arc_display_name": "My First Document",
        "arc_profile": "Document",
        "document_hash_value": "ff2f6191ec870e5120a94795274068f520168108cb8fc87f1239ffa72bd2550c",
        "document_hash_alg":"sha256",
        "document_version":"1"
    },  
   "behaviours": ["RecordEvidence"],
   "public": true
}
```

{{< /tab >}}}
{{< /tabs >}}
<br>

1. The `Advanced Options` tab is where you enter the Asset Attributes that are required for all asset types and also the optional document profile asset attributes.

   * `Document Type` - This is the class of the object; while it is arbitrary, it is best to have consistency amongst the type of Documents you use i.e. if it is a purchase order, the type could be `Purchase Order`, which will then be pre-populated for future Documents to use as their own types.
   * `Proof Mechanism` - The method used to commit the blockchain transaction.

    Please see our [Advanced Concepts](/platform/overview/advanced-concepts/#proof-mechanisms) section for more information on selecting a Proof Mechanism for your Document
{{< tabs name="add_asset_details_min" >}}
{{{< tab name="UI" >}}
{{< img src="RegDocAdvancedOptions.png" alt="Rectangle" caption="<em>Advanced Options</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The YAML Runner uses the reserved attributes `arc_display_name` and `arc_display_type`  to represent `Asset Name` and `Asset Type`respectively.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Document 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
    proof_mechanism: SIMPLE_HASH
    public: true
    attributes: 
      arc_display_name: My First Document 
      arc_profile: Document
      document_hash_value: ff2f6191ec870e5120a94795274068f520168108cb8fc87f1239ffa72bd2550c
      document_hash_alg: sha256
      document_version: "1"
    confirm: true
```

{{< /tab >}}
{{< tab name="JSON" >}}
The RKVST API uses the reserved attributes `arc_display_name` and `arc_display_type`  to represent `Asset Name` and `Asset Type`respectively.

```json
{
    "attributes": {
        "arc_display_name": "My First Document",
        "arc_profile": "Document",
        "document_hash_value": "ff2f6191ec870e5120a94795274068f520168108cb8fc87f1239ffa72bd2550c",
        "document_hash_alg":"sha256",
        "document_version":"1"

    },
    "behaviours": ["RecordEvidence"],
    "proof_mechanism": "SIMPLE_HASH",
    "public": true
}
```

{{< /tab >}}}
{{< /tabs >}}

1. At this point, you may wish to add other details to your Document, including extended attributes or attachments such as PDFs or Thumbnail Images

    Extended attributes are user-defined and can be added to each unique Document.

    Not all Documents of a specific type need to have the same extended attributes, but in most cases it is better to do so for consistency.  

    To add a new attribute to a Document, enter your key-value pair.  

    For Example:
{{< tabs name="add_extended_attributes" >}}
{{{< tab name="UI" >}}
Select `Add Attribute`, and add your key-value pairs
{{< img src="RegDocAdvancedOptions2.png" alt="Rectangle" caption="<em>Document Extended Attributes</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Extended attributes are custom key-value pairs, such as `document_version`, `format`, and `some_custom_attribute` you see below.

This example also adds a location to our asset. To find out more about locations, [click here](/platform/administration/grouping-assets-by-location/).

It's also good practice to include `confirm: true` which tells RKVST to finish committing the Asset before moving to the next step.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Document 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
    proof_mechanism: SIMPLE_HASH
    public: true
    attributes: 
      arc_display_name: My First Document 
      arc_display_type: Promotional Material
      arc_profile: Document
      arc_description: PUBLIC promotional document
      document_hash_value: ff2f6191ec870e5120a94795274068f520168108cb8fc87f1239ffa72bd2550c
      document_hash_alg: sha256
      document_version: "1"
      document_status: Published
      format: pdf
      some_custom_attribute: anything you like
    confirm: true
```

{{< /tab >}}
{{< tab name="JSON" >}}
Extended attributes are custom key-value pairs, such as `document_version`, `format`, and `some_custom_attribute` you see below.

This example also adds a location to our Asset. To find out more about locations and how to find your Location ID, [click here](/platform/administration/grouping-assets-by-location/).

```json
{
    "attributes": {
        "arc_display_name": "My First Document",
        "arc_display_type": "Promotional Material",
        "arc_profile": "Document",
        "arc_description":"PUBLIC promotional document",
        "document_hash_value": "ff2f6191ec870e5120a94795274068f520168108cb8fc87f1239ffa72bd2550c",
        "document_hash_alg":"sha256",
        "document_version":"1",
        "document_status":"Published",
        "format":"pdf",
        "some_custom_attribute":"anything you like"

    },
    "behaviours": ["RecordEvidence"],
    "proof_mechanism": "SIMPLE_HASH",
    "public": true
}
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. Complete your Asset creation
{{< tabs name="finish_create_asset" >}}
{{{< tab name="UI" >}}
Click `Register Document`.
{{< img src="RegDocCreate.png" alt="Rectangle" caption="<em>Register the Document</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!

```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret client_secret.txt \
      my_first_container.yaml
```

{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

```bash
curl -v -X POST \
    -H "@$HOME/.rkvst/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. View your Document
{{< tabs name="view_all_assets" >}}
{{{< tab name="UI" >}}
Navigate to 'Assets' to see your Asset in the UI.
{{< img src="RegDocMenu.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}
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
     -H "@$HOME/.rkvst/bearer-token.txt" \
     https://app.rkvst.io/archivist/v2/assets
```

{{< /tab >}}}
{{< /tabs >}}<br>

1. View details of the Asset you created
{{< tabs name="view_specific_asset" >}}
{{{< tab name="UI" >}}
To view your Asset, click on the Asset row. You will see the detailed history of your Asset.
{{< img src="DocAsset.png" alt="Rectangle" caption="<em>Viewing Document Asset</em>" class="border-0" >}}

The extended attributes are in the `More Details` tab.
{{< img src="DocAssetDetails.png" alt="Rectangle" caption="<em>Viewing Document Asset Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The `ASSETS_LIST` action can be filtered using identifying attributes (`attrs`) to view the details of a specific Asset.

```yaml
---
steps:An Asset can be anything: a connected machine, a shipping container, or even a data set. It can be any physical or digital object with an associated name, description, and attributes.

Each
  - step:
      action: ASSETS_LIST
      description: Display Asset named My First Document.
      print_response: true
    attrs:
      arc_display_name: My First Document
```

{{< /tab >}}
{{< tab name="JSON" >}}
Details of a specific asset can be retrieved using identifying attributes (`attrs`), such as name, type, or presence of a certain field.  

```bash
curl -g -v -X GET \
     -H "@$HOME/.rkvst/bearer-token.txt" \
     https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name=My%20First%20Document
```

{{< /tab >}}}
{{< /tabs >}}<br>

Here we see all details entered: The extended attributes and a history of Events recorded on the Document.

{{< note >}}
**Note:** To update the details of your Asset after it has been created, you must create an Event containing `Asset Attributes` that conform to the [Document Profile](/developers/developer-patterns/document-profile/).

For more information on creating Events, [click here.](/platform/overview/creating-an-event-against-a-document/)
{{< /note >}}

The first Event will always be the Document Registration. In the next section, we will cover how to create your own Events for your Document.
